---
title: "From scrubs to swarms"
slug: from-scrubs-to-swarms
draft: false
visibility: public
date: 2026-06-25
theme: THEME-01
ideas: 143
span: 2024-04-17 → 2026-06-17
---

Most of what gets said about AI is a snapshot. A benchmark, a launch, a take.

The 8am AI corpus is a time series. Same group, most Wednesdays, two years. The thread that runs cleanest through it is agents: how you build them, what you point them at, who's in charge.

Here's the arc, grounded in the meetings it came from.

---

## 2024: agents you build by hand

The earliest sessions use a word the group had before the industry settled on "agent": scrubs. A scrub is a basic set of instructions — a small unit you hand an LLM to make it do one job reliably. The emphasis from day one is self-reflection: get the model to check its own output.

By summer 2024 the demos are concrete. David builds a product-description agent and runs it against a real project. Agents collaborate. One agent's output becomes another's input. The group starts talking about simulation — agents standing in for people to see how a workflow behaves.

Everything is hand-wired. One agent, one prompt, one task. The work is in the authoring.

---

## 2025: orchestration replaces authoring

The conversation moves up a level. The recurring topic stops being "how do I make an agent" and becomes "how do I wire agents together."

N8N for connecting APIs. Local model runners and MCP servers, so agents can reach tools and data. Node editors where a flow is assembled instead of written out prompt by prompt.

WorkSona shows up here: a lightweight MCP server with standardized agents and reporting, built so a small team can stand up an agent by dropping a JSON file in a folder. The framing shifts from "I wrote an agent" to "I orchestrated a workflow." And then to "I can hand this to a teammate who doesn't code."

The failures get logged alongside the wins. AI-generated code violating an AutoCAD license. Context windows corrupting mid-task. "You're absolutely right" as the tell that the model lost the thread. The group never treated the tools as magic.

---

## 2026: the agentic layer, and the swarm

By January 2026 the ambition is flat: adopt an agentic layer in all work this year. Not "use agents for a task." Make the agents-finish-the-job layer a default property of how work gets done.

In March, the inflection the group had circled for two years arrives: OpenClaw and autonomous swarms. The discussion is matter-of-fact. Developers take a director role — commanding fleets of agents, delegating observation and analysis, managing risk and validation instead of doing the atomic work. The same discipline persists, one level up. The worry — no ladder to climb for people who never did the hands-on work — gets named and debated, not waved away.

The unit of work inverted. In 2024 a human authored an agent to do a task. In 2026 a human directs a swarm and the agents author the work — in the group's own projects, writing their own code and their own tickets.

---

## what the time series shows

David was running collaborating agents against real projects in mid-2024, a year before "agentic" was a headline. The corpus is the receipt.

The hard part moved. In 2024 it was authoring the agent. In 2025, orchestration. In 2026, judgment — knowing what to point the swarm at and how to validate what comes back. The work didn't disappear. It climbed.

The discipline held. Self-reflection in 2024, observability in 2025, validation in 2026. Different words, same insistence: the human stays the evaluator no matter how much the machine takes over.

That last point is the thread to follow. If the agents author the work, the scarce skill is deciding what's worth building and whether the result is true. The corpus has a name for the second half — "how do you know" — and not yet an answer.
