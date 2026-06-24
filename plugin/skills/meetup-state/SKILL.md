---
name: meetup-state
description: Use whenever any meetup-* skill or user request needs to read, write, or validate the 8am-ai facility — including init, allocating an IDEA-NNNN / THEME-NN / DIR-NNNN id, advancing an idea's phase, scrubbing secrets, or appending to state/activity.ndjson. The only skill permitted to write the substrate (ideas/, themes/, directives/, state/) to disk. Trigger phrases include "/meetup-state", "init the meetup facility", "validate the 8am-ai facility", "advance IDEA-0007 to drafted", "scrub this draft".
---

# meetup-state — substrate spine

The shared memory of the 8am-ai facility. Every other meetup-* skill routes its reads and writes through this one — no skill writes the substrate directly.

## When to use

- A meetup skill needs to read or update an `ideas/IDEA-NNNN-slug/idea.yaml`, `themes/THEME-NN-slug/theme.yaml`, or `directives/DIR-NNNN-slug/directive.yaml` record.
- The orchestrator needs to allocate a new id, advance a phase, append to the activity log, or refresh `state/state.json`.
- The user asks to init the facility, validate it, or audit drift.
- A publisher needs to scrub secrets before shipping.

## Facility layout

```
8am-ai/                                 # repo root (this checkout)
  manifest.yaml
  transcripts/MM-DD-YY/                 # weekly transcript folders (existing)
    8am AI! ...Summary.md
    8am-AI-_YYYY-MM-DD.mp3
    8am-AI-*.json                       # fireflies json
    8am-AI-*.docx
  ideas/
    IDEA-NNNN-slug/
      idea.yaml                         # canonical record
      research.md                       # optional
      draft.md                          # blog/gist draft (light track)
      experiment/                       # heavy track only
        plan.md
        artifacts/
      published.yaml                    # gist + blog urls when shipped
  themes/
    THEME-NN-slug/
      theme.yaml                        # recurring pattern across weeks
      synthesis.md
  directives/
    DIR-NNNN-slug/
      directive.yaml                    # actionable item raised in meeting
  blog/drafts/                          # staging before scsiwyg
  gists/drafts/                         # staging before push
  state/
    state.json                          # derived snapshot
    activity.ndjson                     # append-only log
    cursor.yaml                         # per-surface intake cursors
    meetup.lock                         # single-writer flock
    logs/run-YYYY-MM-DD.txt
```

`transcripts/`, `ideas/`, `themes/`, `directives/` are durable. `state/` and `blog/drafts/`, `gists/drafts/` are rebuildable.

## Operations

| op | inputs | effect |
|---|---|---|
| `init` | (none) | create dirs, write empty state.json, idempotent |
| `read` | path | return YAML/JSON/MD contents |
| `write` | path, content | validate against schema (when present), write |
| `validate` | (none) | walk ideas/themes/directives, validate against schemas |
| `allocate-id` | kind=idea\|theme\|directive | scan kind/, return next id |
| `advance-phase` | id, new_phase | update record; append activity event; refresh state.json |
| `scrub-secrets` | text | redact known secret values → return scrubbed text |
| `append-activity` | event | append one NDJSON line to state/activity.ndjson |
| `link` | from_id, to_id, kind | record idea↔theme, idea↔directive cross-links |

## Procedure

1. Resolve facility root: nearest ancestor containing `manifest.yaml` with `facility: 8am-ai`, else `~/8am-ai` if symlinked.
2. Acquire `state/meetup.lock` (advisory flock) for any write op; fail-fast if held.
3. For `write`: if a schema exists in `schemas/`, validate before persisting.
4. For `advance-phase`: only allow transitions matching the lifecycle DAG in manifest.
5. For `scrub-secrets`: load secret values from configured store, build redaction map, replace each with `<REDACTED:name>`.
6. Append every state-changing op to `state/activity.ndjson` as `{ts, op, id, before, after}`.

## Schemas

- `schemas/idea.schema.yaml` — fields: id, slug, phase, track (light|heavy), source.{transcript, speaker, timestamp_s, surface}, summary, tags[], theme_refs[], directive_refs[], created, updated.
- `schemas/theme.schema.yaml` — id, slug, summary, first_seen, last_seen, idea_refs[], status (emerging|active|dormant|matured).
- `schemas/directive.schema.yaml` — id, slug, owner, due, source.{transcript, speaker}, status (open|in-flight|done|dropped), idea_refs[].

## Invariants

- Only meetup-state writes to `ideas/`, `themes/`, `directives/`, `state/`. Other skills compose payloads and hand them to this skill.
- Activity log is append-only.
- Ids are monotonic, never reused.
