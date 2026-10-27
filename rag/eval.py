#!/usr/bin/env python3
"""Mede hit rate@k do RAG usando rag/eval.json. Uso: python rag/eval.py [-k 5]"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from query import IndexNotFound, search  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("-k", type=int, default=5)
k = ap.parse_args().k
cases = json.loads((Path(__file__).parent / "eval.json").read_text(encoding="utf-8"))
if not cases:
    sys.exit("eval.json vazio: adicione casos {question, expected_path}.")
hits = 0
for c in cases:
    try:
        paths = [r["path"] for r in search(c["question"], k)]
    except IndexNotFound as e:
        sys.exit(str(e))
    ok = c["expected_path"] in paths
    hits += ok
    print(f"{'OK  ' if ok else 'FAIL'} {c['question']}  ->  {paths[:3]}")
print(f"\nhit rate@{k}: {hits}/{len(cases)} = {hits / len(cases):.0%}")
