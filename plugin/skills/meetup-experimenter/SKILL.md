---
name: meetup-experimenter
description: Use after meetup-synthesizer has placed an idea on the "heavy" track, or when the user says "/meetup-experimenter IDEA-NNNN", "run an experiment on this", "prove or break this thought". Designs a bounded experiment plan and executes it (sandboxed where possible), writing results into ideas/IDEA-NNNN/experiment/ so meetup-publisher can ship a writeup + runnable artifact.
---

# meetup-experimenter — promote a thought to a runnable test

The heavy track. Analogous to forge-experimenter, but inputs are ideas mined from a meeting, not a marked GitHub repo.

## When to use

- An idea with `track: heavy` is in phase `researched-queued` or `researched`.
- A user wants to convert a single idea into an experiment.

## Inputs

- `ideas/IDEA-NNNN-*/idea.yaml` (must be `track: heavy`).
- `ideas/IDEA-NNNN-*/research.md` if present.
- `manifest.yaml` → sandbox config (inherits from forge-state's docker setup if available).

## Outputs

- `ideas/IDEA-NNNN-*/experiment/plan.md` — hypothesis, method, success criterion, kill criterion, budget.
- `ideas/IDEA-NNNN-*/experiment/run.log` — stdout/stderr of the run.
- `ideas/IDEA-NNNN-*/experiment/artifacts/` — any produced files (notebook, script, gif, data).
- `ideas/IDEA-NNNN-*/experiment/outcome.yaml`:
  ```yaml
  status: succeeded|failed|inconclusive
  hypothesis_held: true|false|partial
  notes: "..."
  artifact_refs: [path1, path2]
  duration_s: 1234
  ```
- Idea phase advanced to `experimented`.

## Procedure

1. Read the idea + any research notes via `meetup-state read`.
2. Compose `plan.md` with: claim under test, smallest sufficient method, success/kill criteria, max budget (default 15 min wall time).
3. Classify experiment type (rough taxonomy):
   - prompt — test a prompt variant on a fixed eval set.
   - script — small Python/JS that demonstrates the claim.
   - dataset-probe — query an existing corpus and report.
   - demo — minimal repro of a behavior to screenshot/gif.
4. Pick the matching template under `plugin/skills/meetup-experimenter/templates/` (to be filled in over time).
5. Execute in a sandbox (docker if available; else local with a wall-clock limit). Capture stdout/stderr to `run.log`. Capture artifacts.
6. Write `outcome.yaml`. Both `succeeded` and `failed` advance the phase — null results are still publishable.
7. Append activity event and advance phase via `meetup-state advance-phase`.

## Flags

- `--idea IDEA-NNNN`: target idea.
- `--max-seconds N`: override budget.
- `--dry-run`: write plan only, do not execute.

## Quality bar

- A failed experiment with a clean writeup is a better artifact than a vague "directional" success.
- Every experiment must produce at least one artifact a reader can look at.
