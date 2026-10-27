# src/protocol — Schemas do protocolo

> Fonte única, legível por máquina, do contrato firmware ↔ backend. Descrição e regras de evolução: `docs/protocol.md`.

## Formato

| Item | Valor |
|---|---|
| Linguagem de schema | <Protobuf | JSON Schema | CBOR/CDDL | outro> |
| Geração de código | <alvos: firmware, backend, frontend> |
| Comando de geração | <comando> |

## Estrutura

```
<arquivos de schema, um por mensagem ou domínio>
```

## Regras

- Os schemas daqui são a referência; código de serialização é gerado, não escrito à mão em duplicidade.
- Evolução aditiva e versão do contrato conforme `docs/protocol.md`.
- Mudança incompatível exige entrada em `.ai/memory/decisions.md`.
