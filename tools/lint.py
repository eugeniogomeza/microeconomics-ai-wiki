#!/usr/bin/env python3
"""
Wiki linter.
Checks the wiki for common issues:
- Orphaned pages (no inbound wiki links)
- Missing frontmatter
- Stale pages (not updated in a while)
- Empty categories
"""
import os
import sys
import re
from pathlib import Path
from datetime import datetime, timedelta

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
INDEX_PATH = WIKI_DIR / "_index.md"
LOG_PATH = WIKI_DIR / "_log.md"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def extract_frontmatter(content: str) -> dict:
    """Parse simple YAML frontmatter."""
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm


def find_wiki_links(content: str) -> list[str]:
    """Find all [[PageName]] links."""
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def lint_wiki():
    if not WIKI_DIR.exists():
        print(f"Wiki directory not found: {WIKI_DIR}")
        sys.exit(1)

    pages = {}  # rel_path -> { frontmatter, content, links_out, links_in }
    for md_path in WIKI_DIR.rglob("*.md"):
        content = read_file(md_path)
        rel = str(md_path.relative_to(WIKI_DIR)).replace("\\", "/")
        fm = extract_frontmatter(content)
        pages[rel] = {
            "frontmatter": fm,
            "content": content,
            "links_out": find_wiki_links(content),
            "links_in": [],
        }

    # Build inbound link map
    for rel, data in pages.items():
        for link in data["links_out"]:
            # Normalize link to possible filenames
            candidates = [
                link + ".md",
                link.replace(" ", "-") + ".md",
                link.replace(" ", "_") + ".md",
            ]
            for cand in candidates:
                if cand in pages:
                    pages[cand]["links_in"].append(rel)
                    break
                # Check inside subdirectories
                for page_rel in pages:
                    if page_rel.endswith("/" + cand):
                        pages[page_rel]["links_in"].append(rel)
                        break

    issues = []
    today = datetime.now()
    stale_threshold = today - timedelta(days=90)

    for rel, data in pages.items():
        fm = data["frontmatter"]
        if not fm:
            issues.append((rel, "Missing YAML frontmatter"))
            continue

        # Check for orphaned pages (excluding meta pages)
        if rel not in ("_index.md", "_log.md", "_templates.md", "00-overview.md"):
            if not data["links_in"]:
                issues.append((rel, "Orphaned page (no inbound links)"))

        # Check staleness
        updated = fm.get("updated", "")
        if updated:
            try:
                up_dt = datetime.strptime(updated, "%Y-%m-%d")
                if up_dt < stale_threshold:
                    issues.append((rel, f"Stale page (last updated {updated})"))
            except ValueError:
                pass

        # Check for empty TL;DR or missing title
        title = fm.get("title", "")
        if not title:
            issues.append((rel, "Missing title in frontmatter"))

    # Check categories existence
    categories = ["sources", "entities", "concepts", "questions", "outputs"]
    for cat in categories:
        cat_dir = WIKI_DIR / cat
        if not cat_dir.exists() or not any(cat_dir.iterdir()):
            issues.append((cat + "/", "Empty category (no pages yet)"))

    print(f"\nWiki Lint Report\n{'=' * 60}")
    print(f"Total pages: {len(pages)}")
    print(f"Issues found: {len(issues)}\n")

    for rel, issue in issues:
        print(f"  [{issue}] {rel}")

    if not issues:
        print("  No issues found. Wiki is healthy!")

    print(f"\n{'=' * 60}")
    print("Recommendations:")
    print("  - Run this periodically (weekly or after large ingests)")
    print("  - Address orphaned pages by adding cross-references")
    print("  - Review stale pages for outdated claims")
    print("  - Keep _index.md up to date")


def main():
    lint_wiki()


if __name__ == "__main__":
    main()
