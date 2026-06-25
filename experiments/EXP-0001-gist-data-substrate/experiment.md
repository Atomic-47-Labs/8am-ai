# EXP-0001 — Git Gists as a verifiable data substrate

- **Source idea:** IDEA-0332 — "Git Gists as Data Substrate" (THEME-07, grade 79.6)
- **Type:** prototype / runnable artifact (§10 taxonomy: *tool*)
- **Status:** built ✅ · smoke-tested ✅
- **Date:** 2026-06-25

## The claim being tested

In the 2026-06-17 meeting, David and Fulvio discussed using GitHub gists to
emulate blockchain-like verifiability — hash data, anchor it, and let anyone
re-verify later that it hasn't changed. The open question they left: is this
*actually* a trust primitive, or just storage with extra steps?

## What was built

`substrate.py` — a dependency-free CLI with four verbs:

| verb | does |
|---|---|
| `anchor <file>` | emit a JSON proof record (SHA-256 digest + content-addressed id) |
| `verify <file> <record>` | confirm the file still matches the record |
| `sign <file> <secret>` | add an HMAC signature to a proof |
| `check <record> <secret>` | verify the HMAC |

## The finding

The experiment **confirms the idea and sharpens it.** The key realization:
verifiability does **not** depend on the gist. The record id *is* the hash,
so tampering is detectable from the record alone — the gist only adds a
timestamp and a shareable URL. That answers the group's open question:
gists are *convenience, not trust root*. The trust root is SHA-256.

This matters because it's the cheap, real version of what "blockchain for
data integrity" usually over-promises: you get tamper-evidence and optional
authentication (HMAC) with 90 lines and no chain, no token, no consensus.

## Smoke test (actual output)

```
anchor sample.txt        → digest 5458444c…  id gist-5458444c413e06b2
verify (unchanged)       → MATCH    want=5458444c… got=5458444c…
verify (after tamper)    → TAMPERED want=5458444c… got=04282824…   (exit 2)
sign  sample.txt <secret>→ hmac 37ec3571…
check (correct secret)   → VALID
check (wrong secret)     → INVALID                                  (exit 2)
```

All six cases behaved correctly; tamper and bad-signature both fail closed.

## Where it could go

- Wire `anchor` to actually POST the proof JSON to a secret gist (the user's
  `scsiwyg` gist track or `gh gist create`) so the URL is the timestamped
  anchor — the substrate is unchanged, the gist is just the publish step.
- This is the same family as the existing **Fingerprint** tool; EXP-0001 is
  the minimal kernel of it, derived independently from the corpus.

## Provenance

Idea mined from `transcripts/06-17-26/`. Verdict: **real** — buildable,
built, runs, and the build clarified the idea (gist = convenience layer over
a SHA-256 trust root).
