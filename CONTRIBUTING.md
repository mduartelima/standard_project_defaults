# Contribuindo

## Fluxo

1. Ler `CLAUDE.md` (regras de trabalho) e `.ai/memory/context.md` (estado atual).
2. Ativar os hooks: `git config core.hooksPath .githooks` e `git config commit.template .gitmessage`.
3. Um objetivo por branch e por commit.
4. Seguir `docs/commit-convention.md` (o hook `commit-msg` valida o cabeçalho).
5. Validar antes do PR: testes, lint e build da camada alterada. Firmware compila para o alvo.
6. Documentar: entrada no topo de `history.md`, `context.md` atualizado e decisão em `decisions.md` quando aplicável.
7. Abrir o PR com o modelo de `.github/pull_request_template.md`.

## Testes

Convenção por camada em `tests/README.md`. Bug corrigido ganha teste de regressão.

## Diretrizes técnicas

`docs/engineering-guidelines.md`.

## Licença

Contribuições ao template são aceitas sob a licença MIT (`LICENSE`). Em projetos derivados, substituir ou remover o `LICENSE` e definir a licença e o titular do próprio projeto.
