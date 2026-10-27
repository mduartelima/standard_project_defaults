<contexto>
{{descrição do problema de negócio ou requisito, e por que é necessário}}
Análise prévia (se houver): `.ai/analyses/{{arquivo}}.md`
</contexto>

<tarefa>
Implementar: {{funcionalidade}}
Camada: {{backend|frontend|firmware}}
</tarefa>

<requisitos>
- {{requisito funcional 1}}
- {{requisito não funcional: desempenho, memória, latência}}
</requisitos>

<restricoes>
- Seguir o estilo e padrões já existentes no módulo.
- Não adicionar dependências sem justificar.
- Mudança mínima necessária; sem refatorações fora do escopo.
</restricoes>

<processo>
1. Ler os arquivos relevantes e apresentar um plano curto (arquivos a alterar e por quê). Aguardar confirmação se a mudança afetar mais de {{N}} arquivos ou interfaces públicas.
2. Implementar.
3. Escrever/atualizar testes.
4. Executar: `{{comando_de_teste_e_build}}`. Corrigir até passar.
5. Executar `.ai/prompts/document-and-commit.md`.
</processo>

<criterio_de_pronto>
Testes passando, build sem warnings novos, history.md atualizado, commit realizado.
</criterio_de_pronto>
