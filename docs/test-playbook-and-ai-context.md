# BC660K Test Playbook and AI Context

Este documento tem dois objetivos:
- servir como passo a passo de testes em campo para o BC660K-GL;
- servir como contexto para outras IAs entenderem rapidamente o fluxo AT deste projeto.

## 1) Contexto Rapido Para IA

Projeto Python para BC660K-GL com foco em:
- registro em rede NB-IoT/LTE Cat NB;
- ativacao de PDP e validacao de conectividade IP;
- publicacao MQTT (1883 e 8883 com TLS).

Estrutura relevante:
- Biblioteca: src/bc660k
- CLI MQTT: src/bc660k/cli.py (entrypoint: bc660k-mqtt)
- Testes unitarios: tests/
- Relatorio de teste real: docs/real-modem-test-report.md
- Notes oficiais: docs/application-notes/

Fluxo funcional esperado:
1. Inicializar UART e modem (AT, ATE0, CMEE, QSCLK).
2. Confirmar SIM e registro em rede (+CEREG, +COPS).
3. Garantir attach e PDP com IP (+CGATT, +CGACT/QIACT, +CGPADDR).
4. Validar internet (HTTP GET ou abertura de socket).
5. Publicar MQTT (QMTOPEN, QMTCONN, QMTPUB).

## 2) Preparacao De Teste

Pre-requisitos:
- Modem BC660K-GL conectado via serial.
- SIM ativo com plano de dados NB-IoT.
- APN da operadora.
- Python 3.10+.
- Dependencias instaladas.

Comandos:
```powershell
pip install -e .
python -m pytest -q
```

## 3) Teste 1: Registro Na Rede

Objetivo: garantir que modulo, SIM e rede estao operacionais.

Sequencia AT recomendada:
```text
AT
ATE0
AT+CMEE=2
AT+QSCLK=0
AT+CPIN?
AT+CEREG?
AT+COPS?
AT+CSQ
AT+CESQ
```

Respostas esperadas (exemplos):
- AT -> OK
- AT+CPIN? -> +CPIN: READY
- AT+CEREG? -> +CEREG: <n>,1 ou +CEREG: <n>,5
- AT+COPS? -> operador presente
- AT+CSQ/AT+CESQ -> valores diferentes de "desconhecido"

Criterio de sucesso:
- modulo responde AT estavelmente;
- SIM pronto;
- status de registro = 1 (home) ou 5 (roaming).

## 4) Teste 2: Conexao Com Internet (PDP/IP)

Objetivo: garantir attach PS e IP valido no CID usado.

Sequencia AT recomendada:
```text
AT+CGATT?
AT+QCGDEFCONT="IP","<APN>","<APN_USER>","<APN_PASS>"
AT+CGATT=1
AT+CGACT=1,0
AT+CGPADDR=0
```

Alternativa de ativacao em alguns firmwares:
```text
AT+QIACT=0
AT+CGPADDR=0
```

Validacao de internet por HTTP:
```text
AT+QHTTPCFG="contextid",0
AT+QHTTPURL=<len>,60
<url>
AT+QHTTPGET=80,60
AT+QHTTPREAD=512
```

Criterio de sucesso:
- +CGATT: 1
- +CGPADDR com IPv4 diferente de 0.0.0.0
- QHTTPGET com resultado 0 e status HTTP 200/3xx/4xx valido (sem erro de transporte)

## 5) Teste 3: Publicacao MQTT

Objetivo: validar publish fim-a-fim.

### 5.1 Sem TLS (porta 1883)

Sequencia AT minima:
```text
AT+QMTCFG="session",0,1
AT+QMTCFG="keepalive",0,60
AT+QMTCFG="version",0,1
AT+QMTOPEN=0,"<BROKER>",1883
-- aguardar: +QMTOPEN: 0,0
AT+QMTCONN=0,"<CLIENT_ID>","<USER>","<PASS>"
-- aguardar: +QMTCONN: 0,0,0
AT+QMTPUB=0,0,0,0,"<TOPIC>"
-- aguardar prompt >, enviar payload + Ctrl+Z
-- aguardar: +QMTPUB: 0,<msgid>,0
AT+QMTDISC=0
AT+QMTCLOSE=0
```

### 5.2 Com TLS (porta 8883)

Configurar SSL antes do QMTOPEN:
```text
AT+QSSLCFG=0,0,"seclevel",<0|1|2>
AT+QSSLCFG=0,0,"sslversion",4
AT+QSSLCFG=0,0,"dataformat",0,0
AT+QSSLCFG=0,0,"timeout",90
AT+QSSLCFG=0,0,"debug",0
AT+QMTCFG="ssl",0,1,0,0
AT+QMTOPEN=0,"<BROKER>",8883
```

Notas:
- seclevel=0 valida conectividade TLS sem validacao de certificado;
- para producao, usar seclevel=1/2 e provisionar certificados conforme note SSL.

Criterio de sucesso MQTT:
- +QMTOPEN: 0,0
- +QMTCONN: 0,0,0
- +QMTPUB ... ,0

## 6) Execucao Via CLI Da Biblioteca

Sem TLS:
```powershell
bc660k-mqtt --port COM22 --baud 115200 --apn your.apn --broker your-broker --broker-port 1883 --username your-user --password your-pass --topic your/topic --message "hello"
```

Com TLS:
```powershell
bc660k-mqtt --port COM22 --baud 115200 --apn your.apn --broker your-broker --broker-port 8883 --ssl --ssl-seclevel 1 --ssl-version 4 --topic your/topic --message "hello tls"
```

## 7) Troubleshooting Rapido

Se nao registra em rede:
- verificar antena, cobertura e SIM;
- consultar +CEREG e +COPS;
- repetir AT+CGATT=1 com timeout maior.

Se sem IP:
- conferir APN/user/pass;
- testar AT+QIACT=0 e depois AT+CGPADDR=0;
- validar se CID esta correto (normalmente 0 neste projeto).

Se MQTT falhar no open/connect:
- limpar sessao antiga: AT+QMTDISC=0 e AT+QMTCLOSE=0;
- confirmar DNS/rede com teste HTTP;
- em TLS, validar QSSLCFG e politica de certificados do broker.

## 8) Checklist De Aceite

- Registro de rede: OK
- Attach e IP: OK
- HTTP: OK
- MQTT 1883: OK
- MQTTS 8883: OK
- Logs/sintese salvos em docs/real-modem-test-report.md
