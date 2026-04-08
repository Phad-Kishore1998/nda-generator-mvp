"""
context_builder.py — Converts raw user input dict into a validated NDAContext.
"""

import json
from pathlib import Path
from src.graph.state import NDAContext
from datetime import date


REQUIRED_FIELDS = [
    "parties",
    "purpose",
    "confidential_info",
    "duration",
    "governing_law",
    "industry",
]


def build_context_from_file(input_path: str) -> NDAContext:
    """
    Load user input from a JSON file and return a populated NDAContext.

    Args:
        input_path: Path to the input JSON file.

    Returns:
        NDAContext dict with all fields populated.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If required fields are missing from the input.
    """
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return build_context_from_dict(data)


def build_context_from_dict(data: dict) -> NDAContext:
    """
    Build NDAContext from a raw dictionary.

    Args:
        data: Dictionary with user-provided NDA inputs.

    Returns:
        NDAContext dict.

    Raises:
        ValueError: If required fields are missing.
    """
    missing = [field for field in REQUIRED_FIELDS if not data.get(field)]
    if missing:
        raise ValueError(f"Missing required fields in input: {missing}")

    context: NDAContext = {
        "parties": data["parties"].strip(),
        "purpose": data["purpose"].strip(),
        "confidential_info": data["confidential_info"].strip(),
        "duration": data["duration"].strip(),
        "governing_law": data["governing_law"].strip(),
        "industry": data["industry"].strip(),
        # Optional extended fields (present when using CLI/UI)
        "disclosing_party": data.get("disclosing_party", "").strip(),
        "receiving_party":  data.get("receiving_party", "").strip(),
        "relationship_type": data.get("relationship_type", "").strip(),
        # In build_context_from_dict(), after the other optional fields:
        "effective_date": data.get("effective_date") or date.today().strftime("%B %d, %Y"),
        "confidential_info_types": data.get("confidential_info_types", []),
        "sections_completed": [],
        "errors": [],
        "final_document_path": None,
    }

    return context
