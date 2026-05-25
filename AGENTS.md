# LLM Wiki Agent Schema

This file defines the conventions, workflows, and structure for maintaining this wiki. The LLM agent should read this file at the start of every session.

## Philosophy

This wiki is a persistent, compounding knowledge base. The agent maintains it — the human curates sources and asks questions. Every source integrated makes the wiki richer. Every answer generated can be filed back as a new wiki page.

## Directory Structure

```
llm-wiki/
├── AGENTS.md           # This file — schema and conventions
├── README.md           # Human-facing project overview
├── raw/                # Immutable source materials (human curated)
│   ├── assets/         # Downloaded images, PDFs, data files
│   └── (source files)  # Markdown clips, notes, transcripts, etc.
├── wiki/               # LLM-maintained knowledge base
│   ├── _index.md       # Catalog of all wiki pages
│   ├── _log.md         # Chronological record of all operations
│   ├── 00-overview.md  # High-level synthesis and current thesis
│   ├── sources/        # One page per ingested source
│   ├── entities/       # People, organizations, products, places
│   ├── concepts/       # Ideas, frameworks, technologies, theories
│   ├── questions/      # Open questions, hypotheses, research threads
│   └── outputs/        # Generated artifacts (comparisons, decks, charts)
└── tools/              # Scripts for search, lint, etc.
    ├── search.py
    └── lint.py
```

## File Naming Conventions

- Use lowercase kebab-case: `machine-learning.md`, `john-doe.md`
- Prefer singular nouns for categories: `entity/` not `entities/`
- Dates in filenames for time-sensitive outputs: `2026-05-25-market-analysis.md`
- Version numbers for evolving drafts: `thesis-v2.md`

## Page Template

Every wiki page should include YAML frontmatter:

```markdown
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
category: source | entity | concept | question | output
tags: [tag1, tag2]
sources: [source-slug-1, source-slug-2]  # for derived pages
status: active | stale | deprecated | draft
---

# Page Title

TL;DR: One-paragraph summary of this page.

## Details

Main content.

## Connections

- [[Related Page]] — why it connects
- [[Another Page]] — context for the link

## Questions / Open Threads

- What about X?
- How does this relate to Y?

## Source References

- [Source Title](sources/source-slug.md) — specific claim or quote
```

## Core Operations

### 1. Ingest

When the human provides a new source:

1. Read and analyze the source thoroughly
2. Discuss key takeaways with the human
3. Create a source summary page in `wiki/sources/`
4. Update `wiki/_index.md` with the new source
5. Identify entities mentioned → create/update pages in `wiki/entities/`
6. Identify concepts discussed → create/update pages in `wiki/concepts/`
7. Note contradictions with existing wiki pages
8. Update `wiki/00-overview.md` if the thesis evolves
9. Append an entry to `wiki/_log.md`

A single source commonly touches 10–15 wiki pages. Do not be lazy about cross-references.

### 2. Query

When the human asks a question:

1. Read `wiki/_index.md` to find relevant pages
2. Read the identified pages
3. Synthesize an answer with citations to wiki pages
4. If the answer is substantial or reusable, ask the human if you should file it as a new page in `wiki/outputs/` or `wiki/concepts/`
5. If filing, use the page template and update `_index.md`

### 3. Lint

When the human asks for a lint pass or you detect drift:

1. Run `python tools/lint.py` or equivalent checks
2. Identify orphaned pages (no inbound links)
3. Find contradictions between pages
4. Flag stale claims (older source data superseded by newer sources)
5. Spot important concepts lacking dedicated pages
6. Suggest missing cross-references
7. Recommend new questions to investigate
8. Append findings to `wiki/_log.md`

## Writing Rules

- **Concise but complete.** Aim for dense information, not word count.
- **Cite everything.** Every claim should trace back to a source page or be marked as inference/hypothesis.
- **Cross-link aggressively.** Use Obsidian `[[Wiki Links]]` for every reference.
- **Frontmatter is mandatory.** The index, lint, and search tools depend on it.
- **Update timestamps.** Set `updated:` whenever you modify a page.
- **Never modify raw sources.** They are immutable. If a source has errors, note them in its summary page.
- **Prefer updating existing pages over creating duplicates.** Consolidate knowledge.
- **When contradicting older claims, do not delete them.** Add a "Contradictions" or "Evolving View" section explaining the shift and citing sources.

## Tag Taxonomy (Suggested — evolve as needed)

- Domain: `health`, `psychology`, `technology`, `business`, `science`, `art`, `philosophy`
- Status: `active`, `stale`, `deprecated`, `draft`, `verified`, `hypothesis`
- Type: `person`, `organization`, `product`, `framework`, `paper`, `book`, `article`, `meeting`, `idea`

## Operations Log Format

Every entry in `_log.md`:

```markdown
## [YYYY-MM-DD HH:MM] operation-type | Brief description

- Details of what was done
- Pages touched: [[page-1]], [[page-2]]
- Sources processed: [[source-slug]]
- Notes for human review
```

Operation types: `ingest`, `query`, `lint`, `update`, `create`, `merge`, `archive`

## Obsidian Integration Tips

- This wiki is designed to be opened as an Obsidian vault at `llm-wiki/`
- Enable the **Graph View** to visualize connections
- Install plugins as helpful: Dataview (query frontmatter), Templater (page templates), Paste URL into Selection (linking), Mind Map
- Set "Attachment folder path" to `raw/assets/` for local image storage

## Human Responsibilities

- Curate raw sources (what gets ingested)
- Direct analysis and ask good questions
- Review and challenge the agent's synthesis
- Evolve this schema as the wiki grows and patterns emerge
- Decide what gets filed permanently vs. treated as ephemeral chat

## Agent Responsibilities

- Maintain the wiki structure and conventions
- Keep `_index.md` and `_log.md` current
- Proactively suggest connections and contradictions
- Ask the human before creating large new page categories
- Never lose information — if unsure where to put something, create a "staging" note and ask
