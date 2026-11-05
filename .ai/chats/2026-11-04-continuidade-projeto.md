# Sessão 2026-11-04 — Consolidação do projeto para continuidade em outro computador

**Objetivo:** Reunir em um único arquivo tudo o que foi implementado, definido e executado nas sessões de 2026-10-27 a 2026-11-04, para retomar o trabalho a partir de uma cópia da pasta em outro computador.
**Ferramenta/modelo:** Claude Code (extensão do VS Code)

## Resumo

O repositório `standard_project_defaults` é um template para iniciar projetos de software, firmware e hardware com agentes de IA: memória local versionada em `.ai/`, RAG offline (SQLite FTS5 com BM25), histórico impessoal em `history.md`, Conventional Commits validados por hook e modelos agnósticos de stack por camada. Estado em 2026-11-04: versões 0.1.0 a 0.1.3 publicadas (tags e Releases no GitHub), `main` e `develop` sincronizadas com `origin`, `AGENTS.md` como fonte canônica das regras e `CLAUDE.md` como ponte. Não há trabalho em andamento; o projeto está em estado de repouso aguardando uso.

## Como retomar em outro computador

1. Copiar a pasta inteira, **incluindo `.git`**. O `.git/config` leva junto `core.hooksPath=.githooks`, `commit.template=.gitmessage` e o remoto `origin`. Em um clone novo, repetir:

   ```bash
   git config core.hooksPath .githooks
   git config commit.template .gitmessage
   ```

2. Remoto: `https://github.com/mduartelima/standard_project_defaults.git`. Branches `main` (publicada) e `develop` (trabalho). Tags `v0.1.0` a `v0.1.3`.
3. Regenerar o índice do RAG, que é artefato ignorado pelo git: `python rag/ingest.py`.
4. Requisitos: Python 3 (biblioteca padrão com SQLite FTS5), Git e Git Bash no Windows (o hook `commit-msg` é shell).
5. Iniciar o agente de IA na pasta. Ele deve ler `AGENTS.md` (Claude Code o recebe pelo import em `CLAUDE.md`), depois `.ai/memory/context.md`, as últimas 5 entradas de `history.md` e `.ai/memory/decisions.md`. Em caso de dúvida, consultar com `python rag/query.py "<pergunta>"`.
6. O que **não** acompanha a pasta: a memória automática do Claude Code (fica em `~/.claude/projects/...`; a regra que ela guarda, de confirmar commit e push, também está em `AGENTS.md`), o índice `rag/index.db` e `.claude/settings.local.json`, se existir.
7. Os arquivos `files.zip` e `temp.txt`, que ficavam na pasta pai, não fazem parte do projeto. O conteúdo de `temp.txt` foi guardado em `.ai/analyses/2026-10-27-referencia-estrutura-iot.md`.

## Linha do tempo (o que foi feito)

| Data | Marco | Versão / commit de referência |
|---|---|---|
| 2026-10-27 | Estruturação inicial: `.ai/`, RAG, hook, regras do agente; D-001 a D-003 | `cb4ccfa` |
| 2026-10-27 | Correção dos bugs do RAG (filtro `--kind`, `IndexNotFound`, `eval.py` vazio) com testes em `tests/rag/` | `13b9548` |
| 2026-10-27 | RAG indexa `.csv`, `.conf`, `sdkconfig`; peso de `datasheet` 1.3 | `9e88f5a` |
| 2026-10-27 | Criados `docs/api.md`, `docs/protocol.md`, `docs/datasheets/`, `.env.example`; `.gitattributes`, `.editorconfig` | `659e239`, `66a4de1` |
| 2026-10-27 | Governança, modelos por camada, OTA, release de hardware, CI por camada, licença MIT | `920f100` a `bdcb3f3` |
| 2026-10-27 | Reforço das permissões em `.claude/settings.json`; D-004 (commit e push sempre perguntados) | `d8e0223`, `67ce6bc` |
| 2026-10-27 | Versão 0.1.0 | tag `v0.1.0` |
| 2026-10-27 | Incorporação seletiva de referência IoT: chaves privadas no `.gitignore`, `src/protocol/`, `hardware.yml`, divisão opcional do firmware | `1386baf` a `efb609b` |
| 2026-10-27 | Versão 0.1.1; branch `develop` criada | tag `v0.1.1` |
| 2026-10-27 | README reescrito como vitrine do template (PT-BR com resumo em inglês); modelo para derivados em `docs/README.project-template.md` | `68030cd`, `6f3431c` |
| 2026-11-04 | Versão 0.1.2 | tag `v0.1.2` |
| 2026-11-04 | `AGENTS.md` canônico, `CLAUDE.md` ponte, D-005, glossário | `ebc4b69` a `1c364aa` |
| 2026-11-04 | Versão 0.1.3; Release publicada; import verificado no VS Code | tag `v0.1.3`, `e5e05bd` |

Detalhes por entrada em `history.md`; resultados de validação em `.ai/results/2026-10-27-validacao-revisao.md`; análises em `.ai/analyses/`.

## Decisões tomadas

