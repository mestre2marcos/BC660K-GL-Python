from collections import deque

import pytest

from bc660k.exceptions import ATCommandError, ModemTimeoutError
from bc660k.transport import ATTransport


class FakeSerial:
    def __init__(self, *args, **kwargs) -> None:
        self.readline_queue = deque()
        self.read_bytes = deque()
        self.writes = []
        self.is_open = True

    def write(self, data: bytes) -> int:
        self.writes.append(data)
        return len(data)

    def flush(self) -> None:
        return None

    def close(self) -> None:
        self.is_open = False

    def reset_input_buffer(self) -> None:
        self.readline_queue.clear()
        self.read_bytes.clear()

    def readline(self) -> bytes:
        if self.readline_queue:
            return self.readline_queue.popleft()
        return b""

    def read(self, n: int = 1) -> bytes:
        if self.read_bytes:
            return self.read_bytes.popleft()
        return b""


def make_transport(monkeypatch: pytest.MonkeyPatch) -> ATTransport:
    monkeypatch.setattr("bc660k.transport.serial.Serial", FakeSerial)
    return ATTransport("COMX", 115200)


def test_send_at_once_ok(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    at.ser.readline_queue.extend([b"AT\r\n", b"+CPIN: READY\r\n", b"OK\r\n"])

    lines = at.send_at_once("AT", timeout_s=0.05)
    assert lines == ["+CPIN: READY", "OK"]


def test_send_at_once_error(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    at.ser.readline_queue.extend([b"AT+CGATT=1\r\n", b"+CME ERROR: ue fail\r\n"])

    with pytest.raises(ATCommandError):
        at.send_at_once("AT+CGATT=1", timeout_s=0.05)


def test_send_at_retries_after_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    calls = []

    def fake_send(cmd: str, timeout_s: float = 8.0):
        calls.append(cmd)
        if len(calls) == 1:
            raise ATCommandError("first fail")
        return ["OK"]

    monkeypatch.setattr(at, "send_at_once", fake_send)
    result = at.send_at("AT+CSQ", timeout_s=0.05)

    assert result == ["OK"]
    assert calls == ["AT+CSQ", "AT", "AT+CSQ"]


def test_wait_prompt_success(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    at.ser.read_bytes.extend([b"x", b">"])
    at.wait_prompt(timeout_s=0.05)


def test_wait_prompt_error(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    for b in b"+CME ERROR":
        at.ser.read_bytes.append(bytes([b]))

    with pytest.raises(ATCommandError):
        at.wait_prompt(timeout_s=0.05)


def test_wake_modem_success(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    monkeypatch.setattr(at, "flush_input", lambda: None)
    at.ser.readline_queue.extend([b"AT\r\n", b"OK\r\n"])
    at.wake_modem(attempts=1)


def test_wait_urc_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    at = make_transport(monkeypatch)
    with pytest.raises(ModemTimeoutError):
        at.wait_urc(r"^\\+QMTOPEN", timeout_s=0.01)
