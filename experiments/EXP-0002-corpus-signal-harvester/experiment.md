# EXP-0002 — Corpus signal harvester

- **Source idea:** IDEA-0230 — "Project State's Four Layers and Signal Harvesting" (THEME-12, grade 74.4)
- **Type:** runnable analysis over real data (§10 taxonomy: *agent/skill*)
- **Status:** built ✅ · run against the live 109-meeting corpus ✅
- **Date:** 2026-06-25

## The claim being tested

THEME-12 claims the valuable knowledge in a group is *distributed across
everything it has said* and stays invisible until something reads the whole
record at once — and that this only becomes intelligence when all four layers
(agents, schema, data, time) are present. This experiment runs that claim
against the group's own two-year corpus.

## What was built

`harvest.py` — reads every meeting's `mentions.yaml`, then computes:
- **persistence** — which entities appear in the most meetings, and their
  first→last span;
- **co-occurrence** — which entities travel together in the same meeting;
- **arrivals** — entities whose first appearance is in 2026;
- **departures** — entities last seen in 2024.

It instantiates the four layers literally: the script is the *agent*, the
`mentions.yaml`/`idea.yaml` records are the *schema*, `transcripts/` is the
*data*, and meeting dates supply *time*.

## The finding

The experiment **validates the claim and, as a bonus, independently confirms
the published chapters' narrative** — which were written from a different
slice of the same corpus. The harvester, knowing nothing about the prose,
surfaces the same inflection points:

- **MCP first appears 2025-04-23** — exactly the "orchestration era" boundary
  *From scrubs to swarms* describes.
- **Open Claw / OpenClaw first appear 2026-02 / 2026-03** — the swarm
  inflection the agentic chapter dates to early 2026.
- **Neuralink + Ozempic first appear 2026-05-27** — the philosophical
  "future & society" turn.
- **Claude is the one constant** — present in 44 meetings, 2024-08 → 2026-06.

That cross-confirmation is the real result: two independent reads of the
corpus (hand-written synthesis vs. mechanical co-occurrence) agree on when
the field turned. That's the signal-harvesting thesis demonstrated, not just
asserted.

## Run output (actual, abridged)

```
85 meetings with mentions

persistent:   Claude 44 (2024-08-28→2026-06-24) · LLM 40 · Gemini 31 · MCP 16 (from 2025-04-23)
co-occur:     Claude+LLM 25 · Claude+Gemini 23 · Claude+MCP 13
arrivals 2026: Open Claw (02-18), OpenClaw (03-04), Jira (04-08), Neuralink (05-27), Ozempic (05-27)
```

(full output in `run-output.txt`)

## Note on data quality

A first run sorted meetings by folder name (MM-DD-YY) and produced nonsense
spans; fixing the sort to the ISO meeting date corrected it. Logged here
because "the schema layer has to be right or time lies to you" is itself a
THEME-12 lesson — observed live.

## Provenance

Idea mined from `transcripts/04-22-26/` (and the broader THEME-12 cluster).
Verdict: **real** — built, run against live data, and the output cross-checks
the corpus's own published narrative.
