"""
test_basic_flow.py — Basic tests for the NDA Generator MVP pipeline.

Run with:
    pytest tests/test_basic_flow.py -v
"""

import pytest
import json
import os
from pathlib import Path
from unittest.mock import patch, MagicMock


# ── Fixtures ──────────────────────────────────────────────────────────────────

VALID_INPUT = {
    "parties": "Alpha Corp (Disclosing Party) and Beta Ltd (Receiving Party)",
    "purpose": "Exploring a joint venture in cloud services",
    "confidential_info": "Source code, API keys, and business roadmaps",
    "duration": "2 years",
    "governing_law": "India",
    "industry": "Software and Technology",
}


# ── Context Builder Tests ─────────────────────────────────────────────────────

class TestContextBuilder:

    def test_build_from_valid_dict(self):
        from src.core.context_builder import build_context_from_dict
        context = build_context_from_dict(VALID_INPUT)
        assert context["parties"] == VALID_INPUT["parties"]
        assert context["governing_law"] == VALID_INPUT["governing_law"]
        assert context["sections_completed"] == []
        assert context["errors"] == []
        assert context["final_document_path"] is None

    def test_missing_required_field_raises_value_error(self):
        from src.core.context_builder import build_context_from_dict
        incomplete = {k: v for k, v in VALID_INPUT.items() if k != "governing_law"}
        with pytest.raises(ValueError, match="Missing required fields"):
            build_context_from_dict(incomplete)

    def test_build_from_file(self, tmp_path):
        from src.core.context_builder import build_context_from_file
        input_file = tmp_path / "test_input.json"
        input_file.write_text(json.dumps(VALID_INPUT))
        context = build_context_from_file(str(input_file))
        assert context["industry"] == VALID_INPUT["industry"]

    def test_file_not_found_raises(self):
        from src.core.context_builder import build_context_from_file
        with pytest.raises(FileNotFoundError):
            build_context_from_file("nonexistent/path/input.json")


# ── Sections Config Tests ─────────────────────────────────────────────────────

class TestSectionsConfig:

    def test_seven_sections_defined(self):
        from src.config.sections import NDA_SECTIONS
        assert len(NDA_SECTIONS) == 7

    def test_sections_have_required_fields(self):
        from src.config.sections import NDA_SECTIONS
        for section in NDA_SECTIONS:
            assert "id" in section
            assert "title" in section
            assert "description" in section

    def test_section_ids_are_sequential(self):
        from src.config.sections import NDA_SECTIONS
        ids = [s["id"] for s in NDA_SECTIONS]
        assert ids == list(range(1, 8))


# ── File Operations Tests ─────────────────────────────────────────────────────

class TestFileOps:

    def test_write_and_read_file(self, tmp_path):
        from src.utils.file_ops import write_file, read_file
        target = str(tmp_path / "test.txt")
        write_file(target, "Hello NDA")
        assert read_file(target) == "Hello NDA"

    def test_ensure_dirs_creates_nested(self, tmp_path):
        from src.utils.file_ops import ensure_dirs
        nested = str(tmp_path / "a" / "b" / "c")
        ensure_dirs(nested)
        assert Path(nested).exists()

    def test_section_draft_exists(self, tmp_path):
        from src.utils.file_ops import section_draft_exists, write_file
        write_file(str(tmp_path / "section_1.txt"), "content")
        assert section_draft_exists(str(tmp_path), 1) is True
        assert section_draft_exists(str(tmp_path), 2) is False


# ── Merger Tests ──────────────────────────────────────────────────────────────

