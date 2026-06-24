# 8am-ai

A thought facility for the 8am-AI peer group.

Weekly meetup transcripts flow through a skills pipeline that mines themes,
mentions, directives, curiosities, and goals — then walks promising threads to
a published blog post, a shared gist, or a runnable experiment.

The "book" is not authored upfront. It accretes from published artifacts.

## Status

- Substrate: scaffolded (v0.1.0). Skills are SKILL.md skeletons — implementation lands incrementally.
- Transcripts: 6 weeks already present under `transcripts/` (08-13-25 through 09-17-25).
- Publishing target: scsiwyg site `8am-ai` (editorial theme, unlisted).

## Install

**Public marketplace** (anyone):

```sh
/plugin marketplace add Atomic-47-Labs/8am-ai
/plugin install 8am-ai@8am-ai
```

**Private marketplace** (Atomic 47 Labs members):

```sh
/plugin marketplace add Atomic-47-Labs/atomic-47-marketplace
/plugin install 8am-ai@atomic-47
```

Landing page: **https://8am-ai.netlify.app**

After install you have these slash commands:

| command | purpose |
|---|---|
| `/meetup-state` | read/write/validate the facility |
| `/meetup-harvester-gdrive` | pull new transcripts from the shared Drive folder |
| `/meetup-intake` | normalize transcripts to utterance windows |
| `/meetup-classify` | extract ideas, directives, mentions, curiosities |
| `/meetup-synthesizer` | longitudinal themes; promote ideas onto a track |
| `/meetup-experimenter` | heavy track — promote a thought to a runnable test |
| `/meetup-publisher` | ship a gist + scsiwyg post |
| `/meetup-orchestrator` | weekly walk over the whole queue |

## Lifecycle

```
transcript
  └─ intake       → normalized utterance windows
     └─ classify  → IDEA / DIRECTIVE / MENTION / CURIOSITY records
        └─ synthesize → THEME records; idea track assigned
           ├─ light: research → draft → publish (blog + gist)
           └─ heavy: research → experiment → publish (blog + gist + artifact)
```

Two tracks because not every thought wants to be a runnable experiment.

## Repo layout

```
manifest.yaml                     facility config (goals, curiosities, intake, publishing)
transcripts/MM-DD-YY/             weekly transcripts (durable)
ideas/IDEA-NNNN-slug/             durable idea records
themes/THEME-NN-slug/             longitudinal theme records
directives/DIR-NNNN-slug/         action items
blog/drafts/                      staged blog posts (rebuildable)
gists/drafts/                     staged gists (rebuildable)
state/                            derived state, lock, activity log, cursors
plugin/                           the Claude Code plugin (skills + manifest)
fireflies-python-scripts/         legacy Fireflies tooling (reference only)
```

## Contributing

1. Drop a thought into a meeting; mention the idea aloud (the classifier picks it up).
2. Or open a PR against `ideas/` directly.
3. Or implement one of the skill skeletons under `plugin/skills/` — start with `meetup-state` and `meetup-intake`.

## Why this exists

Peer groups produce a lot of signal and very few durable artifacts. This
facility is an experiment in fixing that — by treating the transcript as the
source of truth and walking each surfaced thought through a small, opinionated
pipeline that ends in something shareable.

If it works, the corpus becomes a book. If it doesn't, we publish what we
learned about why.

## License

MIT.
