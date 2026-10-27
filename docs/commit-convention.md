# Convenção de Commits

Baseada em [Conventional Commits 1.0](https://www.conventionalcommits.org/pt-br/v1.0.0/), adaptada ao projeto.

## Formato

```
<tipo>(<escopo>): <descrição>

[corpo]

[rodapé]
```

| Campo | Regra |
|---|---|
| tipo | obrigatório, da tabela abaixo |
| escopo | recomendado: `backend`, `frontend`, `firmware`, `hardware`, `rag`, `docs`, `ai`, ou módulo específico (`firmware/uart`) |
| descrição | imperativo, minúscula, sem ponto final, ≤ 72 caracteres no cabeçalho inteiro |
| corpo | o quê e por quê; linhas ≤ 72 colunas; separado por linha em branco |
| rodapé | `Refs #N`, `Closes #N`, `BREAKING CHANGE: ...` |

## Tipos

| Tipo | Uso |
|---|---|
| `feat` | nova funcionalidade |
| `fix` | correção de bug |
| `refactor` | mudança interna sem alterar comportamento |
| `perf` | melhoria de desempenho, consumo de memória ou energia |
| `docs` | documentação, history.md, memória `.ai/` |
| `test` | testes |
| `build` | sistema de build, dependências, toolchain, linker script |
| `ci` | pipelines |
| `chore` | manutenção sem impacto em código de produção |
| `revert` | reversão de commit |

## Regras obrigatórias

- **`Co-Authored-By` nunca é automático.** Só é permitido quando solicitado deliberadamente, a cada commit, e o hook exige `ALLOW_COAUTHOR=1` nesse commit (D-003).
- Sem menção a IA, assistente ou ferramenta de geração, exceto o trailer acima.
- Sem emojis.
- Linguagem técnica e impessoal.
- Um objetivo lógico por commit. Não misturar refatoração com correção.
- Não commitar artefatos gerados (`rag/index.db`, `build/`, binários).

## Exemplos

```
feat(firmware/uart): adiciona recepção por dma com buffer circular

Substitui a recepção por interrupção byte a byte, que perdia dados
acima de 460800 baud. Buffer de 512 bytes com detecção de idle line.

Refs #12
```

```
fix(backend): corrige condição de corrida na fila de telemetria
```

```
docs: registra análise de consumo em modo sleep no history.md
```

```
perf(firmware): reduz uso de ram em 3,2 kb movendo tabelas para flash
```

## Validação automática

```bash
git config core.hooksPath .githooks
git config commit.template .gitmessage
```

O hook `.githooks/commit-msg` rejeita mensagens fora do formato e bloqueia `Co-Authored-By`, salvo com `ALLOW_COAUTHOR=1` no ambiente do commit. O hook não remove nada: apenas rejeita.

## Ferramentas de IA

Configurar o agente para não adicionar atribuição automática em commits. No Claude Code isso é feito em `.claude/settings.json` (o nome exato da opção pode mudar entre versões — conferir em https://docs.claude.com/en/docs/claude-code/settings). Independentemente da configuração, o hook garante a regra.
