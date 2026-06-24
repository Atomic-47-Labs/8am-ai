# Mirroring

Canonical: **[Atomic-47-Labs/8am-ai](https://github.com/Atomic-47-Labs/8am-ai)**.
Mirror: **[worksona/8am-ai](https://github.com/worksona/8am-ai)** (legacy alias, kept in sync).

## How it works

`.github/workflows/mirror.yml` runs on every push to `Atomic-47-Labs/8am-ai`
(plus a daily cron at 07:17 UTC as a safety net) and force-pushes all branches
and tags to `worksona/8am-ai` via `--force-with-lease`.

The workflow short-circuits unless `github.repository == "Atomic-47-Labs/8am-ai"`,
so the mirror repo will never push back the other way.

## One-time setup

1. Create a fine-grained Personal Access Token on the `worksona` GitHub account
   with `Contents: read & write` scoped to the `worksona/8am-ai` repository.
2. In `Atomic-47-Labs/8am-ai`, go to
   **Settings → Secrets and variables → Actions → New repository secret**.
   - Name: `MIRROR_TOKEN`
   - Value: the PAT from step 1.
3. (Optional) trigger the workflow once manually under the Actions tab to confirm
   the first sync succeeds.

## Reverse / disable

To stop mirroring: delete `.github/workflows/mirror.yml` (or remove the secret).
To make worksona canonical instead: flip the `if:` condition and the remote URL.
