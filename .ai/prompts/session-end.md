Encerrar a sessão:

1. Criar `.ai/chats/{{AAAA-MM-DD}}-{{tema}}.md` a partir de `_TEMPLATE.md` com resumo impessoal, decisões, informações levantadas e pendências.
2. Reescrever `.ai/memory/context.md` refletindo o estado atual.
3. Executar `python rag/ingest.py` para reindexar.
4. Se houver alterações não commitadas relevantes, aplicar `.ai/prompts/document-and-commit.md`.
