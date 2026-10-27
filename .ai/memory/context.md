# Contexto Atual

> Fonte da verdade sobre o **estado presente**. Reescrever a cada sessão relevante; não acumular histórico (isso é papel do `history.md`).
> Última atualização: 2026-10-27

## Objetivo do projeto
<O que o projeto entrega, em 2–3 frases.>

## Estado atual
- Fase: <descoberta | prototipagem | desenvolvimento | validação | produção>
- Último marco concluído: Correções do RAG, arquivos ausentes, governança, modelos por camada e CI (2026-10-27).

## Prioridades (ordem)
1. Aplicar manualmente o reforço de `.claude/settings.json`.
2. Preencher objetivo, stack e READMEs de camada com dados do projeto real.
3. Decidir a licença (`LICENSE`).

## Em andamento
- <tarefa> — <status>

## Bloqueios e riscos
- Agente sem permissão para editar `.claude/settings.json` — `deny` continua curto — alteração manual do responsável.
- Workflows YAML nunca executados no GitHub — sintaxe não confirmada — validar no primeiro push.

## Restrições técnicas
- <ex.: MCU com 256 KB RAM; latência < 50 ms; operação offline>

## Próximos passos
- Verificar a chave de atribuição (`includeCoAuthoredBy`) na documentação atual.
- Avaliar indexação de `.kicad_*` no RAG.
- Resolver a duplicidade de `CLAUDE.md` e `ai-project-template-APAGAR/` na pasta pai.
