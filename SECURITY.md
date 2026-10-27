# Política de Segurança

## Reporte de vulnerabilidades

Não abrir issue pública para vulnerabilidades. Reportar para: <contato de segurança>.

Informar: componente afetado (backend, frontend, firmware, hardware), versão ou commit, passos de reprodução e impacto estimado.

| Etapa | Prazo alvo |
|---|---|
| Confirmação de recebimento | <ex.: 3 dias úteis> |
| Avaliação inicial | <ex.: 10 dias úteis> |

## Versões suportadas

| Versão | Suporte |
|---|---|
| <versão> | <sim/não> |

## Diretrizes

- Segredos nunca entram no repositório; usar `.env` (fora do git) e `.env.example` sem valores.
- Firmware com atualização remota segue `docs/ota-policy.md` (imagens assinadas, rollback, rotação de chaves).
- Referência para dispositivos IoT de consumo: ETSI EN 303 645.
