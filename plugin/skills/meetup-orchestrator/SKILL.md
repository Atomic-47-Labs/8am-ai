---
name: meetup-orchestrator
description: Use when the user runs "/meetup-orchestrator", says "run the weekly walk", "what's ready to ship from 8am-ai", or on a scheduled weekly trigger. Thin router that walks every non-terminal idea/directive/theme through its lifecycle, respects state/meetup.lock, honors weekly_budget_s, carries unfinished work forward, and emits a run summary. Holds no state of its own; all reads/writes route through meetup-state.
---

# meetup-orchestrator — weekly walk, thin router

Phase is the queue. Any idea not in `published` (or directive not in `done`/`dropped`) is in the queue.

## When to use

- Scheduled weekly trigger (e.g., the morning after the meeting).
- On-demand: `/meetup-orchestrator --once`.
- Preview: `/meetup-orchestrator --once --dry-run`.

## Flags

- `--once`: run immediately, ignore schedule.
- `--dry-run`: plan only, write nothing, do not invoke worker skills.
- `--only <step>`: harvest|intake|classify|synthesize|experiment|publish.

## Procedure

1. **Lock.** Acquire `state/meetup.lock` (flock). Refuse if held; exit `LOCK_HELD`.
2. **Harvest.** Invoke `meetup-harvester-gdrive` (skip on `--dry-run`).
3. **Intake.** Invoke `meetup-intake` for any meeting folder lacking `normalized.yaml`.
4. **Classify.** Invoke `meetup-classify` for any meeting whose `normalized.yaml` is newer than its last classify event.
5. **Synthesize.** Invoke `meetup-synthesizer` once per week (idempotent within a calendar week).
6. **Walk ideas.** For each non-terminal idea, dispatch by phase + track:
   - `classified` → leave for synthesizer to assign track.
   - `researched-queued` → invoke researcher pass (inline LLM, no separate skill yet) → `researched`.
   - `researched` (light) → compose draft inline (LLM) → `drafted`.
   - `researched` (heavy) → `meetup-experimenter` → `experimented`.
   - `drafted` | `experimented` → `meetup-publisher` (only if `--ship` flag or `manifest.publishing.scsiwyg.auto_publish=true`) → `published`.
7. **Budgets.** `weekly_budget_s` (default 1800) — when exhausted, carry remaining queue forward via `state.json.carry_forward`.
8. **Run log.** Append a line per idea to `state/logs/run-YYYY-MM-DD.txt` via meetup-state.
9. **Summary.** One line: `this week: N ingested, M ideas classified, K themes updated, P drafted, Q experimented, R published.`
10. **Notify.** If `publishing.slack.channel` set, post summary via Slack MCP.

## Carry-forward

`state/state.json.carry_forward` holds idea ids that didn't complete. Next run prioritizes those.

## Invariants

- The orchestrator never writes substrate directly — all writes route through `meetup-state`.
- The orchestrator never publishes without explicit `--ship` or `auto_publish=true` AND a successful secret-scrub.
