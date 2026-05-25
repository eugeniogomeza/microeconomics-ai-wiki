---
title: Page Templates
created: 2026-05-25
updated: 2026-05-25
category: meta
tags: [templates, meta]
status: active
---

# Page Templates

Reusable templates for creating new wiki pages. Copy the relevant template when creating a page.

## Source Template

Use for every ingested raw source.

```markdown
---
title: Source Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
category: source
tags: [article, technology]  # adjust as needed
author: Author Name
publisher: Publisher Name
url: https://example.com
status: active
---

# Source Title

**Author:** [[Author Name]]  
**Published:** YYYY-MM-DD  
**URL:** [link](https://example.com)  
**Original file:** `raw/filename.md`

## TL;DR

One-paragraph summary of the source.

## Key Claims

1. **Claim one** — evidence or reasoning
2. **Claim two** — evidence or reasoning

## Entities Mentioned

- [[Entity Name]] — role or relevance in this source

## Concepts Discussed

- [[Concept Name]] — how this source treats it

## Notable Quotes

> "Quote text" — context

## Connections to Other Sources

- [[other-source]] — agreement, contradiction, or elaboration

## Agent Notes

- Anything the agent wants to flag for future reference
- Contradictions with existing wiki pages
- Uncertainties or questions raised by this source
```

## Entity Template

Use for people, organizations, products, places.

```markdown
---
title: Entity Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
category: entity
tags: [person, organization, product, place]
status: active
---

# Entity Name

**Type:** Person / Organization / Product / Place  
**Also known as:** Aliases or alternative names

## TL;DR

One-paragraph summary.

## Profile

Detailed description, background, significance.

## Relationships

- [[Related Entity]] — nature of relationship

## Appears In

- [[source-slug]] — context of mention
- [[concept-slug]] — connection via concept

## Evolving View

- Initial impression: ...
- Updated by [[newer-source]]: ...
```

## Concept Template

Use for ideas, frameworks, technologies, theories.

```markdown
---
title: Concept Name
created: YYYY-MM-DD
updated: YYYY-MM-DD
category: concept
tags: [framework, technology, theory, idea]
status: active
---

# Concept Name

**AKA:** Alternative names  
**Related:** [[Related Concept]]

## TL;DR

One-paragraph summary.

## Explanation

Detailed explanation of the concept.

## Sources

- [[source-slug]] — how this source treats the concept

## Connections

- [[Related Concept]] — similarity, difference, or dependency

## Open Questions

- Ambiguities or areas needing further exploration
```

## Question Template

Use for open questions and research threads.

```markdown
---
title: Question Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
category: question
tags: [open-question, hypothesis, research-thread]
status: active
---

# Question Title

## Context

Why this question matters.

## Current State of Knowledge

What we know so far.

## Related Sources

- [[source-slug]] — relevant finding

## Hypotheses

1. **Hypothesis A** — supporting evidence
2. **Hypothesis B** — supporting evidence

## Next Steps

- Sources to find
- Experiments to run
- Sub-questions to explore
```

## Output Template

Use for generated artifacts like comparisons, analyses, decks.

```markdown
---
title: Output Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
category: output
tags: [analysis, comparison, summary]
status: active
---

# Output Title

**Generated in response to:** "Original human question"

## TL;DR

One-paragraph summary.

## Content

Main body of the artifact.

## Sources Used

- [[source-slug]] — specific claim used

## Filed Because

Why this answer was worth persisting in the wiki.
```
