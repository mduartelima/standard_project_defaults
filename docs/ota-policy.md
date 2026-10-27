# Política de atualização remota (OTA)

> Campos a preencher. Consultar a documentação oficial do bootloader escolhido antes de transformar em regra; este modelo não fixa bootloader.

## Parâmetros

| Item | Valor |
|---|---|
| Bootloader / modo de swap | <preencher> |
| Layout de partições (slots, trailer) | <preencher> |
| Política de versão (anti-rollback) | <preencher> |
| Assinatura de imagens | <algoritmo> |
| Custódia da chave privada | <cofre de segredos ou HSM; nunca no repositório> |
| Confirmação da imagem | <após quais autotestes a aplicação confirma> |
| Rollback | <comportamento sem confirmação> |
| Rotação de chaves | <plano> |

## Matriz de testes

| Caminho | Testado | Resultado |
|---|---|---|
| Atualização pendente (pending) | [ ] | |
| Execução de teste (test) | [ ] | |
| Confirmação (confirm) | [ ] | |
| Reversão (revert) | [ ] | |
| Atualização permanente | [ ] | |

## Segurança

Referência: ETSI EN 303 645. Outras normas (IEC 62443, NIST IR 8259) devem ser lidas nos textos primários antes de serem citadas como requisito.
