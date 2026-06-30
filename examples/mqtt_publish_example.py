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
        broker="test.mosquitto.org",
        broker_port=1883,
        client_id="bc660k-example",
        topic="bc660k/example",
        message="hello from bc660k-lib",
        qos=0,
        retain=0,
    )

    with BC660KClient(serial_cfg) as modem:
        modem.initialize(disable_sleep=True)
        modem.configure_network(network_cfg)
        modem.mqtt_publish(mqtt_cfg)


if __name__ == "__main__":
    main()
