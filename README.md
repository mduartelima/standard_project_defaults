# <Nome do Projeto>

<Uma frase descrevendo o que o projeto faz e para quem.>

## Visão geral

| Camada | Pasta | Stack |
|---|---|---|
| Backend | `src/backend/` | <ex.: Python/FastAPI> |
| Frontend | `src/frontend/` | <ex.: TypeScript/React> |
| Firmware | `src/firmware/` | <ex.: C/ESP-IDF, Zephyr> |
| Hardware | `src/hardware/` | <ex.: KiCad> |
| Protocolo | `src/protocol/` | <ex.: Protobuf> |
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
tests/                  testes por camada
.github/workflows/      CI por camada
```

## Documentação

- [Arquitetura](docs/architecture.md)
- [Arquitetura RAG](docs/rag-architecture.md)
- [Convenção de commits](docs/commit-convention.md)
- [Diretrizes de engenharia](docs/engineering-guidelines.md)
- [API](docs/api.md) e [protocolo](docs/protocol.md)
- [Política de OTA](docs/ota-policy.md)
- [Release de hardware](docs/hardware-release.md)
- [Testes](tests/README.md)
- [Contribuindo](CONTRIBUTING.md) e [segurança](SECURITY.md)
- [Histórico](history.md)

## Licença

Este template é distribuído sob a licença MIT (`LICENSE`). Ao iniciar um projeto a partir dele, **substituir ou remover o `LICENSE`** e ajustar o titular do copyright: a licença do template não se aplica ao código do projeto derivado.

## Autor

Marcelo Duarte Lima — [@mduartelima](https://github.com/mduartelima) — [LinkedIn](https://www.linkedin.com/in/marcelodtlima)
