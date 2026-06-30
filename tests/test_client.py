from collections import deque

import pytest

from bc660k.client import BC660KClient
from bc660k.exceptions import BC660KError
from bc660k.models import HTTPConfig, MQTTConfig, NetworkConfig, SerialConfig


class FakeSerialEndpoint:
    def __init__(self) -> None:
        self.writes: list[bytes] = []

    def write(self, data: bytes) -> int:
        self.writes.append(data)
        return len(data)

    def flush(self) -> None:
        return None


class FakeAT:
    def __init__(self, *args, **kwargs) -> None:
        self.commands: list[str] = []
        self.responses: dict[str, list[str]] = {}
        self.urc_queue: deque[str] = deque()
        self.ser = FakeSerialEndpoint()
        self.prompt_waits = 0
        self.data_writes: list[tuple[str, bool]] = []
        self.woke = False

    def close(self) -> None:
        return None

    def wake_modem(self) -> None:
        self.woke = True

    def send_at(self, cmd: str, timeout_s: float = 8.0) -> list[str]:
        self.commands.append(cmd)
        if cmd in self.responses:
            return self.responses[cmd]
        return ["OK"]

    def wait_urc(self, regex: str, timeout_s: float = 8.0) -> str:
        if not self.urc_queue:
            raise BC660KError(f"URC ausente para regex {regex}")
        return self.urc_queue.popleft()

    def wait_prompt(self, timeout_s: float = 8.0) -> None:
        self.prompt_waits += 1

    def write_data(self, data: str, end_with_ctrl_z: bool = False) -> None:
        self.data_writes.append((data, end_with_ctrl_z))


def make_client(monkeypatch: pytest.MonkeyPatch) -> BC660KClient:
    monkeypatch.setattr("bc660k.client.ATTransport", FakeAT)
    return BC660KClient(SerialConfig())


def test_initialize_default(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    client.initialize(disable_sleep=True)

    assert client.at.woke is True
    assert "ATE0" in client.at.commands
    assert "AT+CMEE=2" in client.at.commands
    assert "AT+QSCLK=0" in client.at.commands
    assert "AT+CPIN?" in client.at.commands


def test_configure_network_happy_path(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    cfg = NetworkConfig(apn="apn.test", apn_user="u", apn_pass="p", operator="00101", cid=1)

    monkeypatch.setattr(client, "_ensure_attach", lambda retries: None)
    monkeypatch.setattr(client, "_ensure_pdp_ip", lambda cid: None)

    client.configure_network(cfg)

    assert 'AT+COPS=1,2,"00101"' in client.at.commands
    assert 'AT+QCGDEFCONT="IP","apn.test","u","p"' in client.at.commands
    assert 'AT+CGDCONT=1,"IP","apn.test"' in client.at.commands
    assert 'AT+CGAUTH=1,1,"u","p"' in client.at.commands


def test_ensure_pdp_ip_activates_when_needed(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    client.at.responses = {
        "AT+CGPADDR=0": ["+CGPADDR: 0,\"0.0.0.0\"", "OK"],
        "AT+QIACT=0": ["OK"],
        "AT+CGACT=1,0": ["OK"],
    }

    def cgpaddr_toggle(cmd: str, timeout_s: float = 8.0) -> list[str]:
        client.at.commands.append(cmd)
        if cmd == "AT+CGPADDR=0":
            if client.at.commands.count("AT+CGPADDR=0") == 1:
                return ["+CGPADDR: 0,\"0.0.0.0\"", "OK"]
            return ["+CGPADDR: 0,\"10.1.1.2\"", "OK"]
        return ["OK"]

    monkeypatch.setattr(client.at, "send_at", cgpaddr_toggle)
    client._ensure_pdp_ip(0)

    assert "AT+QIACT=0" in client.at.commands
    assert "AT+CGACT=1,0" in client.at.commands


def test_mqtt_publish_non_ssl(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    client.at.responses["AT+QMTOPEN?"] = ["OK"]
    client.at.urc_queue.extend([
        "+QMTOPEN: 0,0",
        "+QMTCONN: 0,0,0",
        "+QMTPUB: 0,0,0",
    ])

    cfg = MQTTConfig(topic="t", message="m", qos=0)
    client.mqtt_publish(cfg)

    assert 'AT+QMTOPEN=0,"test.mosquitto.org",1883' in client.at.commands
    assert any(cmd.startswith("AT+QMTCONN=0,") for cmd in client.at.commands)
    assert client.at.prompt_waits >= 1
    assert client.at.data_writes[-1] == ("m", True)


def test_mqtt_publish_ssl_configures_tls(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    client.at.responses["AT+QMTOPEN?"] = ["OK"]
    client.at.urc_queue.extend([
        "+QMTOPEN: 0,0",
        "+QMTCONN: 0,0,0",
        "+QMTPUB: 0,0,0",
    ])

    cfg = MQTTConfig(
        broker="secure-broker",
        broker_port=8883,
        topic="tls/topic",
        message="hello",
        use_ssl=True,
        ssl_context_id=0,
        ssl_connect_id=0,
        ssl_seclevel=0,
        ssl_version=4,
    )
    client.mqtt_publish(cfg)

    assert 'AT+QSSLCFG=0,0,"seclevel",0' in client.at.commands
    assert 'AT+QSSLCFG=0,0,"sslversion",4' in client.at.commands
    assert 'AT+QMTCFG="ssl",0,1,0,0' in client.at.commands
    assert 'AT+QMTOPEN=0,"secure-broker",8883' in client.at.commands


def test_http_get_success(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    client.at.urc_queue.extend([
        "OK",
        "+QHTTPGET: 0,200",
    ])

    def send_at(cmd: str, timeout_s: float = 8.0) -> list[str]:
        client.at.commands.append(cmd)
        if cmd.startswith("AT+QHTTPREAD="):
            if client.at.commands.count(cmd) == 1:
                return ["+QHTTPREAD: 0,15", "hello-body", "OK"]
            return ["+QHTTPREAD: 0,0", "OK"]
        return ["OK"]

    monkeypatch.setattr(client.at, "send_at", send_at)
    body = client.http_get("http://example.com/", HTTPConfig(context_id=0, response_header=1))

    assert "hello-body" in body
    assert any(cmd.startswith("AT+QHTTPGET=") for cmd in client.at.commands)


def test_mqtt_open_error_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    client = make_client(monkeypatch)
    client.at.responses["AT+QMTOPEN?"] = ["OK"]
    client.at.urc_queue.extend([
        "+QMTOPEN: 0,-1",
    ])

    with pytest.raises(BC660KError):
        client.mqtt_publish(MQTTConfig())
