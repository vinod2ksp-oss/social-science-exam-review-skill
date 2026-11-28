#!/usr/bin/env python3
"""Lightweight stdlib-only structure validation for the new Agent Skill."""
from pathlib import Path
import re
import sys

skill_dir = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "agents/openai.yaml", "references/three-day-plan.md",
    "references/priority-and-timing.md", "references/question-types-and-grading.md",
    "templates/COURSE_INTAKE.md", "templates/PROGRESS.md", "templates/LAST_HOUR_SHEET.md",
]
errors = []
for rel in required:
    p = skill_dir / rel
    if not p.exists() or not p.read_text(encoding="utf-8").strip():
        errors.append(f"Missing/empty: {rel}")

skill = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing YAML frontmatter")
else:
    front = skill.split("---", 2)[1]
    for field in ("name", "description"):
        if not re.search(rf"^{field}:\s*\S", front, flags=re.M):
            errors.append(f"SKILL.md missing frontmatter {field}")
    if not re.search(r"^name:\s*three-day-zero-base-exam\s*$", front, flags=re.M):
        errors.append("SKILL.md name mismatch")
for rel in re.findall(r"(?:references|templates)/[A-Za-z0-9_-]+\.md", skill):
    if not (skill_dir / rel).is_file():
        errors.append(f"Broken relative reference: {rel}")

if errors:
    for e in errors:
        print("ERROR:", e)
    sys.exit(1)
print(f"PASS: {len(required)} required files, frontmatter, and local references")
