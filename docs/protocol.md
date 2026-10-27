# Protocolo de telemetria (firmware ↔ backend)

> Contrato entre dispositivo e servidor. Alterações exigem entrada em `.ai/memory/decisions.md`.

## Transporte

| Item | Valor |
|---|---|
| Protocolo | <MQTT | HTTP | BLE | outro> |
| Codificação | <JSON | Protobuf | CBOR | outro> |
| Versão do contrato | <MAJOR.MINOR> |

## Mensagens

| Nome | Sentido | Tópico/rota | Frequência | Schema |
|---|---|---|---|---|
| <telemetria> | dispositivo → backend | <tópico> | <período> | <campos e tipos> |

## Regras de evolução

- Evolução **aditiva**: acrescentar campos; nunca alterar o significado de um campo existente.
- Em Protobuf, números de campo removidos ficam reservados (`reserved`).
- Quebra de compatibilidade incrementa o MAJOR do contrato e exige plano de migração para dispositivos em campo.
- O backend aceita ao menos a versão MAJOR anterior enquanto houver dispositivos nela.
- Checagem de compatibilidade entre versões no CI: <ferramenta a definir>.
