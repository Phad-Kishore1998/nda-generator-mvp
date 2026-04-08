"""
main.py — Entry point for the NDA Generator MVP.

Usage:
    python -m src.main                          # Uses default sample input
    python -m src.main --input inputs/my.json   # Custom input file
    python -m src.main --export-docx            # Also export as .docx

Environment:
    HUGGINGFACEHUB_API_TOKEN must be set in .env
"""

import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Load .env variables early
load_dotenv()

from src.core.context_builder import build_context_from_file, build_context_from_dict
from src.graph.workflow import build_workflow
from src.core.exporter import export_to_docx


DEFAULT_INPUT = "inputs/sample.json"


def parse_args():
    parser = argparse.ArgumentParser(
        description="NDA Generator MVP — AI-powered NDA document generation"
    )
    parser.add_argument("--input", type=str, default=None,
        help="Path to input JSON file (skips interactive prompt)")
    parser.add_argument("--interactive", action="store_true", default=False,
        help="Collect inputs interactively via CLI prompts")
    parser.add_argument("--export-docx", action="store_true", default=False,
        help="Also export the final NDA as a .docx file")
    return parser.parse_args()


def main():
    args = parse_args()

    print("=" * 60)
    print("  NDA GENERATOR MVP")
    print("=" * 60)
    print(f"\n📂 Input file: {args.input}")

    # ── Step 1: Get inputs ────────────────────────────────────────────────
    if args.interactive or args.input is None:
        # Interactive CLI mode
        from ui.cli import collect_inputs
        raw_data = collect_inputs()
        try:
            context = build_context_from_dict(raw_data)
        except ValueError as e:
            print(f"\n❌ Input error: {e}")
            sys.exit(1)
    else:
        # JSON file mode
        print(f"\n📂 Input file: {args.input}")
        print("\n[1/4] Building NDA context from input...")
        try:
            context = build_context_from_file(args.input)
        except (FileNotFoundError, ValueError) as e:
            print(f"\n❌ Error loading input: {e}")
            sys.exit(1)

    # ── Step 2: Build LangGraph workflow ──────────────────────────────────
    print("\n[2/4] Building LangGraph workflow...")
    workflow = build_workflow()
    print("      ✓ Workflow compiled (7 section nodes + merge node)")

    # ── Step 3: Execute workflow ───────────────────────────────────────────
    print("\n[3/4] Executing NDA generation pipeline...")
    print("      Sections will be generated in parallel.\n")

    final_state = workflow.invoke(context)

    # ── Step 4: Report results ────────────────────────────────────────────
    print("\n[4/4] Pipeline complete.")

    errors = final_state.get("errors", [])
    if errors:
        print(f"\n⚠️  {len(errors)} error(s) occurred during generation:")
        for err in errors:
            print(f"   - {err}")

    final_path = final_state.get("final_document_path")
    if final_path:
        print(f"\n✅ Final NDA document: {final_path}")

        # Optional: export to .docx
        if args.export_docx:
            print("\n📄 Exporting to .docx...")
            try:
                docx_path = export_to_docx(final_path)
                print(f"✅ DOCX saved: {docx_path}")
            except Exception as e:
                print(f"⚠️  DOCX export failed: {e}")
    else:
        print("\n❌ Final document was not produced. Check errors above.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("  DONE")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
