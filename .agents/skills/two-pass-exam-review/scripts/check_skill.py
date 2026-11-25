"""Lightweight, dependency-free structure check for this Agent Skill."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parent.parent
skill_file = root / "SKILL.md"
required = [
    skill_file,
    root / "references" / "round-one.md",
    root / "references" / "round-two.md",
    root / "references" / "grading.md",
    root / "templates" / "COURSE_PROFILE.md",
    root / "templates" / "PROGRESS.md",
    root / "state" / "industrial-economics-2026.md",
]
missing = [str(p.relative_to(root)) for p in required if not p.is_file()]
errors = []
if missing:
    errors.append("Missing files: " + ", ".join(missing))
if skill_file.is_file():
    contents = skill_file.read_text(encoding="utf-8")
    if not contents.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter.")
    else:
        try:
            front = contents.split("---\n", 2)[1]
        except IndexError:
            errors.append("Unclosed YAML frontmatter")
        else:
            name = re.search(r"(?m)^name:\s*(\S+)\s*$", front)
            description = re.search(r"(?m)^description:\s*(.+)$", front)
            if not name or name.group(1) != root.name:
                errors.append("Frontmatter name must match the directory name")
            elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)):
                errors.append("Invalid skill name")
            if not description or not description.group(1).strip():
                errors.append("Missing description")
            elif len(description.group(1)) > 1024:
                errors.append("Description exceeds 1024 characters")
    # Validate references mentioned by the SKILL.md that are local paths.
    for path in re.findall(r"`((?:references|templates|state)/[A-Za-z0-9_.\-/]+)`", contents):
        if not (root / path).is_file():
            errors.append("Unresolved link: " + path)
if errors:
    print("Skill validation FAILED:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print("Skill validation PASSED:", root)
