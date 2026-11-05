# Registro de Decisões (ADR resumido)

Append-only. Decisão revogada não é apagada: muda o status para `Substituída por D-XXX`.

<!--
## D-XXX — <título>
- **Data:** AAAA-MM-DD
- **Status:** Proposta | Aceita | Substituída por D-YYY
- **Contexto:** problema e forças em jogo.
- **Decisão:** o que foi decidido.
- **Alternativas consideradas:** opção — motivo da rejeição.
- **Consequências:** impactos positivos e negativos.
-->

## D-001 — Memória de IA versionada no repositório
- **Data:** 2026-10-27
- **Status:** Aceita
- **Contexto:** Agentes de IA não retêm contexto entre sessões; conhecimento em chats externos se perde.
- **Decisão:** Manter memória em Markdown dentro de `.ai/`, versionada no git, e RAG local sobre ela.
- **Alternativas consideradas:** memória do provedor de IA — não portável entre ferramentas e não auditável; wiki externa — fora do fluxo do código.
- **Consequências:** Contexto auditável e portável; exige disciplina de atualização (garantida pelo ciclo em `CLAUDE.md`).

## D-002 — RAG local com SQLite FTS5
- **Data:** 2026-10-27
- **Status:** Aceita
- **Contexto:** Necessidade de busca no conhecimento do projeto sem infraestrutura externa.
- **Decisão:** Índice BM25 em SQLite FTS5 (zero dependências), com evolução opcional para busca híbrida com embeddings.
- **Alternativas consideradas:** banco vetorial dedicado — custo operacional desproporcional na fase inicial.
- **Consequências:** Busca lexical rápida e offline; sinônimos podem exigir embeddings no futuro.

## D-003 — Co-Authored-By apenas sob solicitação por commit
- **Data:** 2026-10-27
- **Status:** Aceita
- **Contexto:** A regra inicial proibia `Co-Authored-By` de forma absoluta. Ferramentas de IA o adicionam por padrão, e há casos em que o usuário quer a atribuição deliberadamente.
- **Decisão:** Proibido de forma automática. Permitido somente quando o usuário solicitar para aquele commit; o pedido não vale para commits seguintes. O hook `.githooks/commit-msg` aceita o trailer apenas com `ALLOW_COAUTHOR=1` no ambiente do commit. Menções a IA fora desse trailer, assinaturas de geração e emojis seguem bloqueadas.
- **Alternativas consideradas:** exceção só textual, com o hook bloqueando sempre — a regra ficaria impossível de cumprir sem editar o hook; marcador na mensagem — exige o hook remover o marcador e altera a mensagem gravada.
- **Consequências:** Atribuição passa a ser decisão explícita por commit. A proibição absoluta anterior, que constava apenas em `CLAUDE.md`, `commit-convention.md`, `.gitmessage` e no hook, deixa de valer.

## D-004 — Commit e push sempre sob confirmação, separadamente
- **Data:** 2026-10-27
- **Status:** Aceita
- **Contexto:** Commits e pushes feitos pelo agente a partir de pedidos genéricos ("executar as recomendações") publicaram conteúdo e dispararam CI sem confirmação específica.
- **Decisão:** O agente sempre pergunta antes de `git commit` e, em pergunta separada, antes de `git push`. A autorização de um não vale para o outro nem para ocorrências seguintes. O agente nunca executa push de forma automática.
- **Alternativas consideradas:** autorização geral por sessão — o escopo do que é publicado deixa de ser revisado; apenas bloquear push — o histórico local passaria a crescer sem revisão.
- **Consequências:** Mais interações por tarefa; o responsável controla o que entra no histórico e o que é publicado. O ciclo em `CLAUDE.md` passa a ter confirmação explícita na etapa Commitar.

## D-005 — AGENTS.md como fonte canônica das regras; CLAUDE.md como ponte
- **Data:** 2026-11-04
- **Status:** Aceita
- **Contexto:** As regras dos agentes ficavam em `CLAUDE.md` e `AGENTS.md` apenas apontava para ele, vinculando o projeto a um fornecedor, embora qualquer ferramenta de agente e qualquer modelo possam ser usados.
- **Decisão:** `AGENTS.md` passa a conter as regras e a terminologia (agente de IA, ferramenta de agente, modelo). `CLAUDE.md` vira ponte de compatibilidade com a linha `@AGENTS.md`, que o Claude Code importa no início da sessão. Referências ativas em guias e prompts passam a `AGENTS.md`; registros históricos (D-001 a D-004, `history.md`, análises e chats) não são reescritos.
- **Alternativas consideradas:** manter `CLAUDE.md` canônico — preserva o vínculo com um fornecedor; duplicar as regras nos dois arquivos — risco de divergência; link simbólico — no Windows exige privilégio e o Git o baixa como texto; só `AGENTS.md`, sem `CLAUDE.md` — leitura nativa exige Claude Code v2.1.277 ou superior e versões antigas ignorariam as regras em silêncio.
- **Consequências:** Regras independentes de fornecedor e modelo. Onde D-001 a D-004 citam `CLAUDE.md`, leia-se `AGENTS.md`. O import na extensão do VS Code não consta na documentação consultada e deve ser verificado com `/memory`.
- **Nota (2026-11-04):** O import `@AGENTS.md` foi verificado na extensão do VS Code em sessão nova: o agente respondeu sobre a regra de commit e push, citando a seção 4 do `AGENTS.md`, sem ler arquivos. Plano de contingência (duplicar regras em `CLAUDE.md`) não necessário. Verificação no CLI não realizada.
