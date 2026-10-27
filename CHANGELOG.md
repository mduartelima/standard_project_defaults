# Changelog

Mudanças relevantes por versão, no estilo Keep a Changelog (seções Adicionado, Alterado, Corrigido, Removido). Versionamento semântico para o software; firmware e contratos de protocolo seguem `docs/protocol.md`. A versão do template consta em `VERSION` e nas tags `vX.Y.Z`.

## [Não lançado]

### Alterado
- `README.md` passa a apresentar o template (objetivo, necessidade atendida, vantagens, implementação e uso, com resumo em inglês); o modelo com placeholders foi movido para `docs/README.project-template.md`.

## [0.1.1] - 2026-10-27

### Adicionado
- `src/protocol/` como diretório de schemas do protocolo (formato a definir por projeto) e indexação de `.proto` no RAG.
- Workflow `hardware.yml` (disparo manual) para ERC/DRC.
- Divisão opcional do firmware (bootloader, targets, ota-tools, shared) em `src/firmware/README.md`.
- Análise de referência de estrutura IoT em `.ai/analyses/`.

### Alterado
- `.gitignore` bloqueia chaves e certificados privados; `SECURITY.md` e `docs/ota-policy.md` definem a custódia de chaves.

## [0.1.0] - 2026-10-27

### Adicionado
- Estrutura inicial do template: memória em `.ai/`, RAG local (SQLite FTS5), hook e convenção de commits, esqueleto por camada.
- Licença MIT e aviso de substituição em projetos derivados.
- Governança: `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`, `CHANGELOG.md`.
- Modelos: `docs/api.md`, `docs/protocol.md`, `docs/ota-policy.md`, `docs/hardware-release.md`, READMEs por camada, `tests/README.md` e checklist HIL.
- CI: `rag.yml` (ativo) e workflows de backend, frontend, firmware e HIL com disparo manual.
- Regras do agente: Co-Authored-By sob pedido (D-003) e confirmação de commit e push (D-004).

### Alterado
- `.claude/settings.json` usa `attribution` (substitui `includeCoAuthoredBy`) e nega `git push -f`, `git reset --hard` e leitura de `.env`.
- RAG indexa `.csv`, `.conf` e `sdkconfig`; peso de `datasheet` elevado.

### Corrigido
- RAG: filtro `--kind`, mensagem sem índice e `eval.py` com casos vazios.
- CI: YAML inválido nos workflows de disparo manual e gatilho do `rag.yml`.