- **D-001** Memória de IA em Markdown versionada em `.ai/`, com RAG local sobre ela.
- **D-002** RAG local com SQLite FTS5 (BM25), zero dependências; embeddings e MCP como evolução futura (não implementados).
- **D-003** `Co-Authored-By` só sob pedido, por commit; o hook exige `ALLOW_COAUTHOR=1`.
- **D-004** Commit e push sempre perguntados, em perguntas separadas; push nunca automático. A autorização vale para a ocasião e para as ações nomeadas no pedido do responsável (por exemplo "commit, push, merge").
- **D-005** `AGENTS.md` fonte canônica das regras; `CLAUDE.md` ponte com `@AGENTS.md`. Onde D-001 a D-004 citam `CLAUDE.md`, leia-se `AGENTS.md`.
- Template agnóstico quanto a stack de firmware e EDA; placeholders (`<...>`) são intencionais e preenchidos em cada projeto derivado.
- Licença MIT no template (titular Marcelo Duarte Lima); projetos derivados substituem ou removem o `LICENSE`.
- Versionamento semântico, pré-1.0; `VERSION`, `CHANGELOG.md` e tags `vX.Y.Z`; mudanças vão para `develop`, integração na `main` por fast-forward.
- Hardware: saídas de fabricação geradas a partir da tag e anexadas à release, não versionadas (`docs/hardware-release.md`).
- Chaves privadas nunca no repositório (`.gitignore` bloqueia `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.jks`, `*.keystore`).

## Acordos de trabalho com o agente

- Ciclo: Analisar, Levantar, Implementar, Validar, Documentar, Commitar (`AGENTS.md`).
- Pedidos genéricos ("execute as recomendações") não autorizam commit nem push; o agente pergunta.
- O agente não altera as próprias permissões em `.claude/settings.json` sem pedido explícito do responsável.
- Escrita impessoal em `history.md`, entrada nova no topo; datas em ISO 8601.
- Em modo de planejamento, o agente só lê e escreve o arquivo de plano.

## Informações levantadas (fatos verificáveis)

- Claude Code: `includeCoAuthoredBy` está deprecada desde a v2.0.62; a chave atual é `attribution` (`commit` e `pr` vazios ocultam a atribuição). Fonte: https://code.claude.com/docs/en/settings-reference.md.
- Claude Code: `@AGENTS.md` dentro de `CLAUDE.md` é carregado no início da sessão, sem aprovação, com caminho relativo e até 4 saltos; leitura nativa de `AGENTS.md` exige v2.1.277 ou superior e só vale sem `CLAUDE.md`; link simbólico é inadequado no Windows. Fonte: https://code.claude.com/docs/en/memory.md. Confirmado na prática na extensão do VS Code em 2026-11-04.
- O `/memory` da extensão do VS Code lista só memória automática; não serve para verificar arquivos de instruções.
- GitHub: um YAML de workflow com `: ` em valor sem aspas é inválido (ocorreu em `run: echo "preencher: ..."`); o GitHub lista o workflow pelo caminho do arquivo em vez do `name` quando não consegue lê-lo. Validar com PyYAML antes do push.
- Workflows: só `rag.yml` roda em push na `main` e em PRs; backend, frontend, firmware, hardware e HIL são de disparo manual (`workflow_dispatch`).
- O `gh` (GitHub CLI) não está instalado na máquina de origem; Releases foram criadas pela interface web.
- Regras `deny` do `settings.json` casam por prefixo: variações (`rm -fr`, `Remove-Item -Recurse`, `git push --force-with-lease`) escapam.

## Pendências

- Verificar o import `@AGENTS.md` no CLI, se utilizado (no VS Code já confirmado).
- Preencher no GitHub (Settings → General) a descrição, os tópicos e marcar **Template repository**; confirmar se já foi feito. Texto sugerido está no histórico da conversa e resumido em `README.md` (palavras-chave).
- Opcional: ampliar o `deny` de `.claude/settings.json` com as variações citadas acima.
- Opcional: indexar `.kicad_*` no RAG (exige chunker próprio para s-expressions).
- Opcional: busca híbrida com embeddings e servidor MCP (fases 2 e 3 de `docs/rag-architecture.md`).
- Ao usar o template em um projeto real: copiar `docs/README.project-template.md` para `README.md`, substituir o `LICENSE`, preencher `.ai/memory/context.md` e remover as camadas que não se aplicam.

## Estrutura de referência

```text
AGENTS.md / CLAUDE.md   regras (canônico) e ponte
history.md              histórico impessoal, mais recente no topo
.ai/memory/             context.md, decisions.md (D-001..D-005), glossary.md
.ai/chats/ analyses/ results/ prompts/
docs/                   arquitetura, RAG, commits, engenharia, API, protocolo, OTA, release de hardware
rag/                    ingest.py, query.py, eval.py, config.json
src/                    backend, frontend, firmware, hardware, protocol
tests/                  rag (unittest), demais camadas com README
.github/workflows/      rag.yml (ativo), demais de disparo manual
```

Comandos úteis: `python rag/ingest.py`, `python rag/query.py "..." --kind decision`, `python rag/eval.py`, `python -m unittest discover -s tests/rag -v`.
