from pathlib import Path


def project_root() -> Path:
    """Return the Decision_tree project root."""
    return Path(__file__).resolve().parents[2]


def ensure_dir(path: Path) -> None:
    """Create directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)
