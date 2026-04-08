from typing import TypedDict, Optional, Annotated
import operator

class NDAContext(TypedDict):
    # Core fields
    parties: str
    purpose: str
    confidential_info: str
    duration: str
    governing_law: str
    industry: str

    # Extended fields from v2 structured input (optional — CLI/UI populates these)
    disclosing_party: Optional[str]
    receiving_party: Optional[str]
    relationship_type: Optional[str]
    confidential_info_types: Optional[list[str]]

    # Tracking
    sections_completed: Annotated[list[int], operator.add]
    errors: Annotated[list[str], operator.add]
    final_document_path: Optional[str]
    effective_date: Optional[str]   # e.g. "April 09, 2026"