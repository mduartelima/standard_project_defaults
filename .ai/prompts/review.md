Revisar as alterações em: {{git diff main...HEAD | arquivos}}

<criterios>
Para cada achado, classificar severidade (crítico | importante | sugestão) e citar `arquivo:linha`:
1. Correção: bugs, condições de corrida, casos de borda, tratamento de erro.
2. Segurança: entrada não validada, segredos, injeção, overflow.
3. Recursos: vazamento de memória/handles, uso de stack, alocação em ISR.
4. Legibilidade e aderência ao padrão do repositório.
5. Testes: cobertura das mudanças.
</criterios>

<formato_saida>
Tabela: Severidade | Arquivo:linha | Problema | Sugestão.
Ao final, veredito: aprovar | aprovar com ressalvas | reprovar.
Não reportar preferências de estilo já resolvidas pelo linter.
</formato_saida>
