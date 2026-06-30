from bc660k import BC660KClient, MQTTConfig, NetworkConfig, SerialConfig


def main() -> None:
    serial_cfg = SerialConfig(port="COM22", baud=115200)
    network_cfg = NetworkConfig(
        apn="your.apn",
        apn_user="your-apn-user",
        apn_pass="your-apn-pass",
        cid=0,
    )
    mqtt_cfg = MQTTConfig(
        broker="your-broker-host",
        broker_port=8883,
        client_id="bc660k-tls-example",
        topic="bc660k/tls/example",
        message="hello from bc660k-lib tls",
        qos=0,
        retain=0,
        use_ssl=True,
        ssl_context_id=0,
        ssl_connect_id=0,
        ssl_seclevel=0,
        ssl_version=4,
        ssl_timeout=90,
        ssl_debug_level=0,
    )

    with BC660KClient(serial_cfg) as modem:
        modem.initialize(disable_sleep=True)
        modem.configure_network(network_cfg)
        modem.mqtt_publish(mqtt_cfg)


if __name__ == "__main__":
    main()
