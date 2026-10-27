# API REST (frontend ↔ backend)

> Especificação do contrato HTTP. Se houver OpenAPI, apontar para o arquivo e manter este documento como resumo.

## Base

| Item | Valor |
|---|---|
| Especificação | <caminho do OpenAPI ou "somente este documento"> |
| Versionamento | <ex.: prefixo `/v1`> |
| Autenticação | <esquema> |
| Formato de erro | <estrutura padrão> |

## Endpoints

| Método | Caminho | Descrição | Request | Response |
|---|---|---|---|---|
| <GET> | <`/v1/recurso`> | <descrição> | <schema> | <schema> |

## Regras de evolução

- Mudança incompatível exige nova versão e entrada em `.ai/memory/decisions.md`.
- Campos novos são opcionais; campos existentes não mudam de significado.
