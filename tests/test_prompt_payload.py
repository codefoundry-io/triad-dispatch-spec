"""Prompt payload format (prompts/README.md § Clause-file format); host rendering is verified separately."""

import re
from pathlib import Path

import pytest

PROMPTS = Path(__file__).resolve().parents[1] / "prompts"
LEG_FILES = ("leg-claude.md", "leg-codex.md", "leg-google.md")
LIBRARIES = ("common-clauses.md", "investigation.md")
HEADER = re.compile(r"^## (\S+)(?: \((.*)\))?$")
ORDER_ITEM = re.compile(r"^\d+\. (\S+)(?: \(.*\))?$")


def sections(name):
    """[(clause name, header note, body lines)] after the file preamble."""
    result, current = [], None
    for line in (PROMPTS / name).read_text().split("\n"):
        match = HEADER.match(line)
        if match:
            current = (match[1], match[2] or "", [])
            result.append(current)
        elif current is not None:
            current[2].append(line)
    return result


def fenced(lines):
    """(text blocks, non-blank lines outside every block)."""
    blocks, outside, block = [], [], None
    for line in lines:
        if block is None and line == "```text":
            block = []
        elif block is not None and line == "```":
            blocks.append("\n".join(block))
            block = None
        elif block is not None:
            block.append(line)
        elif line.strip():
            outside.append(line)
    assert block is None, "unterminated fenced block"
    return blocks, outside


def clauses(name):
    return {clause: fenced(lines)[0][0] for clause, _, lines in sections(name) if clause != "order"}


@pytest.mark.parametrize("name", LEG_FILES + LIBRARIES)
def test_every_clause_section_holds_exactly_one_text_block(name):
    for clause, _, lines in sections(name):
        blocks, _ = fenced(lines)
        assert len(blocks) == (0 if clause == "order" else 1), (name, clause)


@pytest.mark.parametrize("name", LEG_FILES)
def test_leg_files_carry_no_prose_outside_fences_and_only_items_in_order(name):
    for clause, _, lines in sections(name):
        _, outside = fenced(lines)
        if clause == "order":
            assert all(ORDER_ITEM.match(line) for line in outside), (name, outside)
        else:
            assert outside == [], (name, clause, outside)


def test_review_no_web_is_a_fenced_clause():
    assert clauses("common-clauses.md")["review-no-web"] == (
        "Do not use web search, URL fetching, or other network research in REVIEW.")


def test_current_date_clause_is_two_sentences_with_the_round_date():
    text = clauses("common-clauses.md")["current-date"]
    assert "<review-date>" in text
    assert text.endswith(".") and len(re.split(r"(?<=\.)\s+", text)) == 2, text


@pytest.mark.parametrize("name", LEG_FILES)
def test_every_leg_renders_current_date_after_current_basis(name):
    order = [ORDER_ITEM.match(line)[1]
             for clause, _, lines in sections(name) if clause == "order"
             for line in fenced(lines)[1]]
    assert order[order.index("common:current-basis") + 1] == "common:current-date", order


def test_host_specific_clauses_carry_the_a_only_marker():
    marked = {clause for name in LEG_FILES + LIBRARIES
              for clause, note, _ in sections(name) if clause != "order" and "A-only" in note}
    assert marked == {"claude-output-shape-notice", "claude-output-integrity", "google-a-hook-audit"}


def test_review_web_permission_carries_the_privacy_rule():
    text = clauses("common-clauses.md")["review-web-permission"]
    assert "never send the reviewed material, a local path or a person's name" in text
