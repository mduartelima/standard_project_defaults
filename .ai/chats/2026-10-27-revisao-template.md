# Sessão 2026-10-27 — Revisão do template fullstack + firmware + hardware

**Objetivo:** Levantar os modelos atuais de estrutura fullstack + firmware + hardware e planejar revisão, melhoria e validação do template.
**Ferramenta/modelo:** Claude Code

## Resumo
O repositório é um modelo-base reutilizável para novos projetos e para atualizar projetos existentes. Os placeholders de `context.md`, `README.md` e `docs/architecture.md` são intencionais. Foram feitas auditoria do template, pesquisa web de padrões e plano em 8 passos, detalhado em `.ai/analyses/2026-10-27-revisao-template.md`. O passo 1 (regra de `Co-Authored-By`) foi implementado e validado.

## Decisões tomadas
- Template permanece agnóstico quanto a stack de firmware e EDA.
- `Co-Authored-By` nunca automático; só sob solicitação por commit, com `ALLOW_COAUTHOR=1` no hook → registrado como D-003 em `.ai/memory/decisions.md`.
- Itens sem fonte primária (IEC 62443, NIST IR 8259, registro de schemas, CODEOWNERS, Keep a Changelog, docs oficiais do MCUboot) entram como campos a preencher até leitura da fonte.

## Informações levantadas
- Auditoria: referências quebradas (`docs/api.md`, `docs/protocol.md`, `docs/datasheets/`, `.env.example`), bugs no RAG (`eval.py:21`, `query.py:222`, `query.py:229-232`), `settings.json` com `deny` curto e `python` em vez de `python3`, escopos não validados no hook, `.gitignore` amplo demais. Detalhes na análise.
- Pesquisa: HIL com build em nuvem e teste em runner self-hosted; MCUboot com duas slots e confirmação de imagem; tags de revisão de hardware com saídas geradas a partir da tag; ETSI EN 303 645 como referência de segurança. Fontes na análise.
- Hook `commit-msg` testado em Git Bash: trailer sem variável rejeitado, com `ALLOW_COAUTHOR=1` aceito, sem trailer aceito.

## Pendências
- Passos 2 a 8 do plano: inconsistências, governança, READMEs por camada, contratos e OTA, hardware, CI, testes.
- Conferir a chave de atribuição de `.claude/settings.json` (`includeCoAuthoredBy`) na documentação atual.
- Após a mudança para `standard_project_defaults`: a pasta passa a ser a raiz do projeto. Os dois `CLAUDE.md` (raiz antiga e template) ficam redundantes; manter um só e ajustar caminhos.
- Testar o hook com `git commit` real num repositório (o diretório atual não é git).
