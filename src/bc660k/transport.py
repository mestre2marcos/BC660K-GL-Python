"""Low-level AT transport helpers for BC660K serial communication."""

from __future__ import annotations

import re
import time
from typing import Pattern

import serial

from .exceptions import ATCommandError, ModemTimeoutError


class ATTransport:
    """Line-oriented AT transport with robust wake/retry behavior."""

    def __init__(self, port: str, baud: int, timeout: float = 0.25) -> None:
        self.ser = serial.Serial(port=port, baudrate=baud, timeout=timeout, write_timeout=2)

    def close(self) -> None:
        if self.ser and self.ser.is_open:
            self.ser.close()

    def flush_input(self) -> None:
        self.ser.reset_input_buffer()

    def readline(self) -> str:
        data = self.ser.readline()
        if not data:
            return ""
        return data.decode("utf-8", errors="ignore").strip()

    def send_at_once(self, cmd: str, timeout_s: float = 8.0) -> list[str]:
        self.ser.write((cmd + "\r").encode("ascii"))
        self.ser.flush()

        lines: list[str] = []
        deadline = time.time() + timeout_s

        while time.time() < deadline:
            line = self.readline()
            if not line:
                continue
            if line == cmd:
                continue

            lines.append(line)
            if line == "OK":
                return lines
            if line == "ERROR" or line.startswith("+CME ERROR"):
                raise ATCommandError(f"Falha em '{cmd}': {line}")

        raise ModemTimeoutError(f"Timeout aguardando resposta de '{cmd}'")

    def send_at(self, cmd: str, timeout_s: float = 8.0) -> list[str]:
        """Send command and retry once after wake-up attempt when appropriate."""
        try:
            return self.send_at_once(cmd, timeout_s=timeout_s)
        except (ATCommandError, ModemTimeoutError):
            if cmd != "AT":
                try:
                    self.send_at_once("AT", timeout_s=3.0)
                except (ATCommandError, ModemTimeoutError):
                    pass
                return self.send_at_once(cmd, timeout_s=timeout_s)
            raise

    def wait_urc(self, regex: str | Pattern[str], timeout_s: float) -> str:
        pattern = re.compile(regex) if isinstance(regex, str) else regex
        deadline = time.time() + timeout_s

        while time.time() < deadline:
            line = self.readline()
            if not line:
                continue
            if pattern.match(line):
                return line

        raise ModemTimeoutError(f"Timeout aguardando URC: {pattern.pattern}")

    def wait_prompt(self, timeout_s: float = 8.0) -> None:
        """Wait for data-mode prompt character ('>')."""
        deadline = time.time() + timeout_s
        buf = b""

        while time.time() < deadline:
            byte = self.ser.read(1)
            if not byte:
                continue

            buf += byte
            if b">" in buf:
                return

            text = buf.decode("utf-8", errors="ignore")
            if "ERROR" in text or "+CME ERROR" in text:
                raise ATCommandError(f"Erro antes do prompt: {text.strip()}")

        raise ModemTimeoutError("Timeout aguardando prompt de data mode")

    def write_data(self, data: str, end_with_ctrl_z: bool = False) -> None:
        raw = data.encode("utf-8")
        if end_with_ctrl_z:
            raw += b"\x1A"
        self.ser.write(raw)
        self.ser.flush()

    def wake_modem(self, attempts: int = 4) -> None:
        """Wake modem robustly, ignoring stale URCs until an OK appears."""
        self.flush_input()
        for _ in range(attempts):
            self.ser.write(b"AT\r")
            self.ser.flush()
            deadline = time.time() + 3.0

            while time.time() < deadline:
                line = self.readline()
                if not line or line == "AT":
                    continue
                if line == "OK":
                    return

            time.sleep(1.0)

        raise ModemTimeoutError("Nao foi possivel acordar o modem")
