Analisar as implementações, correções e levantamentos realizados nesta sessão (`git status`, `git diff`).

<tarefa>
1. Documentar, de forma impessoal e técnica, uma nova entrada no topo de `history.md`, seguindo o modelo do arquivo.
2. Atualizar `.ai/memory/context.md` se o estado, prioridades ou pendências mudaram.
3. Registrar em `.ai/memory/decisions.md` qualquer decisão estrutural tomada.
4. Se as alterações forem relevantes e validadas, commitar seguindo `docs/commit-convention.md`:
   - Linguagem técnica, imperativo, minúsculas.
   - Sem `Co-Authored-By`, sem menção a IA, sem emojis.
   - Um commit por objetivo lógico; separar documentação de código se forem independentes.
5. Atualizar o campo **Commit** da entrada do `history.md` com o hash (via `git commit --amend --no-edit` apenas se o commit ainda não foi enviado ao remoto).
</tarefa>

Se nada relevante foi alterado, não commitar e informar o motivo.
