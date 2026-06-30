from bc660k import BC660KClient, HTTPConfig, NetworkConfig, SerialConfig


def main() -> None:
    serial_cfg = SerialConfig(port="COM22", baud=115200)
    network_cfg = NetworkConfig(
        apn="your.apn",
        apn_user="your-apn-user",
        apn_pass="your-apn-pass",
        cid=0,
    )

    with BC660KClient(serial_cfg) as modem:
        modem.initialize(disable_sleep=True)
        modem.configure_network(network_cfg)
        body = modem.http_get("http://example.com/", HTTPConfig(context_id=0, response_header=1))
        print(body)


if __name__ == "__main__":
    main()
