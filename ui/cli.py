"""
cli.py — Interactive CLI input collector for NDA Generator.
"""
from datetime import date

RELATIONSHIP_TYPES = [
    "Technology Partnership",
    "Vendor / Supplier",
    "Employment",
    "Investor / Funding",
    "Merger / Acquisition",
    "Other",
]

CONFIDENTIAL_INFO_OPTIONS = {
    "1": "Technical (source code, algorithms, architecture)",
    "2": "Financial (projections, budgets, revenue data)",
    "3": "Business (strategies, plans, market research)",
    "4": "Customer Data (names, contacts, purchase history)",
    "5": "Legal (contracts, IP filings, compliance docs)",
    "6": "Other",
}


def _prompt(label: str, required: bool = True) -> str:
    while True:
        val = input(f"  {label}: ").strip()
        if val or not required:
            return val
        print("    ⚠  This field is required. Please enter a value.")


def _choose_from_list(label: str, options: list[str]) -> str:
    print(f"\n  {label}:")
    for i, opt in enumerate(options, 1):
        print(f"    [{i}] {opt}")
    while True:
        choice = input("  Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"    ⚠  Please enter a number between 1 and {len(options)}.")


def _choose_multiple(label: str, options: dict[str, str]) -> list[str]:
    print(f"\n  {label} (comma-separated numbers, e.g. 1,3):")
    for key, val in options.items():
        print(f"    [{key}] {val}")
    while True:
        raw = input("  Enter choices: ").strip()
        selected_keys = [k.strip() for k in raw.split(",") if k.strip() in options]
        if selected_keys:
            return [options[k] for k in selected_keys]
        print("    ⚠  Please select at least one valid option.")


def collect_inputs() -> dict:
    """
    Run the interactive CLI to collect all NDA inputs from the user.
    Returns a dict compatible with build_context_from_dict().
    """
    print("\n" + "=" * 60)
    print("  NDA GENERATOR — Input Collection")
    print("=" * 60)
    print("  Please provide the following details.\n")

    disclosing_party = _prompt("Disclosing Party Name (e.g. TechCorp Inc.)")
    receiving_party  = _prompt("Receiving Party Name (e.g. DataSolutions Ltd.)")

    relationship_type = _choose_from_list("Relationship Type", RELATIONSHIP_TYPES)

    # inside collect_inputs(), after receiving_party line:
    print()
    use_today = input("  Use today's date as Effective Date? [Y/n]: ").strip().lower()
    if use_today in ("", "y", "yes"):
        effective_date = date.today().strftime("%B %d, %Y")
    else:
        effective_date = _prompt("Effective Date (e.g. May 1, 2026)")

    print()
    purpose = _prompt("Purpose of this NDA (describe in 1–2 sentences)")

    confidential_types = _choose_multiple(
        "Types of Confidential Information", CONFIDENTIAL_INFO_OPTIONS
    )

    print()
    duration     = _prompt("Confidentiality Duration (e.g. 3 years)")
    governing_law = _prompt("Governing Law / Country (e.g. India)")
    industry     = _prompt("Industry (e.g. Software and Technology)")

    # Build parties string and confidential_info string (compatible with existing NDAContext)
    parties = f"{disclosing_party} (Disclosing Party) and {receiving_party} (Receiving Party)"
    confidential_info = "; ".join(confidential_types)

    data = {
        # Flat fields for NDAContext compatibility
        "parties": parties,
        "purpose": purpose,
        "confidential_info": confidential_info,
        "duration": duration,
        "governing_law": governing_law,
        "industry": industry,
        # Extended fields (available in state for richer prompts)
        "disclosing_party": disclosing_party,
        "receiving_party": receiving_party,
        "relationship_type": relationship_type,
        "effective_date": effective_date,
        "confidential_info_types": confidential_types,
    }

    print("\n" + "-" * 60)
    print("  ✅ Inputs collected. Summary:")
    print(f"     Parties:       {parties}")
    print(f"     Relationship:  {relationship_type}")
    print(f"     Purpose:       {purpose[:70]}{'...' if len(purpose) > 70 else ''}")
    print(f"     Info Types:    {', '.join(confidential_types)}")
    print(f"     Duration:      {duration}")
    print(f"     Governing Law: {governing_law}")
    print(f"     Industry:      {industry}")
    print("-" * 60 + "\n")

    return data