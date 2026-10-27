#!/usr/bin/env python3
"""Consulta a base de conhecimento do projeto.

Uso:
    python rag/query.py "como é feita a recepção uart?"
    python rag/query.py "decisão sobre banco de dados" -k 8 --kind decision,memory
    python rag/query.py "pinout do sensor" --prompt   # gera prompt pronto para o LLM
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

DB_PATH = Path(__file__).parent / "index.db"
CONFIG = json.loads((Path(__file__).parent / "config.json").read_text(encoding="utf-8"))

# Palavras sem valor de busca (PT + EN). Reduz ruído no BM25.
STOP = set("""
a o as os um uma uns umas de do da dos das em no na nos nas por para com sem sob sobre e ou
que se como qual quais quando onde porque por que é ser foi são está estão ao aos à às
isso isto esse essa este esta the of to in on for and or is are was be how what which
""".split())


def normalize(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def to_fts_query(q: str) -> str:
    """Converte texto livre em consulta FTS5 segura (termos com OR e prefixo)."""
    tokens = [t for t in re.findall(r"[\w]+", normalize(q)) if t not in STOP and len(t) > 1]
    if not tokens:
        return ""
    return " OR ".join(f'"{t}"*' for t in dict.fromkeys(tokens))


def search(question: str, k: int = 6, kinds: list[str] | None = None) -> list[dict]:
    if not DB_PATH.exists():
        sys.exit("Índice não encontrado. Execute: python rag/ingest.py")
    fts = to_fts_query(question)
    if not fts:
        return []
    con = sqlite3.connect(DB_PATH)
    # bm25(): valores menores = mais relevante. Peso maior para o campo 'section'.
    rows = con.execute(
        "SELECT path, section, kind, line, content, bm25(chunks, 1.0, 2.0) AS score "
        "FROM chunks WHERE chunks MATCH ? ORDER BY score LIMIT ?",
        (fts, k * 5),
    ).fetchall()
    con.close()
    boost = CONFIG.get("kind_boost", {})
    results = []
    for path, section, kind, line, content, score in rows:
        if kinds and kind not in kinds:
            continue
        rel = -score * boost.get(kind, 1.0)
        if kind == "decision" and re.search(r"Status:\*\*\s*Substitu", content):
            rel *= 0.5  # decisões revogadas perdem prioridade
        results.append({"path": path, "section": section, "kind": kind, "line": line,
                        "content": content, "score": round(rel, 3)})
    results.sort(key=lambda r: -r["score"])
    return results[:k]


def as_prompt(question: str, results: list[dict]) -> str:
    docs = "\n".join(
        f'  <documento indice="{i}" fonte="{r["path"]}:{r["line"]}">\n{r["content"]}\n  </documento>'
        for i, r in enumerate(results, 1)
    )
    return (
        f"<documentos>\n{docs}\n</documentos>\n\n"
        f"<pergunta>\n{question}\n</pergunta>\n\n"
        "Responda usando apenas os documentos acima. Cite as fontes no formato [n].\n"
        "Se os documentos não contiverem a resposta, diga explicitamente que a "
        "informação não foi encontrada no projeto."
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("question")
    ap.add_argument("-k", type=int, default=6, help="número de trechos (padrão 6)")
    ap.add_argument("--kind", help="filtrar tipos: decision,memory,history,analysis,result,chat,doc,code,datasheet")
    ap.add_argument("--prompt", action="store_true", help="imprime prompt pronto com contexto")
    ap.add_argument("--json", action="store_true", help="saída JSON (integração com outras ferramentas)")
    args = ap.parse_args()

    kinds = args.kind.split(",") if args.kind else None
    res = search(args.question, args.k, kinds)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif args.prompt:
        print(as_prompt(args.question, res))
    elif not res:
        print("Nenhum trecho encontrado.")
    else:
        for i, r in enumerate(res, 1):
            preview = r["content"].split("\n", 1)[-1].strip().replace("\n", " ")[:220]
            print(f"[{i}] {r['path']}:{r['line']}  ({r['kind']}, score {r['score']})")
            if r["section"]:
                print(f"    § {r['section']}")
            print(f"    {preview}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
