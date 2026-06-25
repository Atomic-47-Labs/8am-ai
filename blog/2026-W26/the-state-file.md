---
title: "What 8am AI remembers"
slug: what-8am-ai-remembers
draft: false
visibility: public
date: 2026-06-25
kind: explainer
audience: the group
---

Every Wednesday we say things worth keeping. By Thursday most of them are gone. Someone made a sharp point about agents, someone half-promised to send a paper, a theme has been circling for a month and nobody quite noticed. The meeting ends and it scatters.

The substrate is the fix. It is the memory of the group. This is what it is, in plain terms.

---

## it's a folder of plain files

Not a database. Not an app you log into. A folder of text files you can open and read.

That's the whole trick, and it's deliberate. If the memory were locked inside some service, you'd need that service forever, and you'd trust it without being able to check it. Plain files you can read, copy, and back up by dragging them somewhere. An AI can read them too. So can you.

The folder has a few drawers:

- `transcripts/` — every meeting, one folder each.
- `ideas/` — the distinct things that got said.
- `themes/` — the patterns those things fall into.
- `directives/` — the action items.
- `state/` — the running tally of all of it.

---

## an idea is one thing somebody said

Here is a real one, lightly trimmed:

```
id: IDEA-0303
summary: Introduction of Project State
source:
  meeting: '2026-06-10'
  excerpt: David introduced "Project State," an application built to
    deliver skills and schemas to help users manage projects and
    stakeholders. He uses Claude to build dashboards...
theme_refs: [THEME-11]
phase: published
grade: 81.7
```

Read it top to bottom. It has a name. A one-line summary. The meeting it came from, with the actual words. The theme it belongs to. Where it is in the process. And a score from 0 to 100.

That's it. No magic. An idea is a small card with a few labels on it. There are 759 of these. Each one points back to the Wednesday it came from, so you can always check the claim against what was actually said.

---

## a theme is a pattern across many cards

```
id: THEME-01
slug: agentic-workflow
summary: 'Recurring across 68 meetings: agentic workflow.'
first_seen: '2024-04-17'
last_seen: '2026-06-17'
idea_refs: [IDEA-0192, IDEA-0238, IDEA-0272, ...]
```

A theme is what you get when the same kind of idea keeps showing up. Agentic workflow turned up in 68 meetings across two years. The theme record just lists which ideas belong to it and when it first and last appeared. Nobody decided agents would be the biggest theme. The cards piled up and the pattern was already there.

---

## a directive is something somebody said they'd do

```
id: DIR-0001
owner: André
text: Bertram will explore tools to leverage AI for updating
  documentation, and will reach out to David...
phase: dropped
```

These are the "I'll send you that" and "we should try X" moments. Each one gets an owner and a status. Most old ones are marked done or dropped — they happened, or the moment passed. Forty are still open. The point isn't to nag anyone. It's that the promises stop vanishing.

---

## the state file is the dashboard, in one file

One file, `state/state.json`, holds the running count of everything:

```
counts:
  transcripts: 109
  ideas: 759       published: 78    queued: 147    backlog: 531
  themes: 14
  directives: 401  open: 40   done: 89   dropped: 272
```

When someone asks "where are we," this is the answer, and it's never out of date, because the same process that does the work updates the count. There's also a small log next to it, `activity.ndjson`, that records every action with a timestamp — a diary of what the system did and when.

---

## two rules make it trustworthy

It's rebuildable. Every file except the raw transcripts can be deleted and regenerated. The transcripts are the only thing that matters; everything else is derived. If the memory ever looks wrong, you throw it away and rebuild it from the record.

It has one writer. Only one part of the system is allowed to change the files. Everything else asks it to. That's how 759 ideas and 401 directives stay consistent instead of turning into a mess of half-edits.

---

The whole thing is just files in a folder, with a count on top and a rule about who's allowed to write. That's the memory. The next piece — the skills — is the set of small workers that fill it in. None of this replaces the meeting. It just stops the meeting from being the only place the thinking lives.
