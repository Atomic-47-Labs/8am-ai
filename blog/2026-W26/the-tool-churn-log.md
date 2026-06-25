---
title: "The tool-churn log: two years of developer productivity at 8am AI"
slug: the-tool-churn-log
draft: true
visibility: unlisted
date: 2026-06-25
theme: THEME-04
ideas: 59
span: 2024-08-28 → 2026-06-17
---

## A diary of what people actually used

If you want to know what AI development *felt* like between 2024 and 2026 —
not the press-release version, the working-developer version — the
developer-productivity thread is the receipt. It's 59 ideas of tools tried,
tools dropped, things that broke, and the slow realization that the bottleneck
kept moving.

## The churn, in order

- **Late 2024 — the field opens up.** GPT-4 is the baseline; the news that
  *Claude is now available in Canada* is itself an event. The group compares
  coding tools, wires up N8N to connect APIs, runs OpenWebUI locally. The
  energy is "what can these things actually do for a build."
- **Early 2025 — and the field bites back.** The honest counter-current
  arrives. Fulvio hits AI-generated code that violates an AutoCAD license
  agreement; the model apologizes and does it again. AI safety in coding
  assistance becomes a real topic, not a hypothetical. The tools are powerful
  and *unreliable in specific, expensive ways.*
- **Mid 2025 — process over tool.** The conversation matures from "which
  tool" to "which methodology." Pre-development planning, methodologies for
  app building, the recognition that the IDE-with-an-agent is a workflow, not
  a gadget.
- **Late 2025 — meta on the meeting itself.** Even the Fireflies notetaker
  becomes a subject — the group is now productive enough with AI that the
  *tooling around the conversation* is worth optimizing.
- **2026 — slop, healthcare, and the upskilling gap.** "Slop code" gets
  embraced as a competitive necessity (ship fast, document the control plane).
  AI lands in regulated domains like healthcare documentation. And the gap
  that won't close: collaboration and upskilling — getting a *team* to use the
  tools compatibly, not just individuals.

## The three things that never stopped being true

Under the churn, the corpus keeps re-deriving the same lessons:

1. **The tool you're excited about will be obsolete in a quarter.** Almost
   every tool named in 2024 was superseded by 2026. The skill that survived
   wasn't tool knowledge; it was the ability to evaluate and switch.
2. **The failures are specific, not vague.** License violations, context
   corruption, "you're absolutely right" as a tell. The group logged failure
   modes as carefully as wins — which is exactly why their productivity
   advice aged better than the hype did.
3. **Individual speed ≠ team speed.** The recurring frustration of 2026: one
   person can 10x with agents, but a team that doesn't adopt compatibly loses
   the gain to friction. The hard problem was never the model. It was getting
   humans to change how they work together.

## What the churn is really measuring

The interesting thing about a two-year tool log isn't the tools. It's that
the *bottleneck moved up the stack every few months* — from "can the model
write the code" (solved fast) to "can I trust the code" (license, context) to
"can my team work this way" (still open). Productivity gains kept getting
eaten by the next layer up.

That's the real finding: **AI made the code cheap and the coordination
expensive.** Two years of tool-churn was really two years of discovering that
the hard part was never the part the tools were for.

## Open question

If individual productivity is solved and team adoption is the bottleneck,
the next tool that matters isn't a better model — it's whatever lets a group
share context, conventions, and a control plane without friction. The corpus
has a name for the substrate (project-state) but not yet a clean answer to
the social problem on top of it.
