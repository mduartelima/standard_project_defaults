# CLAUDE.md — Regras do Agente de IA

> Arquivo lido automaticamente pelo Claude Code no início de cada sessão.
> `AGENTS.md` aponta para cá (Codex, Cursor, Copilot e outros agentes).
> Mantenha este arquivo curto: regras estáveis aqui, conhecimento volátil em `.ai/memory/`.

## 1. Inicialização de sessão (obrigatório)

Antes de qualquer ação, ler na ordem:

1. `.ai/memory/context.md` — estado atual do projeto, prioridades, bloqueios.
2. `history.md` — últimas 5 entradas.
3. `.ai/memory/decisions.md` — decisões vigentes (não contrariar sem registrar nova decisão).
4. Se a tarefa exigir conhecimento além disso: `python rag/query.py "<pergunta>"` e usar os trechos retornados como contexto, citando o arquivo de origem.

## 2. Ciclo de trabalho padrão

Toda tarefa segue: **Analisar → Levantar → Implementar → Validar → Documentar → Commitar**.

| Etapa | Ação | Saída |
|---|---|---|
| Analisar | Entender o pedido, ler código e memória relevantes | Plano curto antes de editar |
| Levantar | Registrar fatos, restrições, riscos e alternativas | `.ai/analyses/AAAA-MM-DD-tema.md` (se não trivial) |
| Implementar | Mudanças mínimas e coesas; um objetivo por commit | Código |
| Validar | Rodar testes/lint/build; para firmware, compilar para o alvo | Resultado em `.ai/results/` se relevante |
| Documentar | Entrada impessoal em `history.md`; atualizar `context.md` | Markdown |
| Commitar | Conventional Commits, linguagem técnica, **`Co-Authored-By` só se solicitado no commit** | Commit |

Se o pedido for ambíguo, perguntar antes de implementar. Se for apenas análise, não alterar código.

## 3. Regras de documentação

- Escrita **impessoal** e técnica: "Implementado parser…", "Corrigido overflow…". Nunca "eu fiz", "vamos", "o Claude".
- Datas em ISO 8601 (`2026-10-27`).
- `history.md`: entrada nova **no topo**, seguindo o modelo do próprio arquivo.
- `context.md`: reescrever (não acumular) — reflete apenas o estado presente.
- `decisions.md`: append-only; decisão revogada recebe status `Substituída por D-XXX`.
- Resumo de sessão longa ou relevante: `.ai/chats/AAAA-MM-DD-tema.md`.

## 4. Regras de commit

Ver `docs/commit-convention.md`. Resumo:

```
<tipo>(<escopo>): <descrição no imperativo, minúscula, sem ponto final>

<corpo opcional: o quê e por quê, linhas ≤ 72 colunas>

<rodapé opcional: Refs #123, BREAKING CHANGE: ...>
```

- Proibido: menções a IA/assistente e emojis.
- `Co-Authored-By`: nunca automático. Só é adicionado quando o usuário solicitar deliberadamente, a cada commit (o pedido não vale para o commit seguinte). O hook só aceita o trailer com `ALLOW_COAUTHOR=1` (D-003).
- Commitar apenas quando a mudança for relevante e validada. Não commitar arquivos gerados (`rag/index.db`, builds).
- Hook `.githooks/commit-msg` valida o formato. Ativar com `git config core.hooksPath .githooks`.

## 5. Regras de engenharia

- Ler o código existente antes de propor mudanças; seguir o estilo local.
- Não inventar APIs, registradores, pinos ou parâmetros: se não estiver no repositório ou no datasheet indexado, perguntar.
- Firmware/hardware: ver `docs/engineering-guidelines.md` (sem alocação dinâmica em ISR, timeouts em todo I/O, revisão de pinout contra esquemático).
- Segredos nunca no código nem na memória: usar `.env` (fora do git).

## 6. Limites

- Não executar comandos destrutivos (`rm -rf`, `git push --force`, gravação de flash/fuses) sem confirmação explícita.
- Não editar `history.md` antigo, exceto para corrigir erro factual (registrar a correção).
