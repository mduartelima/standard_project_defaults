# <Nome do Projeto>

<Uma frase descrevendo o que o projeto faz e para quem.>

## Visão geral

| Camada | Pasta | Stack |
|---|---|---|
| Backend | `src/backend/` | <ex.: Python/FastAPI> |
| Frontend | `src/frontend/` | <ex.: TypeScript/React> |
| Firmware | `src/firmware/` | <ex.: C/ESP-IDF, Zephyr> |
| Hardware | `src/hardware/` | <ex.: KiCad> |
| RAG local | `rag/` | Python + SQLite FTS5 |

## Início rápido

```bash
git config core.hooksPath .githooks   # ativa validação de commits
git config commit.template .gitmessage
python rag/ingest.py                  # indexa docs, memória e código
python rag/query.py "como funciona X?"
```

## Estrutura

```
CLAUDE.md / AGENTS.md   regras para agentes de IA
history.md              histórico impessoal de ações
.ai/memory/             contexto vivo, decisões, glossário
.ai/chats/              resumos de sessões
.ai/analyses/           levantamentos e análises técnicas
.ai/results/            resultados de testes, benchmarks, medições
.ai/prompts/            biblioteca de prompts reutilizáveis
docs/                   arquitetura, RAG, commits, engenharia
rag/                    indexação e busca local
src/                    código-fonte por camada
```

## Documentação

- [Arquitetura](docs/architecture.md)
- [Arquitetura RAG](docs/rag-architecture.md)
- [Convenção de commits](docs/commit-convention.md)
- [Diretrizes de engenharia](docs/engineering-guidelines.md)
- [Histórico](history.md)
