# Arquitetura do Sistema

> Preencher conforme o projeto evolui. Manter diagrama e interfaces atualizados: este documento é a referência principal recuperada pelo RAG para perguntas de arquitetura.

## Diagrama de blocos

```
┌────────────┐   HTTPS/WebSocket   ┌────────────┐   MQTT/HTTP/BLE   ┌────────────┐
│  Frontend  │ ◄─────────────────► │  Backend   │ ◄───────────────► │  Firmware  │
│ (web/app)  │                     │ (API, DB)  │                   │   (MCU)    │
└────────────┘                     └────────────┘                   └─────┬──────┘
                                                                         │ GPIO/I2C/SPI/UART
                                                                   ┌─────▼──────┐
                                                                   │  Hardware  │
                                                                   └────────────┘
```

## Componentes

### Backend — `src/backend/`
Responsabilidades, stack, persistência, autenticação.

### Frontend — `src/frontend/`
Responsabilidades, stack, estado, comunicação com o backend.

### Firmware — `src/firmware/`
Alvo, RTOS/framework, tarefas e prioridades, mapa de memória, bootloader/OTA.

### Hardware — `src/hardware/`
Placa, revisão, MCU, periféricos, alimentação, conectores. Pinout em `src/hardware/pinout.md`.

## Interfaces e contratos

| Interface | Entre | Protocolo | Especificação |
|---|---|---|---|
| API REST | frontend ↔ backend | HTTP/JSON | `docs/api.md` ou OpenAPI |
| Telemetria | firmware ↔ backend | <MQTT> | `docs/protocol.md` |

Contratos versionados; qualquer alteração exige entrada em `decisions.md`.
