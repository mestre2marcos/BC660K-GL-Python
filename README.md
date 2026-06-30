# BC660K Python Library

Biblioteca Python para o modem Quectel BC660K-GL, com foco em:
- setup inicial do modem;
- configuracao de rede (APN, attach e PDP);
- operacoes HTTP(S) via QHTTP*;
- operacoes MQTT via QMT*.

## Aviso de IA

Este projeto foi criado com ajuda de IA (GitHub Copilot/GPT-5.3-Codex) e validado com testes práticos no modem.

## Estrutura

- src/bc660k/transport.py: camada de transporte AT (serial, prompt, URC, wake)
- src/bc660k/client.py: cliente de alto nivel (setup, rede, HTTP, MQTT)
- src/bc660k/models.py: dataclasses de configuracao
- src/bc660k/exceptions.py: excecoes da biblioteca
- src/bc660k/cli.py: CLI para publish MQTT
- docs/application-notes/: AT manual e application notes oficiais

## Instalacao

Opcao 1: ambiente local

```powershell
pip install -e .
```

Opcao 2: dependencia direta (sem instalar pacote)

```powershell
pip install pyserial
```

## Uso rapido (MQTT)

```powershell
bc660k-mqtt --broker your-broker-host --broker-port 1883 --username your-user --password your-password --topic your/topic --message "test message" --client-id bc660k-client
```

## Uso rapido (MQTT com TLS/8883)

```powershell
bc660k-mqtt --broker seu-broker --broker-port 8883 --ssl --ssl-seclevel 1 --ssl-version 4 --topic seu/topico --message "teste tls" --client-id bc660k-tls
```

Notas:
- Para autenticacao de servidor (CA), use `--ssl-seclevel 1` e configure certificado CA via QSSLCFG no modem.
- Para TLS sem validacao de certificado (somente laboratorio), use `--ssl-seclevel 0`.

## Uso via API

```python
from bc660k import BC660KClient, SerialConfig, NetworkConfig, MQTTConfig

serial_cfg = SerialConfig(port="COM22", baud=115200)
network_cfg = NetworkConfig(
    apn="your.apn",
    apn_user="your-apn-user",
    apn_pass="your-apn-pass",
    cid=0,
)
mqtt_cfg = MQTTConfig(
    broker="your-broker-host",
    broker_port=1883,
    username="your-user",
    password="your-password",
    topic="your/topic",
    message="hello",
)

with BC660KClient(serial_cfg) as modem:
    modem.initialize(disable_sleep=True)
    modem.configure_network(network_cfg)
    modem.mqtt_publish(mqtt_cfg)
```

## HTTP(S) via API

```python
from bc660k import BC660KClient, SerialConfig, NetworkConfig, HTTPConfig

with BC660KClient(SerialConfig(port="COM22", baud=115200)) as modem:
    modem.initialize(disable_sleep=True)
    modem.configure_network(NetworkConfig())
    payload = modem.http_get(
        url="http://example.com/",
        cfg=HTTPConfig(context_id=0, response_header=1),
        rsptime=80,
    )
    print(payload)
```

## Observacoes

- Para MQTT SSL/TLS (porta 8883), a configuracao QSSLCFG deve estar alinhada com o broker e certificados.
- O fluxo da biblioteca aplica QSSLCFG (seclevel/sslversion/dataformat/timeout/debug) e depois QMTCFG "ssl" antes do QMTOPEN.
- O firmware pode variar no suporte de comandos opcionais (por exemplo, QCFG ou QIACT).
- Este codigo tenta caminhos de fallback para manter robustez em firmware heterogeneo.

## Validacao Em Modem Real

Esta biblioteca foi testada com modem real BC660K-GL em 2026-06-30.

Condicoes de teste coletadas no equipamento:
- Modulo: Quectel BC660K-GL
- Firmware: BC660KGLAAR01A05
- Porta serial: COM22 @ 115200
- Operadora (MCCMNC): registrado (valor mascarado)
- Registro de rede: +CEREG stat=5 (registrado em roaming)
- PS attach: +CGATT: 1
- IP PDP (CID 0): atribuido dinamicamente (valor nao publicado)
- APN: APN privada (valor nao publicado)
- Sinal no momento: +CSQ 30,0 e +CESQ 99,99,255,255,26,81

Cenarios executados com sucesso:
- HTTP real via biblioteca: GET em http://example.com/ com resposta HTTP 200
- MQTT real (sem TLS): publish para br1.data.fichar.io:1883
- MQTTS real (com TLS): publish para test.mosquitto.org:8883 com SSL habilitado

Importante para TLS:
- O teste MQTTS acima foi feito com seclevel=0 (sem validacao de certificado), adequado para validacao de conectividade.
- Para producao, use seclevel=1/2 e configure certificados CA/cliente conforme a nota SSL (AT+QSSLCFG).

Relatorio detalhado:
- docs/real-modem-test-report.md

Documentacao de referencia (Quectel):
- docs/application-notes/BC660k-AT-manual.md
- docs/application-notes/bc660k-HTTPS-application-note.md
- docs/application-notes/bc660k-MQTT-application-note.md
- docs/application-notes/bc660k-SSL-applications-note.md
