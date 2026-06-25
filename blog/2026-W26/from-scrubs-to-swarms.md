---
title: "From scrubs to swarms: the two-year arc of agentic work at 8am AI"
slug: from-scrubs-to-swarms
draft: true
visibility: unlisted
date: 2026-06-25
theme: THEME-01
ideas: 143
span: 2024-04-17 → 2026-06-17
---

## A thread you can actually follow

Most of what gets said about AI is a snapshot — a benchmark, a launch, a
take. The 8am AI corpus is unusual because it's a *time series*: the same
small group, most Wednesdays, for two years. And the single thread that
runs cleanest through it is the one about agents — how you build them, what
you point them at, and who's actually in charge.

Here's the arc, grounded in the meetings it came from.

## 2024: agents you build by hand

The earliest sessions (April–May 2024) open with a word the group used
before the industry settled on "agent": **scrubs**. A scrub was a basic set
of instructions — a small, functional unit you'd give an LLM to make it do
one job reliably. The emphasis from day one was *self-reflection*: getting
the model to check its own output to improve responses.

By summer 2024 the demos get concrete. David builds a product-description
agent and runs it against a real project (Hanif's "Stonemaster"). The group
watches agents collaborate, watches one agent's output become another's
input, and starts talking about *simulation* — agents standing in for
people to see how a workflow behaves.

The defining constraint of this era: **everything is hand-wired.** One
agent, one prompt, one task. The work is in the authoring.

## 2025: orchestration replaces authoring

Through 2025 the conversation moves up a level. The recurring topics stop
being "how do I make an agent" and become "how do I wire agents together":

- N8N for connecting APIs and automating multi-step flows.
- Local model runners and MCP servers, so agents can reach tools and data.
- Workflow builders — node editors where a flow is assembled visually
  rather than written out prompt by prompt.

This is where **WorkSona** shows up in the corpus: a lightweight, portable
MCP server with standardized agents and reporting, built so a small team
can stand up an agent by dropping a JSON file in a folder. The framing
shifts from *I wrote an agent* to *I orchestrated a workflow* — and,
tellingly, to *I can hand this to a non-programmer teammate*.

The honest counter-current runs alongside it: AI-generated code violating
an AutoCAD license, context windows corrupting mid-task, the now-famous
"you're absolutely right" as a tell that the model has lost the thread.
The group never treated the tools as magic; the failure modes are logged
as carefully as the wins.

## 2026: the agentic layer, and the swarm

By January 2026 the ambition is stated flatly: **adopt an agentic layer in
all work this year.** Not "use agents for a task" — make the derivative,
after-hours, agents-finish-the-job layer a default property of how work
gets done.

Then, in March 2026, the inflection the group had been circling for two
years arrives in the conversation: **OpenClaw and autonomous swarms.**
The discussion is striking for how matter-of-fact it is. Developers
describe taking a *director* role — commanding fleets of agents, delegating
observation and analysis, managing risk and validation rather than doing
the atomic work. The same critical-thinking discipline persists, the group
argues, just at a higher altitude. The worry — that there'll be "no ladder
to climb" for people who never did the hands-on work — is named and
debated, not waved away.

Two years on, the unit of work has inverted. In 2024 a human authored an
agent to do a task. In 2026 a human directs a swarm and *the agents author
the work* — sometimes, in the group's own projects, writing their own code
and their own tickets.

## What the arc teaches

Three things only the time series makes visible:

1. **They were early.** David was running collaborating agents against real
   projects in mid-2024 — roughly a year before "agentic" became a
   headline. The corpus is a receipt for that.
2. **The hard part moved.** In 2024 the difficulty was *authoring* the
   agent. In 2025 it was *orchestration*. In 2026 it's *judgment* — knowing
   what to point the swarm at and how to validate what comes back. The work
   didn't disappear; it climbed.
3. **The discipline held.** Across every era the group's through-line is the
   same: self-reflection in 2024, observability in 2025, validation in
   2026. Different words, same insistence — the human stays in the loop as
   the evaluator, no matter how much the machine takes over.

## Open question

If the agents are now authoring the work, the scarce human skill is deciding
*what is worth building* and *whether the result is true*. The corpus has a
name for the second half of that — "how do you know" — and not yet a good
answer. That's the thread to follow next.
