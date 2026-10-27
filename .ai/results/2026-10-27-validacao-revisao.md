# Resultado: validação da revisão do template

- Data: 2026-10-27

| Verificação | Comando | Resultado |
|---|---|---|
| Testes do RAG | `python -m unittest discover -s tests/rag -v` | 5/5 OK; 3 falham sem a correção |
| Avaliação de recuperação | `python rag/eval.py` | hit rate@5 = 3/3 |
| Indexação | `python rag/ingest.py --stats` | 33 arquivos, 128 chunks |
| Hook `commit-msg` | 14 mensagens em Git Bash | todas conforme o esperado |
| Caminhos citados em Markdown | varredura por regex | só `rag/index.db` (gerado) |
| Sintaxe YAML dos workflows | PyYAML `safe_load` | 4 de 5 inválidos no primeiro push; corrigidos e 5/5 válidos |
