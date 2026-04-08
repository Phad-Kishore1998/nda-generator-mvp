

---

# 📄 **README — NDA Generator (MVP v1: Structured + UI Enabled)**

## 🚀 Overview

This project builds an AI-powered system that generates a **multi-section NDA document** from structured user inputs.

The MVP focuses on:

* ✅ A **basic UI / CLI input layer**
* ✅ **Structured NDAContext** (not raw text)
* ✅ **Parallel section generation**
* ✅ **Clean, readable NDA output**

⚠️ This is still an MVP — not a legally validated system.

---

## 🎯 Problem Statement

Users provide key NDA details via a structured interface:

* Parties involved
* Relationship type
* Purpose of NDA
* Type of confidential information
* Confidentiality duration
* Governing law
* Industry

The system generates:

* A structured NDA with **7 sections**
* Consistent naming and context
* Reduced repetition and generic text
* A merged final document saved locally

---

## 🧠 MVP Design Philosophy

* ✅ Structured input → better output
* ✅ Keep system simple but meaningful
* ✅ Avoid garbage generation
* ❌ No heavy validation (yet)
* ❌ No complex orchestration logic

> LLM writes content, system controls structure + inputs.

---

# 🏗️ High-Level Architecture

```text
UI / CLI Input
    ↓
Structured NDAContext
    ↓
LangGraph Workflow
    ↓
Parallel Section Generation (7 nodes)
    ↓
Draft Files (clean sections)
    ↓
Merge Step
    ↓
Final NDA Document
    ↓
Saved Output (.txt / .docx)
```

---

# 🧩 Core Components

---

## 1. Input Layer (UI / CLI)

Basic interface to collect structured data.

### Example Input Fields

```text
Disclosing Party Name:
Receiving Party Name:
Relationship Type: (Partnership / Vendor / Employment / Other)

Purpose of NDA:

Type of Confidential Information:
[ ] Technical
[ ] Financial
[ ] Business
[ ] Customer Data
[ ] Other

Confidentiality Duration:
Governing Law (Country):
Industry:
```

---

## 2. NDAContext (Structured State)

Single source of truth used across all LLM calls.

```json
{
  "disclosing_party": "TechCorp Inc.",
  "receiving_party": "DataSolutions Ltd.",
  "relationship_type": "Technology Partnership",
  "purpose": "Evaluation of joint AI analytics platform",
  "confidential_info_types": ["technical", "business"],
  "duration": "3 years",
  "governing_law": "India",
  "industry": "Technology"
}
```

---

## 3. Section List (Fixed for MVP)

The NDA is divided into 7 sections:

1. Purpose, Parties, and Context
2. Definition of Confidential Information
3. Categories and Scope
4. Obligations of Receiving Party
5. Permitted Disclosures and Exceptions
6. Breach and Remedies
7. Miscellaneous and Legal Terms

---

## 4. Section Generation Strategy

Each section:

* Uses the same NDAContext
* Generated independently
* Produces ~500–800 words
* Uses:

  * Formal legal tone
  * Numbered clauses (e.g., 4.1, 4.2)
* Avoids repetition via prompt constraints

---

## 5. Parallel Execution (LangGraph)

* Each section is a node
* All nodes run in parallel
* Shared state is read-only
* Each node writes output to file

---

## 6. Synchronization

* Wait until all 7 sections are generated
* Then trigger merge step

---

## 7. Merge Step

* Read all section files
* Combine in correct order
* Produce final NDA document

---

## 8. Export

* Default: `.txt`
* Optional: `.docx` (future)

---

# 🗂️ Project Structure

```text
nda-generator-mvp/
│
├── README.md
├── .env
├── requirements.txt
│
├── inputs/
│   └── sample.json
│
├── outputs/
│   ├── drafts/
│   │   ├── section_1.txt
│   │   ├── section_2.txt
│   │   └── ...
│   │
│   └── final/
│       └── nda_final.txt
│
├── ui/
│   ├── cli.py              # CLI input handler
│   └── streamlit_app.py   # Optional UI
│
├── prompts/
│   └── section_prompt.txt
│
├── src/
│   ├── main.py
│   │
│   ├── graph/
│   │   ├── workflow.py
│   │   ├── state.py
│   │   └── nodes.py
│   │
│   ├── core/
│   │   ├── context_builder.py
│   │   ├── section_generator.py
│   │   ├── merger.py
│   │   └── exporter.py
│   │
│   ├── utils/
│   │   ├── file_ops.py
│   │   └── cleaner.py     # basic repetition cleanup
│   │
│   └── config/
│       └── sections.py
│
└── tests/
    └── test_basic_flow.py
```

---

# 🔄 Workflow Design

## Step 1 — Input Collection

* Collect structured input via CLI or UI

---

## Step 2 — Context Builder

* Convert input → NDAContext

---

## Step 3 — Parallel Section Generation

Each node:

```text
Input: NDAContext
Prompt: Section-specific prompt
Output: section_X.txt
```

---

## Step 4 — Wait for Completion

* Ensure all 7 sections exist

---

## Step 5 — Merge

```text
Read → section_1.txt ... section_7.txt
Combine → nda_final.txt
```

---

## Step 6 — Export

* Save final document

---

# ✍️ Prompt Design (Improved MVP)

```text
You are a legal drafting assistant.

Write a professional NDA section.

Section: {section_title}

Context:
- Disclosing Party: {disclosing_party}
- Receiving Party: {receiving_party}
- Relationship: {relationship_type}
- Purpose: {purpose}
- Confidential Info Types: {confidential_info_types}
- Duration: {duration}
- Governing Law: {governing_law}
- Industry: {industry}

Instructions:
- Use formal legal language
- Use numbered clauses (e.g., 4.1, 4.2)
- Avoid repetition
- Do not redefine terms unnecessarily
- Keep content specific to context
- Write 500–800 words

Output only the section content.
```

---

# 🧹 Basic Cleanup Layer (MVP)

Before saving each section:

* Remove duplicate paragraphs
* Trim repeated phrases

(No heavy validation yet)

---

# ⚙️ Tech Stack

* **LangGraph** → orchestration
* **HuggingFace API** → LLM calls
* **Python** → core logic
* **Streamlit / CLI** → input layer
* **File system** → storage

---

# ✅ MVP Success Criteria

The system should:

* Accept structured inputs via UI/CLI
* Generate 7 NDA sections
* Use consistent party names
* Reduce repetition vs naive generation
* Merge into a single document
* Save final output locally

---

# ⚠️ Known Limitations

* No cross-section reference validation
* No legal correctness guarantee
* Still not full 20-page depth
* Possible minor repetition

---

# 🔜 Future Improvements

* Section registry + dependencies
* Cross-reference validation
* Name consistency checker
* Legal refinement layer
* Token scaling (15–20 pages)
* PDF formatting
* Structured outputs (JSON → rendering)

---

# 🚀 Execution Plan

## Step 1

Build CLI / Streamlit UI

## Step 2

Define NDAContext schema

## Step 3

Write improved prompt template

## Step 4

Implement section generator (HF API)

## Step 5

Build LangGraph workflow

## Step 6

Save draft sections

## Step 7

Merge sections

## Step 8

Export final document

---



---


**To run:**
```bash
pip install -r requirements.txt
# Add HUGGINGFACEHUB_API_TOKEN to .env
python -m src.main

python -m src.main --interactive
```