"""
merger.py — Reads all section draft files and merges them into a single NDA document.
"""

from pathlib import Path
from datetime import date


DRAFTS_DIR = Path(__file__).parent.parent.parent / "outputs" / "drafts"
FINAL_DIR = Path(__file__).parent.parent.parent / "outputs" / "final"
FINAL_FILE_TXT = FINAL_DIR / "nda_final.txt"


def merge_sections(total_sections: int = 7) -> str:
    """
    Read all section draft files in order and merge into a single NDA document.

    Args:
        total_sections: Total number of sections to merge (default 7).

    Returns:
        Path to the merged final document.

    Raises:
        FileNotFoundError: If any section draft file is missing.
    """
    FINAL_DIR.mkdir(parents=True, exist_ok=True)

    # Verify all sections exist before merging
    missing = []
    for i in range(1, total_sections + 1):
        path = DRAFTS_DIR / f"section_{i}.txt"
        if not path.exists():
            missing.append(i)

    if missing:
        raise FileNotFoundError(
            f"Cannot merge — the following section drafts are missing: {missing}"
        )

    print("\n📎 Merging all sections into final document...")

    lines = []

    # Document header
    lines.append("=" * 80)
    lines.append("NON-DISCLOSURE AGREEMENT")
    lines.append(f"Generated on: {date.today().strftime('%B %d, %Y')}")
    lines.append("=" * 80)
    lines.append("")
    lines.append(
        "NOTICE: This document is AI-generated for evaluation purposes only. "
        "It does not constitute legal advice. Consult a qualified legal professional "
        "before using this document for any binding legal purpose."
    )
    lines.append("")
    lines.append("=" * 80)
    lines.append("")

    # Append each section
    for i in range(1, total_sections + 1):
        path = DRAFTS_DIR / f"section_{i}.txt"
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        lines.append(content)
        lines.append("")
        lines.append("-" * 80)
        lines.append("")

    # Signature block
    lines.append("SIGNATURE PAGE")
    lines.append("")
    lines.append("IN WITNESS WHEREOF, the Parties have executed this Agreement as of the date first written above.")
    lines.append("")
    lines.append("DISCLOSING PARTY:")
    lines.append("")
    lines.append("Signature: _______________________________")
    lines.append("Name:      _______________________________")
    lines.append("Title:     _______________________________")
    lines.append("Date:      _______________________________")
    lines.append("")
    lines.append("RECEIVING PARTY:")
    lines.append("")
    lines.append("Signature: _______________________________")
    lines.append("Name:      _______________________________")
    lines.append("Title:     _______________________________")
    lines.append("Date:      _______________________________")
    lines.append("")
    lines.append("=" * 80)
    lines.append("END OF AGREEMENT")
    lines.append("=" * 80)

    final_content = "\n".join(lines)

    with open(FINAL_FILE_TXT, "w", encoding="utf-8") as f:
        f.write(final_content)

    print(f"✅ Final NDA document saved → {FINAL_FILE_TXT}")
    return str(FINAL_FILE_TXT)
