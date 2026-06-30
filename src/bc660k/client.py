"""High-level BC660K client for setup, network, HTTP(S), and MQTT."""

from __future__ import annotations

import re
import time

from .exceptions import BC660KError
from .models import HTTPConfig, MQTTConfig, NetworkConfig, SerialConfig
from .transport import ATTransport


class BC660KClient:
    """Facade for common BC660K workflows.

    The client follows Quectel application notes and keeps resilience for
    sleep/wake timing, stale MQTT sessions, and network attach retries.
    """

    def __init__(self, serial_cfg: SerialConfig) -> None:
        self.serial_cfg = serial_cfg
        self.at = ATTransport(serial_cfg.port, serial_cfg.baud, timeout=serial_cfg.timeout)

    def close(self) -> None:
        self.at.close()

    def __enter__(self) -> "BC660KClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    @staticmethod
    def _parse_cereg_stat(lines: list[str]) -> int | None:
        for line in lines:
            if line.startswith("+CEREG:"):
                parts = [p.strip() for p in line.split(":", 1)[1].split(",")]
                if len(parts) >= 2 and parts[1].isdigit():
                    return int(parts[1])
        return None

    @staticmethod
    def _has_valid_ip(lines: list[str], cid: int) -> bool:
        for line in lines:
            if line.startswith("+CGPADDR:") and f"+CGPADDR: {cid}," in line:
                ip = line.split(",", 1)[1].strip().strip('"')
                if ip and ip != "0.0.0.0":
                    return True
        return False

    def initialize(self, disable_sleep: bool = True) -> None:
        """Run initial modem setup in AT mode."""
        self.at.wake_modem()
        self.at.send_at("ATE0")
        self.at.send_at("AT+CMEE=2")
        if disable_sleep:
            self.at.send_at("AT+QSCLK=0")
        self.at.send_at("AT+CPIN?")

    def configure_network(self, cfg: NetworkConfig) -> None:
        """Configure operator, APN, attach, and PDP activation."""
        if cfg.nbiot_only:
            try:
                self.at.send_at('AT+QCFG="nwscanmode",3')
            except BC660KError:
                pass

        if cfg.roaming:
            try:
                self.at.send_at('AT+QCFG="roamservice",1')
            except BC660KError:
                pass

        if cfg.operator:
            try:
                self.at.send_at(f'AT+COPS=1,2,"{cfg.operator}"', timeout_s=20.0)
            except BC660KError:
                self.at.send_at("AT+COPS=0", timeout_s=20.0)
        else:
            self.at.send_at("AT+COPS=0", timeout_s=20.0)

        if cfg.apn_user:
            self.at.send_at(
                f'AT+QCGDEFCONT="IP","{cfg.apn}","{cfg.apn_user}","{cfg.apn_pass}"'
            )
        else:
            self.at.send_at(f'AT+QCGDEFCONT="IP","{cfg.apn}"')

        if cfg.cid != 0:
            self.at.send_at(f'AT+CGDCONT={cfg.cid},"IP","{cfg.apn}"')
            if cfg.apn_user:
                self.at.send_at(f'AT+CGAUTH={cfg.cid},1,"{cfg.apn_user}","{cfg.apn_pass}"')

        self._ensure_attach(cfg.attach_retries)
        self._ensure_pdp_ip(cfg.cid)

    def _wait_network_registration(self, timeout_s: float) -> bool:
        deadline = time.time() + timeout_s
        while time.time() < deadline:
            try:
                lines = self.at.send_at("AT+CEREG?", timeout_s=6.0)
                if self._parse_cereg_stat(lines) in (1, 5):
                    return True
            except BC660KError:
                pass
            time.sleep(3)
        return False

    def _ensure_attach(self, retries: int) -> None:
        for _ in range(retries):
            try:
                self.at.send_at("AT+CGATT=1", timeout_s=30.0)
            except BC660KError:
                pass
            if self._wait_network_registration(timeout_s=25.0):
                return
        cops = self.at.send_at("AT+COPS=?", timeout_s=130.0)
        raise BC660KError(f"Falha ao registrar na rede. COPS: {' | '.join(cops)}")

    def _ensure_pdp_ip(self, cid: int) -> None:
        lines = self.at.send_at(f"AT+CGPADDR={cid}", timeout_s=10.0)
        if self._has_valid_ip(lines, cid):
            return

        try:
            self.at.send_at(f"AT+QIACT={cid}", timeout_s=25.0)
        except BC660KError:
            pass

        try:
            self.at.send_at(f"AT+CGACT=1,{cid}", timeout_s=25.0)
        except BC660KError:
            pass

        lines = self.at.send_at(f"AT+CGPADDR={cid}", timeout_s=10.0)
        if not self._has_valid_ip(lines, cid):
            raise BC660KError(f"PDP sem IP valido no CID {cid}")

    def _reset_mqtt_state(self, connect_id: int) -> None:
        try:
            lines = self.at.send_at("AT+QMTOPEN?", timeout_s=6.0)
        except BC660KError:
            lines = []

        if any(line.startswith("+QMTOPEN:") for line in lines):
            for cmd in (f"AT+QMTDISC={connect_id}", f"AT+QMTCLOSE={connect_id}"):
                try:
                    self.at.send_at(cmd, timeout_s=10.0)
                except BC660KError:
                    pass

    def mqtt_publish(self, cfg: MQTTConfig) -> None:
        """Publish one MQTT message with open/connect/publish/disconnect flow."""
        self._reset_mqtt_state(cfg.connect_id)
        self._configure_mqtt(cfg)

        self.at.send_at(
            f'AT+QMTOPEN={cfg.connect_id},"{cfg.broker}",{cfg.broker_port}', timeout_s=8.0
        )
        open_line = self.at.wait_urc(rf"^\+QMTOPEN:\s*{cfg.connect_id},(-?\d+)", timeout_s=60.0)
        open_result = int(re.search(r",(-?\d+)$", open_line).group(1))
        if open_result != 0:
            raise BC660KError(f"QMTOPEN falhou com codigo {open_result}")

        if cfg.username:
            conn_cmd = (
                f'AT+QMTCONN={cfg.connect_id},"{cfg.client_id}","{cfg.username}","{cfg.password}"'
            )
        else:
            conn_cmd = f'AT+QMTCONN={cfg.connect_id},"{cfg.client_id}"'

        self.at.send_at(conn_cmd, timeout_s=8.0)
        conn_line = self.at.wait_urc(
            rf"^\+QMTCONN:\s*{cfg.connect_id},(\d+),(\d+)", timeout_s=30.0
        )
        match = re.search(r":\s*\d+,(\d+),(\d+)", conn_line)
        result = int(match.group(1))
        ret_code = int(match.group(2))
        if result != 0 or ret_code != 0:
            raise BC660KError(f"QMTCONN falhou: result={result}, ret_code={ret_code}")

        msg_id = 0 if cfg.qos == 0 else 1
        pub_cmd = (
            f'AT+QMTPUB={cfg.connect_id},{msg_id},{cfg.qos},{cfg.retain},"{cfg.topic}"'
        )
        self.at.ser.write((pub_cmd + "\r").encode("ascii"))
        self.at.ser.flush()
        self.at.wait_prompt(timeout_s=8.0)
        self.at.write_data(cfg.message, end_with_ctrl_z=True)
        self.at.wait_urc(rf"^\+QMTPUB:\s*{cfg.connect_id},\d+,\d+", timeout_s=30.0)

        self.mqtt_close(cfg.connect_id)

    def _configure_mqtt(self, cfg: MQTTConfig) -> None:
        if cfg.use_ssl:
            self._configure_mqtt_ssl(cfg)

        try:
            self.at.send_at(f'AT+QMTCFG="will",{cfg.connect_id}')
            self.at.send_at(f'AT+QMTCFG="session",{cfg.connect_id},{cfg.clean_session}')
            self.at.send_at(f'AT+QMTCFG="keepalive",{cfg.connect_id},{cfg.keepalive}')
            self.at.send_at(f'AT+QMTCFG="timeout",{cfg.connect_id},30')
            self.at.send_at(f'AT+QMTCFG="version",{cfg.connect_id},{cfg.mqtt_version}')
            if cfg.use_ssl:
                self.at.send_at(
                    f'AT+QMTCFG="ssl",{cfg.connect_id},1,{cfg.ssl_context_id},{cfg.ssl_connect_id}'
                )
        except BC660KError:
            # Some firmware variants may reject optional configs; keep flow running.
            if cfg.use_ssl:
                raise

    def _configure_mqtt_ssl(self, cfg: MQTTConfig) -> None:
        """Configure SSL context for MQTT as described in Quectel SSL app note."""
        self.at.send_at(
            f'AT+QSSLCFG={cfg.ssl_context_id},{cfg.ssl_connect_id},"seclevel",{cfg.ssl_seclevel}'
        )
        self.at.send_at(
            f'AT+QSSLCFG={cfg.ssl_context_id},{cfg.ssl_connect_id},"sslversion",{cfg.ssl_version}'
        )
        self.at.send_at(
            f'AT+QSSLCFG={cfg.ssl_context_id},{cfg.ssl_connect_id},"dataformat",0,0'
        )
        self.at.send_at(
            f'AT+QSSLCFG={cfg.ssl_context_id},{cfg.ssl_connect_id},"timeout",{cfg.ssl_timeout}'
        )
        self.at.send_at(
            f'AT+QSSLCFG={cfg.ssl_context_id},{cfg.ssl_connect_id},"debug",{cfg.ssl_debug_level}'
        )

    def mqtt_close(self, connect_id: int = 0) -> None:
        for cmd in (f"AT+QMTDISC={connect_id}", f"AT+QMTCLOSE={connect_id}"):
            try:
                self.at.send_at(cmd, timeout_s=10.0)
            except BC660KError:
                pass

    def http_get(self, url: str, cfg: HTTPConfig, rsptime: int = 80, read_length: int = 1024) -> str:
        """Execute HTTP(S) GET using QHTTP* commands and return response body text."""
        self.at.send_at(f'AT+QHTTPCFG="contextid",{cfg.context_id}')
        self.at.send_at(f'AT+QHTTPCFG="requestheader",{cfg.request_header}')
        self.at.send_at(f'AT+QHTTPCFG="responseheader",{cfg.response_header}')
        self.at.send_at(f'AT+QHTTPCFG="readformat",{cfg.read_format}')
        if url.startswith("https://"):
            self.at.send_at(
                f'AT+QHTTPCFG="ssl",{cfg.ssl_context_id},{cfg.ssl_connect_id}'
            )

        self.at.ser.write((f"AT+QHTTPURL={len(url)},60\r").encode("ascii"))
        self.at.ser.flush()
        self.at.wait_prompt(timeout_s=8.0)
        self.at.write_data(url, end_with_ctrl_z=False)
        self.at.wait_urc(r"^OK$", timeout_s=10.0)

        self.at.send_at(f"AT+QHTTPGET={rsptime},60", timeout_s=8.0)
        get_line = self.at.wait_urc(r"^\+QHTTPGET:\s*\d+,\d+", timeout_s=max(30.0, float(rsptime)))
        get_match = re.search(r"\+QHTTPGET:\s*(\d+),(\d+)", get_line)
        if not get_match or int(get_match.group(1)) != 0:
            raise BC660KError(f"QHTTPGET falhou: {get_line}")

        body_chunks: list[str] = []
        for _ in range(20):
            lines = self.at.send_at(f"AT+QHTTPREAD={read_length}", timeout_s=20.0)
            body_chunks.extend(lines)
            header = next((l for l in lines if l.startswith("+QHTTPREAD:")), "")
            if header:
                m = re.search(r"\+QHTTPREAD:\s*\d+,(\d+)", header)
                if m and int(m.group(1)) == 0:
                    break

        return "\n".join(body_chunks)
