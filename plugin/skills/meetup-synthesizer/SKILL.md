---
name: meetup-synthesizer
description: Use weekly after meetup-classify, or when the user says "/meetup-synthesizer", "what themes are emerging", "synthesize the last month". Reads ideas, directives, and theme-suggestions; detects recurring patterns across meetings; creates or updates THEME-NN records; promotes ideas onto a track (light vs. heavy); and writes the weekly synthesis brief.
---

# meetup-synthesizer — longitudinal pattern detection

This is the step where the "book" begins to form. Single-meeting classification produces atoms; this skill detects the molecules and decides which deserve to be shipped.

## When to use

- Step 4 of every weekly walk.
- On-demand: `/meetup-synthesizer --window 4w`.

## Inputs

- All `ideas/IDEA-*/idea.yaml`.
- All `themes/THEME-*/theme.yaml`.
- `state/theme-suggestions.ndjson` (from meetup-classify).
- `directives/DIR-*/directive.yaml`.
- `manifest.yaml` → `goals`, `curiosities`, `lifecycle.tracks`.

## Outputs

- Updated / new `themes/THEME-NN-<slug>/theme.yaml`:
  ```yaml
  id: THEME-03
  slug: agents-as-rituals
  status: active
  summary: "Repeating across weeks: people treat agents as recurring rituals, not one-shots."
  first_seen: 2025-08-20
  last_seen: 2025-09-17
  idea_refs: [IDEA-0011, IDEA-0027, IDEA-0042]
  evidence:
    - meeting: 2025-08-20
      excerpt: "..."
  trajectory: rising                   # rising|steady|fading
  ```
- Updated `themes/THEME-NN/synthesis.md` — prose synthesis for inclusion in the book.
- For each promotable idea: set `phase: classified → researched-queued` and `track: light|heavy` on `ideas/IDEA-NNNN/idea.yaml`.
- `state/synthesis/YYYY-WNN.md` — the weekly brief (themes rising/fading, ideas promoted, directives open, curiosities surfaced).

## Track assignment heuristic

Heavy (idea → experiment → publish) when ANY of:
- The idea proposes a buildable artifact (CLI, prompt, dataset, tool, demo).
- An existing repo/library mention is attached and a test-or-demo is feasible.
- The idea cites a measurable claim that can be checked with a bounded experiment.

Otherwise: light (idea → research → blog/gist → publish).

## Procedure

1. Cluster ideas across meetings by embedding cosine (≥ 0.80). Each cluster ≥ 2 meetings → theme candidate.
2. For each candidate cluster:
   - If it matches an existing theme (id known via theme-suggestions or label match) → append idea_refs, update `last_seen`, recompute trajectory.
   - Else allocate `THEME-NN` and create the record.
3. Trajectory = `rising` if cluster grew this week, `steady` if same count ±1, `fading` if no new ideas in 3 weeks, `dormant` if 6 weeks.
4. For each idea not yet on a track, apply the heuristic; record `track` and advance phase to `researched-queued`.
5. Generate `synthesis/YYYY-WNN.md` with sections: rising themes, fading themes, promoted ideas (heavy), promoted ideas (light), open directives, fresh curiosities.
6. Append activity events for every theme/idea mutation.

## Flags

- `--window 4w`: limit clustering window for performance.
- `--dry-run`: emit synthesis brief and proposed mutations, write nothing.