class TestMerger:

    def test_merge_raises_if_sections_missing(self, tmp_path, monkeypatch):
        from src.core import merger
        monkeypatch.setattr(merger, "DRAFTS_DIR", tmp_path / "drafts")
        monkeypatch.setattr(merger, "FINAL_DIR", tmp_path / "final")
        monkeypatch.setattr(merger, "FINAL_FILE_TXT", tmp_path / "final" / "nda_final.txt")

        with pytest.raises(FileNotFoundError, match="missing"):
            merger.merge_sections(total_sections=7)

    def test_merge_produces_final_file(self, tmp_path, monkeypatch):
        from src.core import merger
        drafts_dir = tmp_path / "drafts"
        drafts_dir.mkdir()
        final_dir = tmp_path / "final"

        # Create 7 fake section files
        for i in range(1, 8):
            (drafts_dir / f"section_{i}.txt").write_text(
                f"SECTION {i}\n\n{i}.1 This is clause {i}.1\n{i}.2 This is clause {i}.2\n"
            )

        monkeypatch.setattr(merger, "DRAFTS_DIR", drafts_dir)
        monkeypatch.setattr(merger, "FINAL_DIR", final_dir)
        monkeypatch.setattr(merger, "FINAL_FILE_TXT", final_dir / "nda_final.txt")

        result = merger.merge_sections(total_sections=7)
        assert Path(result).exists()

        content = Path(result).read_text()
        assert "NON-DISCLOSURE AGREEMENT" in content
        assert "SIGNATURE PAGE" in content
        for i in range(1, 8):
            assert f"SECTION {i}" in content


# ── Section Generator Tests (mocked) ─────────────────────────────────────────

class TestSectionGenerator:

    @patch("src.core.section_generator.InferenceClient")
    def test_generate_section_saves_file(self, mock_client_class, tmp_path, monkeypatch):
        from src.core import section_generator
        monkeypatch.setattr(section_generator, "DRAFTS_DIR", tmp_path)

        mock_client = MagicMock()
        mock_client.text_generation.return_value = "1.1 This is a generated clause.\n1.2 Another clause here."
        mock_client_class.return_value = mock_client

        with patch.dict(os.environ, {"HUGGINGFACEHUB_API_TOKEN": "test-token"}):
            from src.core.context_builder import build_context_from_dict
            ctx = build_context_from_dict(VALID_INPUT)
            result = section_generator.generate_section(
                section_id=1,
                section_title="Purpose, Parties, and Context",
                section_description="Describe parties and purpose.",
                context=ctx,
            )

        assert Path(result).exists()
        assert "clause" in Path(result).read_text()

    def test_generate_section_raises_without_token(self, monkeypatch):
        from src.core import section_generator
        monkeypatch.delenv("HUGGINGFACEHUB_API_TOKEN", raising=False)

        with pytest.raises(RuntimeError, match="HUGGINGFACEHUB_API_TOKEN"):
            from src.core.context_builder import build_context_from_dict
            ctx = build_context_from_dict(VALID_INPUT)
            section_generator.generate_section(1, "Title", "Desc", ctx)


# ── End-to-End Flow Test (fully mocked) ──────────────────────────────────────

class TestEndToEndFlow:

    @patch("src.core.section_generator.InferenceClient")
    def test_full_pipeline_produces_final_document(self, mock_client_class, tmp_path, monkeypatch):
        """
        Integration test: runs the full workflow with mocked LLM calls.
        Verifies that a final NDA document is produced.
        """
        from src.core import section_generator, merger

        drafts_dir = tmp_path / "drafts"
        final_dir = tmp_path / "final"

        monkeypatch.setattr(section_generator, "DRAFTS_DIR", drafts_dir)
        monkeypatch.setattr(merger, "DRAFTS_DIR", drafts_dir)
        monkeypatch.setattr(merger, "FINAL_DIR", final_dir)
        monkeypatch.setattr(merger, "FINAL_FILE_TXT", final_dir / "nda_final.txt")

        mock_client = MagicMock()
        mock_client.text_generation.return_value = (
            "1.1 The parties agree to the following terms.\n"
            "1.2 This clause governs the agreement.\n"
        )
        mock_client_class.return_value = mock_client

        with patch.dict(os.environ, {"HUGGINGFACEHUB_API_TOKEN": "test-token"}):
            from src.core.context_builder import build_context_from_dict
            from src.graph.workflow import build_workflow

            context = build_context_from_dict(VALID_INPUT)
            workflow = build_workflow()
            final_state = workflow.invoke(context)

        assert final_state.get("final_document_path") is not None
        assert Path(final_state["final_document_path"]).exists()
        assert len(final_state.get("errors", [])) == 0
        assert len(final_state.get("sections_completed", [])) == 7
