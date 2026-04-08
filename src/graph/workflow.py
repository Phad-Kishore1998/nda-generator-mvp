"""
workflow.py — Builds and compiles the LangGraph workflow for NDA generation.

Graph structure:
  START
    ↓
  [section_1 ... section_7]  ← run in parallel (fan-out from START)
    ↓
  merge_node
    ↓
  END
"""

from langgraph.graph import StateGraph, START, END
from src.graph.state import NDAContext
from src.graph.nodes import SECTION_NODES, merge_node
from src.config.sections import NDA_SECTIONS


def build_workflow():
    """
    Build and compile the LangGraph StateGraph for NDA generation.

    Returns:
        A compiled LangGraph workflow ready to invoke.
    """
    graph = StateGraph(NDAContext)

    # ── Add all section nodes ──────────────────────────────────────────────
    for section in NDA_SECTIONS:
        node_name = f"section_{section['id']}"
        graph.add_node(node_name, SECTION_NODES[node_name])

    # ── Add the merge node ─────────────────────────────────────────────────
    graph.add_node("merge", merge_node)

    # ── Fan-out: START → all section nodes (parallel) ─────────────────────
    for section in NDA_SECTIONS:
        graph.add_edge(START, f"section_{section['id']}")

    # ── Fan-in: all section nodes → merge ─────────────────────────────────
    for section in NDA_SECTIONS:
        graph.add_edge(f"section_{section['id']}", "merge")

    # ── merge → END ───────────────────────────────────────────────────────
    graph.add_edge("merge", END)

    return graph.compile()
