"""Command-line entry points for bc660k."""

from __future__ import annotations

import argparse
import sys

from .client import BC660KClient
from .exceptions import BC660KError
from .models import MQTTConfig, NetworkConfig, SerialConfig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Publicador MQTT via BC660K-GL")
    parser.add_argument("--port", default="COM22", help="Porta serial")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate")

    parser.add_argument("--apn", default="your.apn", help="APN")
    parser.add_argument("--apn-user", default="", help="Usuario APN")
    parser.add_argument("--apn-pass", default="", help="Senha APN")
    parser.add_argument("--cid", type=int, default=0, help="CID do contexto PDP")
    parser.add_argument("--operator", default="", help="Operadora MCCMNC")
    parser.add_argument("--nbiot-only", action="store_true", help="Tenta forcar NB-IoT")
    parser.add_argument("--roaming", action="store_true", help="Tenta habilitar roaming")
    parser.add_argument("--attach-retries", type=int, default=3, help="Tentativas de attach")

    parser.add_argument("--broker", required=True, help="Broker MQTT")
    parser.add_argument("--broker-port", type=int, default=1883, help="Porta do broker")
    parser.add_argument("--client-id", default="bc660k-client", help="Client ID")
    parser.add_argument("--username", default="", help="Usuario MQTT")
    parser.add_argument("--password", default="", help="Senha MQTT")
    parser.add_argument("--mqtt-version", type=int, choices=[0, 1], default=1, help="0=3.1, 1=3.1.1")
    parser.add_argument("--clean-session", type=int, choices=[0, 1], default=1, help="Clean session")
    parser.add_argument("--keepalive", type=int, default=60, help="Keepalive")
    parser.add_argument("--qos", type=int, choices=[0, 1, 2], default=0, help="QoS")
    parser.add_argument("--retain", type=int, choices=[0, 1], default=0, help="Retain")
    parser.add_argument("--ssl", action="store_true", help="Habilita MQTT sobre TLS")
    parser.add_argument("--ssl-context-id", type=int, default=0, help="SSL context ID")
    parser.add_argument("--ssl-connect-id", type=int, default=0, help="SSL connect ID")
    parser.add_argument("--ssl-seclevel", type=int, choices=[0, 1, 2], default=0, help="QSSLCFG seclevel")
    parser.add_argument("--ssl-version", type=int, choices=[1, 2, 3, 4], default=4, help="QSSLCFG sslversion")
    parser.add_argument("--ssl-timeout", type=int, default=90, help="QSSLCFG timeout")
    parser.add_argument("--ssl-debug-level", type=int, choices=[0, 1, 2, 3, 4], default=0, help="QSSLCFG debug")

    parser.add_argument("--topic", required=True, help="Topico")
    parser.add_argument("--message", required=True, help="Mensagem")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    serial_cfg = SerialConfig(port=args.port, baud=args.baud)
    network_cfg = NetworkConfig(
        apn=args.apn,
        apn_user=args.apn_user,
        apn_pass=args.apn_pass,
        cid=args.cid,
        operator=args.operator,
        nbiot_only=args.nbiot_only,
        roaming=args.roaming,
        attach_retries=args.attach_retries,
    )
    mqtt_cfg = MQTTConfig(
        broker=args.broker,
        broker_port=args.broker_port,
        client_id=args.client_id,
        username=args.username,
        password=args.password,
        mqtt_version=args.mqtt_version,
        clean_session=args.clean_session,
        keepalive=args.keepalive,
        qos=args.qos,
        retain=args.retain,
        topic=args.topic,
        message=args.message,
        use_ssl=args.ssl,
        ssl_context_id=args.ssl_context_id,
        ssl_connect_id=args.ssl_connect_id,
        ssl_seclevel=args.ssl_seclevel,
        ssl_version=args.ssl_version,
        ssl_timeout=args.ssl_timeout,
        ssl_debug_level=args.ssl_debug_level,
    )

    try:
        with BC660KClient(serial_cfg) as client:
            print("[1/4] Inicializando modem...")
            client.initialize(disable_sleep=True)
            print("[2/4] Configurando rede...")
            client.configure_network(network_cfg)
            print("[3/4] Publicando MQTT...")
            client.mqtt_publish(mqtt_cfg)
            print("[4/4] Concluido.")
        return 0
    except BC660KError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
