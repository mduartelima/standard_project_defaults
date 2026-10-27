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

## 2026-10-27 — README como apresentação do template

**Tipo:** documentação
**Escopo:** docs

**Contexto:** O `README.md` era um modelo com placeholders e não descrevia o template. Necessidade de texto otimizado para busca web, com objetivo, necessidade atendida, vantagens, implementação e uso.

**Ações realizadas:**
- Movido o modelo com placeholders para `docs/README.project-template.md`.
- Reescrito o `README.md` com objetivo, tabela problema-solução, vantagens, funcionamento em camadas de memória, passos de implementação e de uso, estrutura, requisitos, resumo e palavras-chave em inglês, licença e autoria.
- Recursos futuros (busca vetorial, servidor MCP) descritos como evolução, não como funcionalidade atual.
- Acrescentados o aviso em `CONTRIBUTING.md` e o item em `CHANGELOG.md`.

**Resultado:** Varredura de caminhos citados sem ausências; sem emojis; `rag/eval.py` com hit rate@5 de 3/3; 5 testes do RAG passando. Renderização no GitHub não verificada.

**Arquivos afetados:** `README.md`, `docs/README.project-template.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `history.md`

**Pendências:** Autorização para push. Definir no GitHub a descrição e os tópicos do repositório e habilitar "Template repository" (ação manual). Conferir a renderização após o push.

**Commit:** `docs: move o modelo de readme para docs/README.project-template.md` e `docs: reescreve o readme como apresentacao do template`

## 2026-10-27 — Publicação das versões 0.1.0 e 0.1.1

**Tipo:** infraestrutura
**Escopo:** geral

**Contexto:** Publicação das versões do template no GitHub após a integração da `develop` na `main`.

**Ações realizadas:**
- Enviadas ao remoto `main` (`22b2bab`), `develop` e as tags anotadas `v0.1.0` e `v0.1.1`, sem `--force`.
- Apagadas pelo responsável as execuções de CI com falha geradas pelos workflows de YAML inválido.
- Publicadas pelo responsável as GitHub Releases `v0.1.0` e `v0.1.1`, com notas derivadas do `CHANGELOG.md` (criação manual pela interface web; `gh` ausente na máquina).

**Resultado:** `main` e `develop` em `22b2bab`, sincronizadas com o remoto. Execução do `rag.yml` no GitHub confirmada pelo responsável.

**Arquivos afetados:** `history.md`, `.ai/memory/context.md`

**Pendências:** Opcional: ampliar o `deny` de `.claude/settings.json` (`rm -fr`, `Remove-Item -Recurse`, `git push --force-with-lease`).

**Commit:** `docs(ai): registra publicacao das versoes e atualizacao do readme`

## 2026-10-27 — Versionamento 0.1.1

**Tipo:** documentação
**Escopo:** geral

**Contexto:** Preparação da versão 0.1.1 com as mudanças da incorporação seletiva de referência IoT.

**Ações realizadas:**
- `VERSION` atualizado de `0.1.0` para `0.1.1`.
- `CHANGELOG.md`: seção `[Não lançado]` convertida em `[0.1.1] - 2026-10-27`, com nova seção `[Não lançado]` vazia.

**Resultado:** Versão preparada na branch `develop`. Tag `v0.1.1` não criada.

**Arquivos afetados:** `VERSION`, `CHANGELOG.md`, `history.md`

**Pendências:** Autorização para criar a tag `v0.1.1` e para push da branch e da tag.

**Commit:** `chore: versiona o template em 0.1.1`

## 2026-10-27 — Incorporação seletiva de referência de estrutura IoT

**Tipo:** documentação
**Escopo:** geral

**Contexto:** Avaliação de um texto de referência (estrutura de monorepo IoT industrial) concluiu que adotá-lo integralmente reorganizaria o template e fixaria stack; 4 pontos foram extraídos.

**Ações realizadas:**
- Texto guardado, sem emojis, em `.ai/analyses/2026-10-27-referencia-estrutura-iot.md`, com ressalvas (afirmações não verificadas).
- `.gitignore`: `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.jks`, `*.keystore`; custódia de chaves em `SECURITY.md` e `docs/ota-policy.md`.
- Criado `src/protocol/README.md`; referências em `docs/protocol.md`, `docs/architecture.md` e `README.md`; `.proto` adicionado ao RAG.
- Criado `.github/workflows/hardware.yml` (disparo manual).
- Seção "Divisão opcional" em `src/firmware/README.md`.

**Resultado:** 6 workflows válidos no PyYAML; 5 testes do RAG passando; `probe.key` e `x.pem` ignorados pelo git; consulta sobre custódia de chave recupera `docs/ota-policy.md`. Execução do `hardware.yml` no GitHub não verificada.

**Arquivos afetados:** `.gitignore`, `SECURITY.md`, `docs/ota-policy.md`, `docs/protocol.md`, `docs/architecture.md`, `README.md`, `rag/config.json`, `src/protocol/README.md`, `src/firmware/README.md`, `.github/workflows/hardware.yml`, `CHANGELOG.md`

**Pendências:** Push da branch `develop` e integração na `main`. O texto original permanece também em `temp.txt` na pasta pai (fora do repositório).

**Commit:** `docs(ai): guarda referencia de estrutura iot` e 4 commits de aplicação

## 2026-10-27 — Versionamento 0.1.0

**Tipo:** documentação
**Escopo:** geral

**Contexto:** Pedido para versionar o projeto. Adotado versionamento semântico em 0.1.0 (pré-1.0: template em evolução).

**Ações realizadas:**
- Criado `VERSION` com `0.1.0`.
- `CHANGELOG.md`: seção `[Não lançado]` convertida em `[0.1.0] - 2026-10-27`, com nova seção `[Não lançado]` vazia.

**Resultado:** Tag anotada `v0.1.0` criada localmente sobre o commit desta entrada.

**Arquivos afetados:** `VERSION`, `CHANGELOG.md`, `history.md`

**Pendências:** Autorização para push dos 7 commits e da tag `v0.1.0`.

**Commit:** `chore: versiona o template em 0.1.0`

## 2026-10-27 — Regra de confirmação para commit e push

**Tipo:** documentação
**Escopo:** geral

**Contexto:** O responsável definiu que o agente deve perguntar sobre commit e push separadamente e nunca executar push automaticamente.

**Ações realizadas:**
- Registrada a decisão D-004 em `.ai/memory/decisions.md`.
- Acrescentada a regra na seção 4 de `CLAUDE.md`.

**Resultado:** Regra vigente a partir desta entrada.

**Arquivos afetados:** `CLAUDE.md`, `.ai/memory/decisions.md`, `history.md`

**Pendências:** Autorização para push dos 6 commits locais.

**Commit:** `docs(ai): registra regra de confirmacao para commit e push (D-004)`

## 2026-10-27 — Correção dos workflows de CI

**Tipo:** correção
**Escopo:** geral

**Contexto:** Após o push, os workflows `backend`, `frontend`, `firmware` e `hil` falharam e o `rag` não executou. Na interface do GitHub os quatro apareciam pelo caminho do arquivo, não pelo `name`, indicando arquivo inválido.

**Ações realizadas:**
- Reproduzida a falha com PyYAML (instalado fora do repositório): `mapping values are not allowed here` nos quatro arquivos.
- Causa: `run: echo "preencher: ..."` com `: ` em escalar sem aspas. Valores de `run` passaram a usar aspas simples externas.
- `rag.yml`: removido o filtro `paths` (os pushes recentes não tocavam `rag/**`) e adicionados `branches: [main]` e `workflow_dispatch`.

**Resultado:** Os cinco arquivos passam no parser local e expõem o `name` esperado. Execução no GitHub ainda não confirmada.

**Arquivos afetados:** `.github/workflows/*.yml`, `.ai/results/2026-10-27-validacao-revisao.md`

**Pendências:** Push e conferência da aba Actions. O `hil.yml` contém acento em texto de `echo`; sem impacto esperado.

**Commit:** `fix(ci): corrige yaml invalido e gatilho do workflow rag`

## 2026-10-27 — Licença MIT e migração da chave de atribuição

**Tipo:** documentação
**Escopo:** geral

**Contexto:** Pendências de licença e de atribuição (`includeCoAuthoredBy` deprecada desde a v2.0.62, conforme a referência oficial de configurações do Claude Code).

**Ações realizadas:**
- Adicionado `LICENSE` (MIT, titular Marcelo Duarte Lima) e avisos de substituição em `README.md` e `CONTRIBUTING.md`; seção de autoria no `README.md`.
- Removida a chave `includeCoAuthoredBy` de `.claude/settings.json`; mantido `attribution` com `commit` e `pr` vazios.
- Remoto `origin` verificado: `origin/main` em `90af7c3` antes dos commits desta entrada.

**Resultado:** JSON de `settings.json` válido. Versão local da extensão (2.1.311) acima da mínima da forma `"attribution": false` (2.1.281); mantida a forma com strings vazias por compatibilidade.

**Arquivos afetados:** `LICENSE`, `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `.claude/settings.json`

**Pendências:** Push dos commits novos. Ampliar `deny` com variações (`rm -fr`, `Remove-Item -Recurse`) é opcional.

**Commit:** `b896737`, `8d59c1d`

## 2026-10-27 — Reforço das permissões em settings.json

**Tipo:** infraestrutura
**Escopo:** geral

**Contexto:** Pendência da entrada anterior: a edição de `.claude/settings.json` foi bloqueada para o agente e aplicada manualmente pelo responsável.

**Ações realizadas:**
- Adicionados ao `deny`: `git push -f`, `git reset --hard`, leitura de `.env` e `.env.*`.
- Adicionado ao `allow`: `rag/eval.py`.
- Diff revisado e JSON validado.

**Resultado:** Arquivo com sintaxe válida. Efeito das regras não exercitado em sessão nova.

**Arquivos afetados:** `.claude/settings.json`, `history.md`, `.ai/memory/context.md`

**Pendências:** Nenhuma nova.

**Commit:** `chore(ai): reforca permissoes do agente em settings.json`

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

**Pendências:** Conferir a chave `includeCoAuthoredBy` na documentação atual. `LICENSE` depende de escolha do responsável. Indexação de `.kicad_*` não implementada. `CLAUDE.md` e `ai-project-template-APAGAR/` fora do repositório, na pasta pai. Preencher placeholders de `context.md` e `README.md`.

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
