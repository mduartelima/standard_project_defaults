<sintoma>
{{comportamento observado}}
</sintoma>

<esperado>
{{comportamento esperado}}
</esperado>

<evidencias>
{{logs, stack trace, saída serial, captura de osciloscópio/analisador lógico, passos para reproduzir}}
</evidencias>

<instrucoes>
1. Em `<analise>`, listar hipóteses de causa raiz ordenadas por probabilidade, com a evidência que sustenta ou refuta cada uma.
2. Confirmar a causa raiz (teste mínimo, log adicional ou leitura de código) antes de corrigir.
3. Corrigir a causa raiz, não o sintoma. Se a correção for paliativa, declarar explicitamente.
4. Adicionar teste de regressão quando possível.
5. Registrar em `history.md` (Tipo: correção) com causa raiz e solução; commitar como `fix(<escopo>): ...`.
</instrucoes>
