---
name: meetup-intake
description: Use after meetup-harvester-gdrive (or when a user manually drops a transcript), or when the user says "/meetup-intake", "process new transcripts", "ingest this week's meeting". Reads transcript artifacts in transcripts/MM-DD-YY/ and writes a normalized transcript record + a queue of utterance windows ready for classification. Does NOT extract ideas — that is meetup-classify.
---

# meetup-intake — normalize transcripts into utterance windows

A transcript may arrive as `.md`, `.docx`, `.json` (Fireflies), `.txt`, or even just an `.mp3`. This skill normalizes them to a single shape so downstream skills do not branch on format.

## When to use

- Step 2 of every weekly walk.
- After a manual drop into `transcripts/MM-DD-YY/`.

## Inputs

- `transcripts/MM-DD-YY/*` (any of the supported formats above).
- `manifest.yaml` → `intake.meeting_day`, `participants`.
- `state/cursor.yaml.intake.last_processed_meeting`.

## Outputs

- `transcripts/MM-DD-YY/normalized.yaml` — canonical record:
  ```yaml
  meeting:
    date: 2025-09-17
    title: "8am-AI 2025-09-17"
    participants: [name1, name2]
    duration_s: 3600
    source_files:
      summary: "8am AI! Sep 17 2025 Summary.md"
      transcript: "8am-AI-b76f44ea-cdda.json"
      audio: "8am-AI-_2025-09-17.mp3"
  utterances:
    - speaker: David
      t_start: 12.3
      t_end: 38.4
      text: "..."
  windows:                          # ~120s sliding, 30s overlap
    - id: W-0001
      t_start: 0
      t_end: 120
      utterance_ids: [u1, u2, u3]
      text: "..."
  ```
- Updated `state/cursor.yaml.intake.last_processed_meeting`.
- Activity events `{op: intake, meeting: MM-DD-YY, utterances: N, windows: M}`.

## Procedure

1. `meetup-state read manifest.yaml` and `state/cursor.yaml`.
2. List `transcripts/*/` newer than the cursor (or all if `--reprocess`).
3. For each meeting folder, pick the richest source in this order: Fireflies JSON → Summary MD → DOCX → MP3 (transcribe). Other files become `source_files` metadata.
4. Parse utterances. For Fireflies JSON, map directly. For DOCX/MD with `Speaker: text` lines, regex-split. For MP3 without a transcript, defer (`status: needs_transcription`).
5. Compute participants ∪ across meetings → update `manifest.participants` via `meetup-state write` (dedup by lowercase first name + last initial).
6. Build sliding `windows` of ~120s with ~30s overlap. Window text is concatenated utterance text.
7. Write `normalized.yaml` via `meetup-state write`. (This file lives under `transcripts/` and is treated as a derived artifact — safe to delete and rebuild.)
8. Advance cursor.

## Flags

- `--reprocess`: rebuild `normalized.yaml` for all meetings.
- `--meeting MM-DD-YY`: process a single meeting.

## Notes

- Transcription of bare MP3s is out of scope here — surface a `needs_transcription` flag in the activity log and let the orchestrator route it.
- Speaker diarization quality varies; prefer the source format that already provides it.
