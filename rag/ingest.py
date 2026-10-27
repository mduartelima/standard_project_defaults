#!/usr/bin/env python3
"""Indexa a base de conhecimento do projeto em SQLite FTS5 (BM25).

Uso:
    python rag/ingest.py            # reindexa tudo
    python rag/ingest.py --stats    # reindexa e mostra estatísticas
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((Path(__file__).parent / "config.json").read_text(encoding="utf-8"))
DB_PATH = Path(__file__).parent / "index.db"

HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
CODE_EXT = {".py", ".ts", ".tsx", ".js", ".jsx", ".c", ".h", ".cpp", ".hpp", ".rs", ".go", ".ld", ".dts", ".overlay"}


def classify(rel: str) -> str:
    """Define o tipo do documento a partir do caminho (usado para boost)."""
    if rel.endswith("decisions.md"):
        return "decision"
    if rel.startswith(".ai/memory/"):
        return "memory"
    if rel == "history.md":
        return "history"
    if rel.startswith(".ai/analyses/"):
        return "analysis"
    if rel.startswith(".ai/results/"):
        return "result"
    if rel.startswith(".ai/chats/"):
        return "chat"
    if "datasheet" in rel.lower():
        return "datasheet"
    if Path(rel).suffix in CODE_EXT:
        return "code"
    return "doc"


def split_long(text: str, size: int) -> list[str]:
    """Divide texto longo em blocos de ~size caracteres, quebrando em parágrafos."""
    if len(text) <= size:
        return [text]
    parts, buf = [], ""
    for para in re.split(r"\n\s*\n", text):
        if buf and len(buf) + len(para) + 2 > size:
            parts.append(buf)
            buf = buf[-200:] + "\n\n" + para  # pequena sobreposição
        else:
            buf = f"{buf}\n\n{para}" if buf else para
    if buf:
        parts.append(buf)
    return parts


def chunk_markdown(text: str) -> list[tuple[str, str, int]]:
    """Chunk por heading. Retorna (caminho_de_seções, conteúdo, linha_inicial)."""
    chunks, stack, buf, start, in_fence = [], [], [], 1, False

    def flush():
        body = "\n".join(buf).strip()
        if body:
            section = " > ".join(t for _, t in stack)
            for part in split_long(body, CONFIG["chunk_chars"]):
                chunks.append((section, part, start))

    for i, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else HEADING.match(line)
        if m:
            flush()
            level = len(m.group(1))
            stack = [(lv, t) for lv, t in stack if lv < level] + [(level, m.group(2))]
            buf, start = [], i
        else:
            buf.append(line)
    flush()
    return chunks


def chunk_code(text: str) -> list[tuple[str, str, int]]:
    """Janelas de linhas com sobreposição, preferindo quebrar em linhas em branco."""
    lines = text.splitlines()
    win, ov = CONFIG["code_window_lines"], CONFIG["code_overlap_lines"]
    chunks, i = [], 0
    while i < len(lines):
        end = min(i + win, len(lines))
        if end < len(lines):  # recua até uma linha em branco, se houver perto
            for j in range(end, max(i + win // 2, end - 15), -1):
                if not lines[j - 1].strip():
                    end = j
                    break
        body = "\n".join(lines[i:end]).strip()
        if body:
            chunks.append((f"linhas {i + 1}-{end}", body, i + 1))
        if end >= len(lines):
            break
        i = max(end - ov, i + 1)
    return chunks


def iter_files():
    seen = set()
    for root in CONFIG["roots"]:
        p = ROOT / root
        if not p.exists():
            continue
        files = [p] if p.is_file() else p.rglob("*")
        for f in files:
            if not f.is_file() or f in seen:
                continue
            if any(part in CONFIG["exclude_dirs"] for part in f.relative_to(ROOT).parts):
                continue
            if f.name in CONFIG["exclude_files"]:
                continue
            if f.suffix.lower() not in CONFIG["extensions"] and f.name not in CONFIG.get("include_files", []):
                continue
            if f.stat().st_size > CONFIG["max_file_kb"] * 1024:
                continue
            seen.add(f)
            yield f


def build() -> dict:
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    con.execute(
        "CREATE VIRTUAL TABLE chunks USING fts5("
        "content, section, path UNINDEXED, kind UNINDEXED, line UNINDEXED, mtime UNINDEXED, "
        "tokenize='unicode61 remove_diacritics 2')"
    )
    stats = {"files": 0, "chunks": 0, "by_kind": {}}
    for f in iter_files():
        rel = f.relative_to(ROOT).as_posix()
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        kind = classify(rel)
        is_code = f.suffix in CODE_EXT
        pieces = chunk_code(text) if is_code else chunk_markdown(text)
        for section, body, line in pieces:
            # Contextualização: o prefixo com arquivo e seção também é indexado.
            header = f"Arquivo: {rel}" + (f" > {section}" if section else "")
            con.execute(
                "INSERT INTO chunks VALUES (?,?,?,?,?,?)",
                (f"{header}\n{body}", section, rel, kind, line, int(f.stat().st_mtime)),
            )
            stats["chunks"] += 1
            stats["by_kind"][kind] = stats["by_kind"].get(kind, 0) + 1
        stats["files"] += 1
    con.commit()
    con.close()
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stats", action="store_true", help="exibe estatísticas por tipo")
    args = ap.parse_args()
    t0 = time.time()
    s = build()
    print(f"Indexados {s['files']} arquivos em {s['chunks']} chunks ({time.time() - t0:.2f}s) -> {DB_PATH.relative_to(ROOT)}")
    if args.stats:
        for k, v in sorted(s["by_kind"].items(), key=lambda x: -x[1]):
            print(f"  {k:<10} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
