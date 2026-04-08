"""
nodes.py — LangGraph node functions for each NDA section and the merge step.

Each section node:
  - Receives the shared NDAContext state
  - Calls section_generator to produce the section content
  - Returns updated state (with section ID marked complete)

The merge node:
  - Waits for all sections to be flagged as complete
  - Triggers the merger to produce the final document
"""

from src.graph.state import NDAContext
from src.core.section_generator import generate_section
from src.core.merger import merge_sections
from src.config.sections import NDA_SECTIONS


def _make_section_node(section: dict):
    def section_node(state: NDAContext) -> dict:
        section_id = section["id"]
        try:
            generate_section(
                section_id=section_id,
                section_title=section["title"],
                section_description=section["description"],
                context=state,
            )
            # Return ONLY the fields this node updates
            return {"sections_completed": [section_id], "errors": []}
        except Exception as e:
            error_msg = f"Section {section_id} failed: {str(e)}"
            print(f"  ✗ {error_msg}")
            return {"sections_completed": [], "errors": [error_msg]}

    section_node.__name__ = f"section_{section['id']}_node"
    return section_node


def merge_node(state: NDAContext) -> NDAContext:
    """
    LangGraph node that merges all section drafts into the final NDA document.

    Args:
        state: Current NDAContext with sections_completed list.

    Returns:
        Updated state with final_document_path set.
    """
    completed = state.get("sections_completed", [])
    errors = state.get("errors", [])

    if errors:
        print(f"\n⚠️  Warning: {len(errors)} section(s) had errors:")
        for err in errors:
            print(f"   - {err}")

    print(f"\n📋 Sections completed: {sorted(completed)}")

    try:
        final_path = merge_sections(total_sections=len(NDA_SECTIONS))
        return {**state, "final_document_path": final_path}
    except Exception as e:
        error_msg = f"Merge failed: {str(e)}"
        print(f"✗ {error_msg}")
        updated_errors = state.get("errors", []) + [error_msg]
        return {**state, "errors": updated_errors}


# Pre-built node functions for all 7 sections (used in workflow.py)
SECTION_NODES = {
    f"section_{s['id']}": _make_section_node(s)
    for s in NDA_SECTIONS
}
