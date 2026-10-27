# Arquitetura RAG (Retrieval-Augmented Generation)

## Objetivo

Permitir que agentes de IA recuperem conhecimento do projeto (memória, decisões, análises, código, datasheets) sob demanda, em vez de carregar tudo no contexto. Benefícios: menor custo de tokens, respostas ancoradas em fontes citáveis, contexto que sobrevive entre sessões e ferramentas.

## Visão geral

```
            ┌───────────── INGESTÃO (offline, python rag/ingest.py) ─────────────┐
            │                                                                     │
 Fontes ──► Carregamento ──► Limpeza ──► Chunking ──► Metadados ──► Indexação ──► rag/index.db
 .ai/ docs/ history.md          (por tipo)    (por heading /      (path, seção,    (SQLite FTS5,
 src/ datasheets (.md/.txt)                    função / janela)    tipo, data)       BM25)
            │                                                                     │
            └─────────────────────────────────────────────────────────────────────┘

            ┌───────────── CONSULTA (online, python rag/query.py "...") ──────────┐
 Pergunta ──► Reescrita/expansão ──► Busca BM25 (+ vetorial, opcional) ──► Fusão  │
            │   de consulta              top-k candidatos                   (RRF)  │
            │                                     │                               │
            │                              Reranking (opcional) ──► Top-N chunks  │
            │                                     │                               │
            │        Montagem do contexto com citações ──► Prompt ──► LLM ──► Resposta com fontes
            └─────────────────────────────────────────────────────────────────────┘
```

## Camadas de memória

| Nível | Conteúdo | Como chega ao modelo |
|---|---|---|
| 0 — Regras | `CLAUDE.md` | Sempre no contexto (carregado automaticamente) |
| 1 — Memória de trabalho | `.ai/memory/context.md`, últimas entradas de `history.md` | Lido no início da sessão |
| 2 — Memória de longo prazo | `decisions.md`, `.ai/analyses/`, `.ai/chats/`, `.ai/results/`, `docs/` | Recuperado via RAG |
| 3 — Conhecimento técnico | código-fonte, datasheets, manuais de referência | Recuperado via RAG |

Regra: o que é sempre necessário fica no nível 0–1 e deve ser curto; o resto vai para o RAG.

## Ingestão

**Fontes indexadas** (configurável em `rag/config.json`): Markdown, texto, código (`.py .ts .tsx .js .c .h .cpp .hpp .rs .go`), YAML/JSON de configuração. Datasheets em PDF devem ser convertidos para Markdown antes (ex.: `pdftotext -layout` ou `marker`) e salvos em `docs/datasheets/`.

**Chunking**

| Tipo | Estratégia | Motivo |
|---|---|---|
| Markdown | por heading (`#`, `##`, `###`), mantendo o caminho de títulos como prefixo | preserva a unidade semântica e dá contexto ao trecho |
| Código | janelas de ~60 linhas com sobreposição de 10, quebrando preferencialmente em linha em branco | evita cortar funções no meio |
| Seções longas | subdivididas em ~1.500 caracteres com sobreposição | mantém chunks dentro do orçamento de contexto |

Cada chunk recebe metadados: `path`, `section` (caminho de headings), `kind` (memory, history, analysis, doc, code, datasheet), `mtime`.

**Contextualização de chunks** (recomendada): prefixar cada chunk com uma linha descrevendo onde ele está (`Arquivo: docs/x.md > Seção > Subseção`). Técnica simples que melhora muito a recuperação, pois trechos isolados perdem referência ("ele", "esta função").

## Recuperação

1. **Lexical (BM25 via FTS5)** — implementada. Excelente para identificadores, nomes de registradores, códigos de erro, nomes de funções.
2. **Vetorial (embeddings)** — opcional. Melhor para perguntas conceituais e sinônimos. Sugestões: `sentence-transformers` local (ex.: modelos multilíngues como `multilingual-e5`) ou API de embeddings; armazenar em `sqlite-vec`, Chroma ou pgvector.
3. **Híbrida** — combinar as duas listas com *Reciprocal Rank Fusion*: `score = Σ 1/(60 + rank)`.
4. **Reranking** — opcional: reordenar top-30 com cross-encoder ou com o próprio LLM, mantendo top-5 a top-8.
5. **Boost por tipo** — `decisions` e `context` recebem peso maior que `chats` antigos; decisões com status "Substituída" são penalizadas.

## Geração

Modelo de prompt para respostas com RAG (já gerado por `rag/query.py --prompt`):

```
<documentos>
  <documento indice="1" fonte="docs/x.md > Seção">...</documento>
  ...
</documentos>

<pergunta>...</pergunta>

Responda usando apenas os documentos acima. Cite as fontes no formato [n].
Se os documentos não contiverem a resposta, diga explicitamente que a
informação não foi encontrada no projeto.
```

Documentos antes da pergunta, citações obrigatórias e permissão explícita para "não encontrado" são as três práticas de maior impacto contra alucinação.

## Manutenção

- Reindexar ao fim de cada sessão (`session-end.md`) ou via hook `post-commit`.
- `rag/index.db` é artefato gerado: listado no `.gitignore`.
- Avaliação: manter `rag/eval.json` com 10–20 perguntas e o arquivo esperado; medir *hit rate@5* após mudanças no chunking.

## Evolução

| Fase | Quando | O que adicionar |
|---|---|---|
| 1 | início (atual) | BM25 local, Markdown + código |
| 2 | > ~500 chunks ou perguntas conceituais falhando | embeddings + busca híbrida |
| 3 | múltiplos agentes/ferramentas | expor o RAG como servidor MCP (ferramenta `search_project`) |
| 4 | base grande | reranking, filtros por metadados, avaliação contínua |
