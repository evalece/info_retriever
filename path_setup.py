"""Ensure the repository root is on sys.path so imports like `config.BEIR` work."""
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent


def ensure_project_root_on_path() -> Path:
    root = str(_REPO_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)
    return _REPO_ROOT
