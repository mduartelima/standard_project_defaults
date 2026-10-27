# Biblioteca de Prompts

Prompts reutilizáveis. Copiar, substituir os `{{placeholders}}` e colar no agente.
No Claude Code, podem virar comandos: copiar para `.claude/commands/<nome>.md` e invocar com `/<nome>`.

## Princípios aplicados (boas práticas de prompting)

1. **Contexto antes da tarefa** — o modelo não sabe o que não foi dito. Informar objetivo, público, restrições e o "porquê".
2. **Estrutura com tags XML** — separar `<contexto>`, `<tarefa>`, `<restricoes>`, `<formato_saida>`. Reduz ambiguidade entre instrução e dado.
3. **Instruções positivas e específicas** — "responda em tabela com colunas X, Y" > "não seja vago".
4. **Raciocínio explícito em tarefas complexas** — pedir análise em `<analise>` antes da `<resposta>`.
5. **Exemplos (few-shot)** — 1 a 3 exemplos do formato desejado, variados, dentro de `<exemplos>`.
6. **Ancoragem em fontes** — exigir citação de arquivo/linha/seção; permitir "não sei" explicitamente. Principal defesa contra alucinação.
7. **Documentos longos primeiro** — em prompts com muito material, colocar os documentos no início e a pergunta no fim.
8. **Critério de pronto** — dizer como validar (teste, compilação, checklist).

## Índice

| Prompt | Uso |
|---|---|
| `session-start.md` | Abrir sessão carregando memória |
| `analyze.md` | Levantamento/análise sem alterar código |
| `implement.md` | Implementar funcionalidade |
| `fix.md` | Diagnosticar e corrigir bug |
| `review.md` | Revisão de código |
| `firmware.md` | Tarefas de firmware/hardware |
| `document-and-commit.md` | Fechar o ciclo: history.md + commit |
| `session-end.md` | Encerrar sessão e atualizar memória |
