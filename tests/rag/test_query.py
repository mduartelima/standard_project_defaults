"""Testes do RAG: filtro por tipo, índice ausente e eval com casos vazios.

Executar: python -m unittest discover -s tests/rag -v
"""
import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAG = Path(__file__).resolve().parents[2] / "rag"
sys.path.insert(0, str(RAG))
import query  # noqa: E402


def make_index(path: Path, rows: list[tuple[str, str, str]]) -> None:
    con = sqlite3.connect(path)
    con.execute(
        "CREATE VIRTUAL TABLE chunks USING fts5("
        "content, section, path UNINDEXED, kind UNINDEXED, line UNINDEXED, mtime UNINDEXED, "
        "tokenize='unicode61 remove_diacritics 2')"
    )
    for p, kind, content in rows:
        con.execute("INSERT INTO chunks VALUES (?,?,?,?,?,?)", (content, "", p, kind, 1, 0))
    con.commit()
    con.close()


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / "index.db"
        self._orig = query.DB_PATH
        query.DB_PATH = self.db
        self.addCleanup(setattr, query, "DB_PATH", self._orig)

    def test_missing_index_raises(self):
        with self.assertRaises(query.IndexNotFound):
            query.search("uart")

    def test_kind_filter_finds_rare_kind_beyond_k5_window(self):
        # 40 chunks 'doc' mais relevantes que o único 'decision': com o filtro
        # aplicado após o LIMIT k*5 (=10), o 'decision' seria descartado.
        rows = [(f"d{i}.md", "doc", "uart uart uart uart " * 5) for i in range(40)]
        rows.append(("decisions.md", "decision", "uart"))
        make_index(self.db, rows)
        res = query.search("uart", k=2, kinds=["decision"])
        self.assertEqual([r["path"] for r in res], ["decisions.md"])

    def test_no_filter_returns_k(self):
        make_index(self.db, [(f"d{i}.md", "doc", "uart") for i in range(10)])
        self.assertEqual(len(query.search("uart", k=3)), 3)


class EvalTest(unittest.TestCase):
    def run_eval(self, cases, with_index):
        # Copia rag/ para um diretório temporário para controlar eval.json e o índice.
        with tempfile.TemporaryDirectory() as d:
            dst = Path(d)
            for name in ("eval.py", "query.py", "config.json"):
                (dst / name).write_text((RAG / name).read_text(encoding="utf-8"), encoding="utf-8")
            (dst / "eval.json").write_text(json.dumps(cases), encoding="utf-8")
            if with_index:
                make_index(dst / "index.db", [("a.md", "doc", "uart")])
            return subprocess.run([sys.executable, str(dst / "eval.py")], capture_output=True, text=True)

    def test_empty_cases_exit_cleanly(self):
        r = self.run_eval([], with_index=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("eval.json vazio", r.stderr)
        self.assertNotIn("ZeroDivisionError", r.stderr)

    def test_missing_index_exit_message(self):
        r = self.run_eval([{"question": "uart", "expected_path": "a.md"}], with_index=False)
        self.assertIn("ingest.py", r.stderr)
        self.assertNotIn("Traceback", r.stderr)


if __name__ == "__main__":
    unittest.main()
