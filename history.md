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

## 2026-10-27 — Correções do RAG, arquivos ausentes e governança do template

**Tipo:** correção
**Escopo:** geral

**Contexto:** Análise do projeto apontou bugs no RAG, referências a arquivos inexistentes, ausência de governança, de READMEs úteis por camada e de CI. Primeiro commit do repositório (sem commits anteriores).

**Ações realizadas:**
- Corrigido o filtro `--kind` (aplicado no SQL, antes do `LIMIT`), `search()` passou a lançar `IndexNotFound` e `eval.py` deixou de dividir por zero. Testes de regressão em `tests/rag/`, que falham no código anterior.
- RAG passou a indexar `.csv`, `.conf`, `sdkconfig` e `sdkconfig.defaults`; peso de `datasheet` elevado para 1.3.
- Criados `docs/api.md`, `docs/protocol.md`, `docs/datasheets/` e `.env.example`.
- Criados `.gitattributes` (LF em hooks e scripts) e `.editorconfig`; `.gitignore` deixou de ignorar `*.bin` e `*.hex`.
- Criados `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`, `CHANGELOG.md`, `docs/ota-policy.md`, `docs/hardware-release.md`, modelos de README por camada, `tests/README.md` e checklist HIL.
- Criados workflows `rag.yml` (ativo) e `backend`, `frontend`, `firmware`, `hil` (somente disparo manual); `.tool-versions` como modelo.
- Hook `commit-msg` exercitado com 14 mensagens (formato, maiúscula, ponto final, comprimento, trailer com e sem `ALLOW_COAUTHOR=1`, assinatura de geração, merge) e em commits reais; comportamento conforme o esperado.

**Resultado:** 5 testes unitários do RAG passando; `rag/eval.py` com 3/3 (100%) em `hit rate@5`; nenhum caminho citado em Markdown inexistente, exceto `rag/index.db` (gerado). Sintaxe dos workflows YAML não validada por parser (sem PyYAML local) nem executada no GitHub.

**Correção factual:** a entrada anterior cita caminhos com prefixo `ai-project-template/` e afirma que o diretório não era repositório git; esses fatos valiam para a pasta de origem. O repositório atual tem a raiz em `standard_project_defaults/`.

**Arquivos afetados:** `rag/*`, `tests/*`, `docs/*`, `src/*/README.md`, `.github/workflows/*`, `.gitignore`, `.gitattributes`, `.editorconfig`, `.tool-versions`, `.env.example`, `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`, `CHANGELOG.md`

**Pendências:** Reforçar `.claude/settings.json` (negar `git push -f`, `git reset --hard`, leitura de `.env`; liberar `eval.py`), bloqueado por permissão e a aplicar manualmente. Conferir a chave `includeCoAuthoredBy` na documentação atual. `LICENSE` depende de escolha do responsável. Indexação de `.kicad_*` não implementada. `CLAUDE.md` e `ai-project-template-APAGAR/` fora do repositório, na pasta pai. Preencher placeholders de `context.md` e `README.md`.

**Commit:** `cb4ccfa` a `bdcb3f3` — `chore: adiciona estrutura inicial do template` e demais commits da sessão

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
