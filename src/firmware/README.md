# src/firmware — Firmware

> Modelo a preencher. Contexto geral: `docs/architecture.md`; regras: `docs/engineering-guidelines.md`.

## Stack

| Item | Valor |
|---|---|
| Alvo (MCU), RTOS/framework e toolchain (versão fixada) | <valor> |

## Build e execução

```bash
<comando de build>
<comando de execução>
```

## Testes

```bash
<comando de teste>
```

Convenção em `tests/README.md`.

## Estrutura

```
<pastas principais e responsabilidade de cada uma>
```

## Divisão opcional

Padrão a adotar quando o projeto precisar; não criar pastas vazias de antemão.

| Pasta | Conteúdo |
|---|---|
| `bootloader/` | configuração do bootloader, tabela de partições, referência às chaves públicas |
| `targets/<alvo>/` | uma aplicação por alvo, quando houver mais de um (bare-metal, RTOS, Linux embarcado) |
| `ota-tools/` | scripts de assinatura e empacotamento de imagens; **sem chaves privadas** (ver `SECURITY.md`) |
| `shared/` | drivers e bibliotecas usados por mais de um alvo |

Política de atualização remota: `docs/ota-policy.md`.

## Dependências e interfaces

- Depende de: <camadas, serviços, bibliotecas>
- Contrato: <`docs/api.md` | `docs/protocol.md` | `src/hardware/pinout.md`>
