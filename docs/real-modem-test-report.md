# Real Modem Test Report

Date: 2026-06-30

## Device And Network Conditions

- Module: Quectel BC660K-GL
- Firmware: BC660KGLAAR01A05
- Serial: COM22 @ 115200
- Operator (MCCMNC): registered (masked value)
- Registration: +CEREG: 5,5,... (registered roaming)
- PS attach: +CGATT: 1
- PDP IP (CID 0): dynamically assigned (value not published)
- APN: private APN (value not published)
- RF snapshot: +CSQ: 30,0 and +CESQ: 99,99,255,255,26,81

## Executed Real Tests

1. HTTP via library
- Flow: initialize -> configure_network -> http_get
- Target: http://example.com/
- Result: success, HTTP 200 returned in payload

2. MQTT (non TLS) via wrapper/library
- Command target: br1.data.fichar.io:1883
- Topic: private topic (masked)
- Result: success ([1/4] .. [4/4] completed)

3. MQTTS (TLS) via wrapper/library
- Command target: test.mosquitto.org:8883
- Topic: bc660k/real/tls
- TLS mode: --ssl --ssl-seclevel 0 --ssl-version 4
- Result: success ([1/4] .. [4/4] completed)

## Notes

- seclevel=0 validates TLS connectivity only (no certificate validation).
- For production, use seclevel=1 or 2 and provision CA/client certs with QSSLCFG.
