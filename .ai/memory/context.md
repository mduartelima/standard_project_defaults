# Contexto Atual

> Fonte da verdade sobre o **estado presente**. Reescrever a cada sessão relevante; não acumular histórico (isso é papel do `history.md`).
> Última atualização: 2026-11-04

> Retomada em outro computador ou nova sessão: ver `.ai/chats/2026-11-04-continuidade-projeto.md` (estado, decisões, acordos e pendências consolidados).

## Objetivo do projeto
<O que o projeto entrega, em 2–3 frases.>

## Estado atual
- Fase: <descoberta | prototipagem | desenvolvimento | validação | produção>
- Último marco concluído: Versão 0.1.3 publicada (tag, Release e `main`), com `AGENTS.md` como fonte canônica das regras (2026-11-04).

## Prioridades (ordem)
1. Próximas mudanças seguem em `develop`; versões publicadas: 0.1.0 a 0.1.3.
2. Manter o template agnóstico: placeholders são intencionais e preenchidos em cada projeto derivado.

## Em andamento
- <tarefa> — <status>

## Bloqueios e riscos
- Regras `deny` do `settings.json` casam por prefixo — variações de comando podem escapar — ampliar se necessário.

## Restrições técnicas
- <ex.: MCU com 256 KB RAM; latência < 50 ms; operação offline>

## Próximos passos
- Verificar o import `@AGENTS.md` no CLI, se utilizado (no VS Code já confirmado).
- Avaliar indexação de `.kicad_*` no RAG.
