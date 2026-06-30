from bc660k.models import HTTPConfig, MQTTConfig, NetworkConfig, SerialConfig


def test_serial_config_defaults() -> None:
    cfg = SerialConfig()
    assert cfg.port == "COM22"
    assert cfg.baud == 115200
    assert cfg.timeout == 0.25


def test_network_config_defaults() -> None:
    cfg = NetworkConfig()
    assert cfg.apn == "your.apn"
    assert cfg.cid == 0
    assert cfg.attach_retries == 3


def test_mqtt_config_tls_defaults() -> None:
    cfg = MQTTConfig()
    assert cfg.use_ssl is False
    assert cfg.ssl_context_id == 0
    assert cfg.ssl_connect_id == 0
    assert cfg.ssl_seclevel == 0
    assert cfg.ssl_version == 4


def test_http_config_defaults() -> None:
    cfg = HTTPConfig()
    assert cfg.context_id == 0
    assert cfg.response_header == 1
