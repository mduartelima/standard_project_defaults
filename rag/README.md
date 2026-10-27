# rag/

RAG local do projeto. Arquitetura completa em [`docs/rag-architecture.md`](../docs/rag-architecture.md).

```bash
python rag/ingest.py --stats                 # (re)indexar
python rag/query.py "pergunta"               # buscar
python rag/query.py "pergunta" --prompt      # prompt pronto com contexto e citações
python rag/query.py "pergunta" --kind decision,memory
python rag/query.py "pergunta" --json        # integração com scripts/MCP
```

Requisitos: Python 3.9+ com SQLite compilado com FTS5 (padrão nas distribuições atuais). Sem dependências externas.

`index.db` é gerado e não deve ser versionado.

Datasheets/manuais em PDF: converter para texto e salvar em `docs/datasheets/` para indexação, ex.:
`pdftotext -layout manual.pdf docs/datasheets/manual.md`
