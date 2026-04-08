"""
cleaner.py — Basic post-processing cleanup for generated NDA sections.
Removes obvious duplicate paragraphs and trims excessive whitespace.
"""

import re


def clean_section(text: str) -> str:
    """
    Apply basic cleanup to a generated section:
    - Normalize whitespace
    - Remove duplicate consecutive paragraphs
    - Strip leading/trailing blank lines

    Args:
        text: Raw generated section text.

    Returns:
        Cleaned text.
    """
    # Normalize Windows line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Collapse 3+ blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Split into paragraphs and deduplicate consecutive identical ones
    paragraphs = text.split("\n\n")
    deduped = []
    prev = None
    for para in paragraphs:
        normalized = para.strip()
        if normalized and normalized != prev:
            deduped.append(normalized)
            prev = normalized

    return "\n\n".join(deduped).strip()