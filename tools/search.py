#!/usr/bin/env python3
"""
Wiki search tool.
Searches all markdown files in the wiki/ directory for a query string.
Supports basic text search with optional BM25-like ranking.
"""
import os
import sys
import re
import argparse
from pathlib import Path
from collections import Counter

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def score_content(query: str, content: str) -> tuple[float, list[int]]:
    """Simple frequency-based scoring. Returns (score, line_numbers)."""
    q_lower = query.lower()
    content_lower = content.lower()

    # Count occurrences
    count = content_lower.count(q_lower)
    if count == 0:
        return 0.0, []

    # Penalize very long files slightly
    words = content_lower.split()
    tf = count / max(len(words), 1)

    # Find line numbers
    lines = content.splitlines()
    line_nums = []
    for i, line in enumerate(lines, start=1):
        if q_lower in line.lower():
            line_nums.append(i)

    return tf * 100 + count, line_nums


def search_wiki(query: str, top_n: int = 10):
    if not WIKI_DIR.exists():
        print(f"Wiki directory not found: {WIKI_DIR}")
        sys.exit(1)

    results = []
    for md_path in WIKI_DIR.rglob("*.md"):
        content = read_file(md_path)
        score, line_nums = score_content(query, content)
        if score > 0:
            rel_path = md_path.relative_to(WIKI_DIR)
            results.append((score, rel_path, line_nums, content))

    results.sort(key=lambda x: x[0], reverse=True)

    print(f"\nSearch: '{query}'\n{'=' * 60}")
    if not results:
        print("No matches found.")
        return

    for i, (score, rel_path, line_nums, content) in enumerate(results[:top_n], start=1):
        print(f"\n{i}. [{score:.1f}] {rel_path}")
        if line_nums:
            print(f"   Lines: {', '.join(str(ln) for ln in line_nums[:5])}")
        # Show context from first match line
        lines = content.splitlines()
        for ln in line_nums[:1]:
            if 0 <= ln - 1 < len(lines):
                ctx = lines[ln - 1].strip()
                if len(ctx) > 100:
                    ctx = ctx[:97] + "..."
                print(f"   > {ctx}")

    if len(results) > top_n:
        print(f"\n... and {len(results) - top_n} more results")


def main():
    parser = argparse.ArgumentParser(description="Search the LLM wiki")
    parser.add_argument("query", nargs="+", help="Search query")
    parser.add_argument("-n", "--top", type=int, default=10, help="Max results to show")
    args = parser.parse_args()
    query = " ".join(args.query)
    search_wiki(query, top_n=args.top)


if __name__ == "__main__":
    main()
