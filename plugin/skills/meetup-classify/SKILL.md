---
name: meetup-classify
description: Use after meetup-intake, or when the user says "/meetup-classify", "extract ideas from this week", "mine the transcript". Reads normalized.yaml for one or more meetings and extracts five record kinds — ideas, themes (candidate matches), directives (action items), mentions (people/tools/repos), curiosities (open questions) — writing each as a substrate record via meetup-state.
---

# meetup-classify — mine transcripts for substrate records

This is the discriminating layer. It looks across utterance windows and writes durable records into `ideas/`, `directives/`, and a per-meeting `mentions.yaml`. Themes are not created here directly; this skill proposes theme matches that `meetup-synthesizer` later confirms or merges.

## When to use

- Step 3 of every weekly walk.
- On-demand for a single meeting.

## Inputs

- `transcripts/MM-DD-YY/normalized.yaml`.
- `manifest.yaml` → `goals`, `curiosities` (used as priors).
- Existing `themes/THEME-NN-slug/theme.yaml` (so re-occurring patterns get linked, not duplicated).
- Existing `ideas/IDEA-NNNN-*/idea.yaml` (dedup).

## Outputs (all via meetup-state write)

- New `ideas/IDEA-NNNN-<slug>/idea.yaml`:
  ```yaml
  id: IDEA-0042
  slug: agents-as-rituals
  phase: classified
  track: null                          # decided by synthesizer
  source:
    meeting: 2025-09-17
    speaker: David
    window_id: W-0014
    timestamp_s: 1832
    excerpt: "..."
  summary: "One-sentence claim of the idea."
  rationale: "Why it might matter."
  tags: [agents, rituals, applied-ai]
  theme_refs: [THEME-03]               # if matched
  directive_refs: []
  created: 2025-09-17T15:02:11Z
  updated: 2025-09-17T15:02:11Z
  ```
- New `directives/DIR-NNNN-<slug>/directive.yaml` for action items ("we should X", "I'll do Y by Z").
- `transcripts/MM-DD-YY/mentions.yaml` — flat list of `{kind: person|tool|repo|paper|company, value, count, contexts:[window_ids]}`. Lighter than its own record kind.
- Append-only theme suggestions to `state/theme-suggestions.ndjson` for the synthesizer.

## Procedure

1. `meetup-state read` normalized + manifest + existing themes/ideas.
2. For each window, run an LLM pass with this schema:
   ```json
   {
     "ideas": [{"summary","rationale","speaker","timestamp_s","excerpt","tags"}],
     "directives": [{"text","owner","due","speaker","timestamp_s"}],
     "mentions": [{"kind","value","context"}],
     "curiosities": [{"question","speaker","timestamp_s"}],
     "theme_matches": [{"theme_id","window_id","confidence"}]
   }
   ```
3. Dedup ideas across windows within the meeting (cosine on summary embeddings ≥ 0.85 → merge, prefer earliest timestamp).
4. Dedup against existing `ideas/` (same threshold) — if matched, append a new `source.linked_meetings` entry instead of creating a record.
5. Allocate ids via `meetup-state allocate-id`.
6. Write records and append activity events.
7. Curiosities that are not already in `manifest.curiosities` are surfaced in the run summary, not auto-promoted (user reviews).

## Flags

- `--meeting MM-DD-YY`: single meeting.
- `--no-dedup`: skip cross-meeting dedup (forensic).

## Quality bar

- Prefer fewer, higher-signal ideas. A meeting yielding 50 "ideas" is a failure mode. Target ≤ 10/meeting.
- Every record must cite a `window_id` + `timestamp_s` so it is traceable to the transcript.
