# Histórico do Projeto

Registro impessoal e cronológico (mais recente no topo) das ações realizadas.
Cada entrada descreve fatos verificáveis; opiniões e planos ficam em `.ai/memory/context.md`.

<!--
MODELO DE ENTRADA — copiar para o topo da lista

## AAAA-MM-DD — <título curto>

**Tipo:** análise | implementação | correção | refatoração | documentação | infraestrutura
**Escopo:** backend | frontend | firmware | hardware | rag | docs | geral

**Contexto:** motivo da ação (problema, requisito, issue).

**Ações realizadas:**
- Ação objetiva 1.
- Ação objetiva 2.

**Resultado:** estado final, métricas, testes executados.

**Arquivos afetados:** `caminho/a.c`, `caminho/b.md`

**Pendências:** itens em aberto (ou "Nenhuma").

**Commit:** `<hash curto>` — `<mensagem>`
-->

## 2026-10-27 — Regra de Co-Authored-By sob solicitação por commit

**Tipo:** documentação
**Escopo:** geral

**Contexto:** A proibição absoluta de `Co-Authored-By` impedia a atribuição deliberada. A regra passou a proibir apenas o uso automático.

**Ações realizadas:**
- Registrada a decisão D-003 em `.ai/memory/decisions.md`.
- Atualizada a regra em `CLAUDE.md` (raiz e template), `docs/commit-convention.md` e `.gitmessage`.
- Alterado `.githooks/commit-msg` para aceitar o trailer somente com `ALLOW_COAUTHOR=1` no ambiente do commit.

**Resultado:** Hook executado em Git Bash com três mensagens: trailer sem variável rejeitado (saída 1), trailer com `ALLOW_COAUTHOR=1` aceito (saída 0) e mensagem sem trailer aceita (saída 0). O diretório não é repositório git, então o hook não foi exercitado por um `git commit` real.

**Arquivos afetados:** `CLAUDE.md`, `ai-project-template/CLAUDE.md`, `ai-project-template/.githooks/commit-msg`, `ai-project-template/docs/commit-convention.md`, `ai-project-template/.gitmessage`, `ai-project-template/.ai/memory/decisions.md`

**Pendências:** Passos 2 a 8 do plano de revisão (inconsistências, governança, READMEs por camada, contratos, hardware, CI, testes). Conferir a chave de atribuição de `.claude/settings.json` na documentação atual.

**Commit:** Não realizado (diretório fora de repositório git).

## 2026-10-27 — Estruturação inicial do projeto

**Tipo:** infraestrutura
**Escopo:** geral

**Contexto:** Necessidade de padronizar o uso de agentes de IA, manter memória local versionada e estabelecer convenções de documentação e commit.

**Ações realizadas:**
- Criada estrutura `.ai/` para memória, chats, análises, resultados e prompts.
- Definidas regras do agente em `CLAUDE.md` e ponteiro em `AGENTS.md`.
- Implementado RAG local com SQLite FTS5 (`rag/ingest.py`, `rag/query.py`).
- Definida convenção de commits e hook de validação `.githooks/commit-msg`.

**Resultado:** Template funcional; indexação e busca validadas localmente.

**Arquivos afetados:** estrutura completa do repositório.

**Pendências:** Preencher `README.md` e `docs/architecture.md` com dados do projeto.

**Commit:** `chore: estrutura inicial do projeto com memória local e rag`
