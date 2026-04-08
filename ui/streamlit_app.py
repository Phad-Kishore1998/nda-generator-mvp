"""
streamlit_app.py — Streamlit UI for NDA Generator MVP.
Run with: streamlit run ui/streamlit_app.py
"""

import streamlit as st
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.context_builder import build_context_from_dict
from src.graph.workflow import build_workflow
from datetime import date as dt


RELATIONSHIP_TYPES = [
    "Technology Partnership",
    "Vendor / Supplier",
    "Employment",
    "Investor / Funding",
    "Merger / Acquisition",
    "Other",
]

CONFIDENTIAL_INFO_OPTIONS = [
    "Technical (source code, algorithms, architecture)",
    "Financial (projections, budgets, revenue data)",
    "Business (strategies, plans, market research)",
    "Customer Data (names, contacts, purchase history)",
    "Legal (contracts, IP filings, compliance docs)",
    "Other",
]


def main():
    st.set_page_config(page_title="NDA Generator", page_icon="📄", layout="centered")

    st.title("📄 NDA Generator")
    st.caption("AI-powered Non-Disclosure Agreement generator. Fill in the details below.")
    st.divider()

    with st.form("nda_form"):
        st.subheader("🏢 Parties")
        col1, col2 = st.columns(2)
        with col1:
            disclosing_party = st.text_input("Disclosing Party", placeholder="TechCorp Inc.")
        with col2:
            receiving_party = st.text_input("Receiving Party", placeholder="DataSolutions Ltd.")

        relationship_type = st.selectbox("Relationship Type", RELATIONSHIP_TYPES)

        st.subheader("📋 Agreement Details")
        purpose = st.text_area(
            "Purpose of this NDA",
            placeholder="e.g. Evaluating a potential technology partnership for a joint AI analytics platform",
            height=80,
        )

        confidential_types = st.multiselect(
            "Types of Confidential Information",
            CONFIDENTIAL_INFO_OPTIONS,
            default=["Technical (source code, algorithms, architecture)"],
        )

        col3, col4, col5 = st.columns(3)
        with col3:
            duration = st.text_input("Duration", placeholder="3 years")
        with col4:
            governing_law = st.text_input("Governing Law", placeholder="India")
        with col5:
            industry = st.text_input("Industry", placeholder="Software and Technology")

        submitted = st.form_submit_button("⚡ Generate NDA", use_container_width=True, type="primary")

    if submitted:
        # Validate
        missing = []
        if not disclosing_party: missing.append("Disclosing Party")
        if not receiving_party:  missing.append("Receiving Party")
        if not purpose:          missing.append("Purpose")
        if not confidential_types: missing.append("Confidential Info Types")
        if not duration:         missing.append("Duration")
        if not governing_law:    missing.append("Governing Law")
        if not industry:         missing.append("Industry")

        if missing:
            st.error(f"Please fill in: {', '.join(missing)}")
            return

        parties = f"{disclosing_party} (Disclosing Party) and {receiving_party} (Receiving Party)"
        confidential_info = "; ".join(confidential_types)

        data = {
            "parties": parties,
            "purpose": purpose,
            "confidential_info": confidential_info,
            "duration": duration,
            "governing_law": governing_law,
            "industry": industry,
            "disclosing_party": disclosing_party,
            "receiving_party": receiving_party,
            "relationship_type": relationship_type,
            "confidential_info_types": confidential_types,
        }

        context = build_context_from_dict(data)
        workflow = build_workflow()

        progress = st.progress(0, text="Starting generation...")
        status   = st.status("Generating NDA sections...", expanded=True)

        with status:
            for i in range(1, 8):
                st.write(f"✍️  Generating Section {i}...")
                progress.progress(i * 12, text=f"Section {i}/7...")

        final_state = workflow.invoke(context)
        progress.progress(100, text="Done!")

        errors = final_state.get("errors", [])
        final_path = final_state.get("final_document_path")

        if errors:
            st.warning(f"{len(errors)} section(s) had errors during generation.")
            for e in errors:
                st.caption(f"• {e}")

        if final_path and Path(final_path).exists():
            status.update(label="✅ NDA Generated!", state="complete")
            st.success("Your NDA document is ready.")

            content = Path(final_path).read_text(encoding="utf-8")
            st.download_button(
                label="⬇️ Download NDA (.txt)",
                data=content,
                file_name="nda_final.txt",
                mime="text/plain",
                use_container_width=True,
            )
            with st.expander("👁️ Preview Document"):
                st.text(content)
        else:
            status.update(label="❌ Generation failed", state="error")
            st.error("Document could not be produced. Check errors above.")


if __name__ == "__main__":
    main()