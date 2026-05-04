# Uses BM25 from venv: rank_bm25 (see site-packages/rank_bm25.py).
import sys
from pathlib import Path

# Minimal bootstrap so `path_setup` (at repo root) is importable when this file is run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import path_setup

path_setup.ensure_project_root_on_path()

from rank_bm25 import BM25
from config.BEIR import BEIR

# rank_bm25 expects tokenized corpus (list of list of str) and query tokens; build from BEIR first, e.g.:
# beir = BEIR(dataset_name="scidocs")
# corpus = ...  # tokenize beir.corpus into list[list[str]]
# query = ...   # tokenize one query
# bm25 = BM25(corpus)
# bm25.get_scores(query)
