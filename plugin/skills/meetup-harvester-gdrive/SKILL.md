---
name: meetup-harvester-gdrive
description: Use when the user runs "/meetup-harvester-gdrive", says "pull the latest transcripts from Drive", "sync 8am-ai transcripts", or when meetup-orchestrator begins its weekly walk. Pulls transcript artifacts (Google Docs, .txt, .md, .json, .docx) from the configured Google Drive folder into transcripts/MM-DD-YY/ subdirectories keyed by meeting date, and advances state/cursor.yaml.
---

# meetup-harvester-gdrive — pull transcripts from Drive

The trigger is a Drive folder containing per-meeting subfolders (or files named with dates). This skill drains new artifacts into the local `transcripts/` tree without overwriting existing files.

## When to use

- Step 1 of every weekly walk (called by `meetup-orchestrator`).
- On-demand when the user wants to flush the intake queue.
- After a `--bind` operation that sets the source folder id.

## Inputs

- `manifest.yaml` → `intake.surfaces[kind=google-drive]`: `folder_id`, `mime_types`.
- `state/cursor.yaml` → last harvested `modifiedTime` per folder.
- Google Drive credentials from host keychain (`secrets.refs.google_drive`).

## Outputs

- New files written to `transcripts/MM-DD-YY/` where date is derived from the file/folder name or the Drive `createdTime`.
- Updated `state/cursor.yaml`.
- Activity events `{op: harvest, surface: gdrive, file_id, path}` via meetup-state.

## Procedure

1. Read manifest + cursor via `meetup-state read`.
2. If `intake.surfaces[kind=google-drive].folder_id` is null and the user passed `--bind <folder_id>`, write it to manifest via `meetup-state write` and continue. Otherwise refuse with `GDRIVE_NOT_BOUND` and instruct the user to run `/meetup-harvester-gdrive --bind <folder_id>`.
3. List files under the folder (recursive) where `modifiedTime > cursor.last_modified` and `mimeType ∈ intake.mime_types`. Use the Google Drive MCP if present, otherwise `gdrive` CLI, otherwise instruct user to install one.
4. For each file:
   - Parse meeting date: try filename regex (`\b(\d{2}-\d{2}-\d{2})\b` or `(\d{4}-\d{2}-\d{2})`), then fall back to parent-folder name, then `createdTime`. Normalize to `MM-DD-YY`.
   - Compute target path `transcripts/<MM-DD-YY>/<original_filename>`. If it exists with same SHA-256, skip. Otherwise download.
   - For Google Doc mime: export as `text/markdown` and save with `.md` extension.
5. Advance `cursor.yaml.gdrive.last_modified` to max processed `modifiedTime`.
6. Emit activity events for each new file.
7. Summary: `harvested N transcripts across M meetings`.

## Flags

- `--bind <folder_id>`: persist a new Drive folder id into manifest and exit.
- `--since YYYY-MM-DD`: override cursor for a backfill.
- `--dry-run`: list what would be pulled, write nothing.

## Tools

- Google Drive MCP (preferred): file listing + export.
- `gdrive` CLI as fallback.

## Notes

- The legacy `fireflies-python-scripts/` directory is kept for reference and re-enabled via `intake.surfaces[kind=fireflies].enabled=true` if direct Fireflies API access is preferred over Drive.
- Never write transcripts outside `transcripts/`. Never delete on the Drive side.
