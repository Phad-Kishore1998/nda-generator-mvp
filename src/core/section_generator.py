"""
section_generator.py — Generates a single NDA section using ChatHuggingFace.
"""

import os
from pathlib import Path
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from src.graph.state import NDAContext
from src.utils.cleaner import clean_section
from datetime import date

DEFAULT_MODEL = "meta-llama/Llama-3.1-8B-Instruct"
PROMPT_TEMPLATE_PATH = Path(__file__).parent.parent.parent / "prompts" / "section_prompt.txt"
DRAFTS_DIR = Path(__file__).parent.parent.parent / "outputs" / "drafts"


def _load_prompt_template() -> str:
    with open(PROMPT_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def _build_prompt(section_id: int, section_title: str, section_description: str, context: NDAContext) -> str:
    template = _load_prompt_template()

    # Use extended fields if available, fall back to parsing from parties string
    disclosing_party = context.get("disclosing_party") or context["parties"].split(" and ")[0].replace("(Disclosing Party)", "").strip()
    receiving_party  = context.get("receiving_party")  or context["parties"].split(" and ")[-1].replace("(Receiving Party)", "").strip()
    relationship_type = context.get("relationship_type") or "Business"

    prompt = template.format(
        section_number=section_id,
        section_title=section_title,
        section_title_upper=section_title.upper(),
        disclosing_party=disclosing_party,
        receiving_party=receiving_party,
        relationship_type=relationship_type,
        purpose=context["purpose"],
        confidential_info=context["confidential_info"],
        duration=context["duration"],
        governing_law=context["governing_law"],
        industry=context["industry"],
        section_description=section_description,
        effective_date=context.get("effective_date", date.today().strftime("%B %d, %Y")),
    )

    return prompt


def generate_section(
    section_id: int,
    section_title: str,
    section_description: str,
    context: NDAContext,
) -> str:
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not token:
        raise RuntimeError("HUGGINGFACEHUB_API_TOKEN is not set in your .env file.")

    model_id = os.getenv("HF_MODEL_ID", DEFAULT_MODEL)

    # prompt = _build_prompt(section_title, section_description, context)
    prompt = _build_prompt(section_id, section_title, section_description, context)

    print(f"  → Generating Section {section_id}: {section_title}")

    try:
        llm = HuggingFaceEndpoint(
            repo_id=model_id,
            temperature=0.3,
            max_new_tokens=1200,
            huggingfacehub_api_token=token,
        )
        model = ChatHuggingFace(llm=llm)
        response = model.invoke([HumanMessage(content=prompt)])
        generated_text = clean_section(response.content.strip())
        # generated_text = response.content.strip()

    except Exception as e:
        raise RuntimeError(f"HuggingFace API call failed for section {section_id}: {e}") from e

    output_path = _save_draft(section_id, generated_text)
    print(f"  ✓ Section {section_id} saved → {output_path}")
    return output_path


def _save_draft(section_id: int, content: str) -> str:
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    file_path = DRAFTS_DIR / f"section_{section_id}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return str(file_path)