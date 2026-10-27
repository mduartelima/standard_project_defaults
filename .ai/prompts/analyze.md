<contexto>
Projeto: ver `CLAUDE.md` e `.ai/memory/context.md`.
Motivação da análise: {{por_que_esta_analise_importa}}
</contexto>

<tarefa>
Realizar levantamento técnico sobre: {{tema}}
Escopo: {{arquivos_modulos_ou_documentos}}
</tarefa>

<instrucoes>
1. Consultar o RAG: `python rag/query.py "{{tema}}"` e ler os arquivos retornados.
2. Ler o código e documentos do escopo. Não alterar nenhum arquivo de código.
3. Separar **fatos** (com fonte: `arquivo:linha` ou seção do documento) de **inferências** (marcadas como tal).
4. Se uma informação não estiver disponível, declarar "não encontrado" em vez de supor.
5. Listar alternativas com prós, contras e esforço.
</instrucoes>

<formato_saida>
Salvar em `.ai/analyses/{{AAAA-MM-DD}}-{{tema-curto}}.md` seguindo `_TEMPLATE.md`.
Responder no chat com um resumo de até 8 linhas e a recomendação.
</formato_saida>
