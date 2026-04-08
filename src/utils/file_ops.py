"""
file_ops.py — Utility functions for file and directory operations.
"""

from pathlib import Path


def ensure_dirs(*paths: str) -> None:
    """Create directories if they don't already exist."""
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)


def clean_drafts(drafts_dir: str) -> None:
    """
    Delete all section draft files from the drafts directory.
    Useful for fresh re-runs.

    Args:
        drafts_dir: Path to the drafts directory.
    """
    d = Path(drafts_dir)
    if d.exists():
        for f in d.glob("section_*.txt"):
            f.unlink()
        print(f"🗑️  Cleaned drafts in {drafts_dir}")


def read_file(path: str) -> str:
    """Read and return the content of a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    """Write content to a text file, creating parent dirs as needed."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)


def section_draft_exists(drafts_dir: str, section_id: int) -> bool:
    """Check if a section draft file already exists."""
    return (Path(drafts_dir) / f"section_{section_id}.txt").exists()
