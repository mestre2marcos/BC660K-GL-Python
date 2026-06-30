"""Data models used to configure BC660K workflows."""

from dataclasses import dataclass


@dataclass
class SerialConfig:
    port: str = "COM22"
    baud: int = 115200
    timeout: float = 0.25


@dataclass
class NetworkConfig:
    apn: str = "your.apn"
    apn_user: str = ""
    apn_pass: str = ""
    cid: int = 0
    operator: str = ""
    nbiot_only: bool = False
    roaming: bool = False
    attach_retries: int = 3


@dataclass
class MQTTConfig:
    broker: str = "test.mosquitto.org"
    broker_port: int = 1883
    topic: str = "bc660k/test"
    message: str = "hello from bc660k"
    client_id: str = "bc660k-client"
    username: str = ""
    password: str = ""
    keepalive: int = 60
    mqtt_version: int = 1
    clean_session: int = 1
    qos: int = 0
    retain: int = 0
    connect_id: int = 0
    use_ssl: bool = False
    ssl_context_id: int = 0
    ssl_connect_id: int = 0
    ssl_seclevel: int = 0
    ssl_version: int = 4
    ssl_timeout: int = 90
    ssl_debug_level: int = 0


@dataclass
class HTTPConfig:
    context_id: int = 0
    ssl_context_id: int = 0
    ssl_connect_id: int = 0
    response_header: int = 1
    request_header: int = 0
    read_format: int = 0
