---
name: meetup-publisher
description: Use when an idea is in phase "drafted" (light track) or "experimented" (heavy track), or when the user says "/meetup-publisher IDEA-NNNN", "ship this", "publish the week". Composes the final post body, pushes a secret gist for the long-form / artifact, publishes a scsiwyg blog post on the 8am-ai site (unlisted, editorial theme), and records URLs into ideas/IDEA-NNNN/published.yaml. Secret-scrubs everything before send.
---

# meetup-publisher — ship to gist + scsiwyg blog

## When to use

- An idea is ready: light track in `drafted`, heavy track in `experimented`.
- The user runs `/meetup-publisher` to ship one or all eligible ideas.

## Inputs

- `ideas/IDEA-NNNN-*/idea.yaml`, `draft.md`, `research.md`, `experiment/outcome.yaml` (heavy only).
- `manifest.yaml` → `publishing.scsiwyg.{site_slug,theme,visibility,auto_publish}`, `publishing.gist.visibility`.
- Secrets via `meetup-state` keychain refs (never inlined).

## Outputs

- A secret gist with the long-form writeup + any code/data artifacts.
- A scsiwyg post on the `8am-ai` site (editorial theme, unlisted) linking to the gist.
- `ideas/IDEA-NNNN-*/published.yaml`:
  ```yaml
  gist_url: https://gist.github.com/...
  blog_url: https://8am-ai.scsiwyg.app/p/...
  published_at: 2026-06-24T14:30:00Z
  visibility:
    gist: secret
    blog: unlisted
  ```
- Idea phase advanced to `published`.

## Procedure

1. `meetup-state read` the idea bundle.
2. Compose body:
   - Title from `idea.summary` (rewritten for headline shape).
   - Light track: 600–1200 word essay drawn from `draft.md` + `research.md`, ending in a "what this unlocks" + "open questions" pair.
   - Heavy track: prepend a TL;DR (claim, outcome, surprise), then writeup, then "how to reproduce" pointing at the gist.
   - Footer: attribution `Surfaced in the 8am-AI meetup on <date>. Participants: <list>.` and a permalink to the source transcript in this repo.
3. `meetup-state scrub-secrets` on the full body and on every artifact about to be pushed. If any redaction fires, abort and require user review.
4. Push secret gist via `gh gist create` with all artifacts.
5. Publish to scsiwyg: `mcp__scsiwyg__create_post` with `site=8am-ai`, `unlisted=true`, body = composed essay (with gist URL appended).
6. Write `published.yaml` and advance phase via `meetup-state advance-phase`.
7. If `publishing.slack.channel` is configured, post a one-line announcement via the Slack MCP.
8. Append activity event `{op: publish, id, gist_url, blog_url}`.

## Flags

- `--idea IDEA-NNNN`: ship one.
- `--all-ready`: ship everything currently eligible.
- `--draft-only`: compose body, write to `blog/drafts/` and `gists/drafts/`, do not push.

## Safety

- Never push without a successful secret-scrub pass.
- Never make a post `public` unless `publishing.scsiwyg.visibility=public` explicitly (manifest is `unlisted` by default).
- A failed gist push aborts the blog publish (atomicity).
