# Hardware-in-the-loop (HIL)

> Checklist da bancada. Workflow de CI correspondente: `.github/workflows/hil.yml` (desativado por padrão).

## Bancada

| Item | Valor |
|---|---|
| Runner self-hosted | <host> |
| Label de roteamento | <ex.: `has_<placa>`> |
| Dispositivos e mapa (serial, programador) | <preencher> |
| Fixture serial | <porta, baud> |

## Critério de aprovação

O job só é aprovado se **build, flash, boot, estímulo e asserções** passaram. Abrir a porta serial não conta como teste.

## Pré-requisito

Testes de host passando antes de usar a bancada.
