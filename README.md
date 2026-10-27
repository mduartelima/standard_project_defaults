# Template de projeto com memória local para agentes de IA, RAG e padrões de engenharia

![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-blue) ![Versão](https://img.shields.io/github/v/release/mduartelima/standard_project_defaults)

Template de repositório para iniciar projetos de software, firmware e hardware com **agentes de IA** (Claude Code, Codex, Cursor, GitHub Copilot): memória local versionada no próprio projeto, busca **RAG** offline, histórico impessoal de ações e **commits no padrão Conventional Commits**, validados por hook.

## Objetivo

Fornecer, desde o primeiro commit, um conjunto único de regras, pastas e automações para que agentes de IA trabalhem com contexto persistente e produzam documentação e commits consistentes entre projetos. O template cobre backend, frontend, firmware, hardware e o protocolo entre eles, sem fixar linguagem, framework, RTOS ou ferramenta de EDA.

## Qual necessidade supre

| Problema comum | Solução no template |
|---|---|
| Agentes de IA não retêm contexto entre sessões | Memória em Markdown na pasta `.ai/`, lida no início de cada sessão |
| Decisões e análises ficam perdidas em chats externos | `.ai/chats/`, `.ai/analyses/`, `.ai/results/` e decisões em formato ADR (`decisions.md`) |
| Cada projeto documenta e commita de um jeito | `history.md` impessoal, ciclo de trabalho padrão e hook de validação de commits |
| O agente "inventa" APIs, pinos e registradores | Regra de citar a fonte, RAG sobre o próprio repositório e prompts com ancoragem |
| Contexto grande demais para caber no prompt | Busca RAG local (SQLite FTS5, BM25) que recupera só os trechos relevantes |
| Backend, frontend, firmware e hardware sem contrato comum | `src/<camada>`, `src/protocol/`, modelos de API, protocolo, OTA e release de hardware |

## Vantagens

- **Contexto auditável:** a memória do agente vive no git, com histórico, revisão e diff, e não em um serviço externo.
- **Portável entre ferramentas:** `CLAUDE.md` para Claude Code e `AGENTS.md` para Codex, Cursor, Copilot e outros agentes.
- **RAG sem infraestrutura:** apenas a biblioteca padrão do Python e o SQLite; sem servidor, sem chave de API, funciona offline.
- **Commits consistentes:** formato Conventional Commits, linguagem técnica e impessoal, `Co-Authored-By` bloqueado por padrão e commit e push sempre confirmados pelo responsável.
- **Decisões rastreáveis:** registro append-only; decisão revogada recebe o status `Substituída por D-XXX`.
- **Agnóstico de stack:** os modelos têm campos a preencher, não tecnologias impostas.
- **Pronto para CI:** workflows por camada (só o do RAG vem ativo) e checklist de HIL.

## Como funciona

Toda tarefa segue o ciclo **Analisar → Levantar → Implementar → Validar → Documentar → Commitar**, descrito em `CLAUDE.md`. O agente lê a memória no início da sessão e recupera o restante sob demanda.

| Nível | Conteúdo | Como chega ao agente |
|---|---|---|
| 0 — Regras | `CLAUDE.md`, `AGENTS.md` | Carregado automaticamente |
| 1 — Memória de trabalho | `.ai/memory/context.md`, últimas entradas de `history.md` | Lido no início da sessão |
| 2 — Memória de longo prazo | `decisions.md`, `.ai/analyses/`, `.ai/chats/`, `.ai/results/`, `docs/` | Busca RAG |
| 3 — Conhecimento técnico | Código-fonte e datasheets convertidos para texto | Busca RAG |

Detalhes da indexação, do chunking e da evolução prevista (busca híbrida com embeddings, servidor MCP) em [Arquitetura RAG](docs/rag-architecture.md). Esses dois recursos estão descritos como evolução futura e não fazem parte da versão atual.

## Como implementar em um novo projeto

1. Criar o repositório a partir do template. Pelo botão **Use this template**, o GitHub copia os arquivos sem o histórico do template, e não há nada a limpar. Para criar localmente, clonar e descartar o histórico:

   ```bash
   git clone https://github.com/mduartelima/standard_project_defaults meu-projeto
   cd meu-projeto
   rm -rf .git && git init     # PowerShell: Remove-Item -Recurse -Force .git; git init
   ```

2. Substituir o README: copiar `docs/README.project-template.md` para `README.md` e preencher os campos entre `< >`.
3. Substituir ou remover o `LICENSE` (MIT do template) e definir o titular do projeto.
4. Preencher `.ai/memory/context.md` (objetivo, fase, prioridades) e, se houver, `.ai/memory/glossary.md`.
5. Ativar os hooks de commit:

   ```bash
   git config core.hooksPath .githooks
   git config commit.template .gitmessage
   ```

6. Indexar o conhecimento do projeto: `python rag/ingest.py`.
7. Remover as camadas que não se aplicam (`src/firmware/`, `src/hardware/` etc.) e ajustar `docs/architecture.md`.

## Como utilizar no dia a dia

1. **Abrir a sessão:** o agente lê `context.md`, as últimas entradas de `history.md` e `decisions.md` (prompt `session-start`).
2. **Consultar o conhecimento do projeto:**

   ```bash
   python rag/query.py "por que a memória fica versionada no repositório" -k 2
   ```

   ```text
   [1] .ai/memory/decisions.md:15  (decision, score 18.419)
       § Registro de Decisões (ADR resumido) > D-001 — Memória de IA versionada no repositório
   ```

   Opções: `--kind decision,memory` filtra por tipo, `--prompt` gera um prompt pronto com contexto e citações, `--json` integra com outras ferramentas. `python rag/eval.py` mede o hit rate@k.
3. **Trabalhar com os prompts:** `analyze`, `implement`, `fix`, `review`, `firmware`, `document-and-commit`, `session-start` e `session-end` em `.ai/prompts/`. No Claude Code, estão disponíveis como comandos `/analyze`, `/implement` etc.
4. **Fechar o ciclo:** registrar a ação no topo de `history.md` e atualizar `context.md`; depois, commitar com a mensagem no formato `<tipo>(<escopo>): <descrição>`.
5. **Reindexar** ao fim da sessão: `python rag/ingest.py`.

## Estrutura do repositório

```text
CLAUDE.md / AGENTS.md   regras para agentes de IA
history.md              histórico impessoal de ações
.ai/memory/             contexto vivo, decisões, glossário
.ai/chats/              resumos de sessões
.ai/analyses/           levantamentos e análises técnicas
.ai/results/            resultados de testes, benchmarks, medições
.ai/prompts/            biblioteca de prompts reutilizáveis
docs/                   arquitetura, RAG, commits, engenharia, API, protocolo, OTA
rag/                    indexação e busca local (SQLite FTS5)
src/                    backend, frontend, firmware, hardware e protocol
tests/                  testes por camada
.github/workflows/      CI por camada
.githooks/              validação de mensagens de commit
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
- [Histórico](history.md) e [Changelog](CHANGELOG.md)

## Requisitos

- Python 3 (somente a biblioteca padrão, com SQLite com FTS5).
- Git. No Windows, o hook `commit-msg` é executado pelo Git Bash.
- Um agente de IA que leia `CLAUDE.md` (Claude Code) ou `AGENTS.md` (Codex, Cursor, Copilot e similares).

## English summary

AI agent project template with **local project memory**, an offline **RAG** (SQLite FTS5 and BM25, Python standard library only), an impersonal action history (`history.md`), **Conventional Commits** enforced by a git hook, and stack-agnostic layouts for backend, frontend, firmware, hardware and the protocol between them. Works with Claude Code (`CLAUDE.md`) and agents that read `AGENTS.md`. To use it, clone the template, copy `docs/README.project-template.md` over `README.md`, replace the MIT `LICENSE`, enable the hooks and run `python rag/ingest.py`.

**Keywords:** AI agent project template, Claude Code, AGENTS.md, CLAUDE.md, local memory for LLM agents, RAG, SQLite FTS5, BM25, Conventional Commits, commit-msg hook, monorepo, firmware, embedded, IoT, OTA, prompt library.

## Licença

Este template é distribuído sob a licença MIT (`LICENSE`). Ao iniciar um projeto a partir dele, **substituir ou remover o `LICENSE`** e ajustar o titular do copyright: a licença do template não se aplica ao código do projeto derivado.

## Autor

Marcelo Duarte Lima — [@mduartelima](https://github.com/mduartelima) — [LinkedIn](https://www.linkedin.com/in/marcelodtlima)
