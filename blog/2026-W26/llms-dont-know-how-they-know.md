---
title: "LLMs don't know how they know — and that's why your input is the eval"
slug: llms-dont-know-how-they-know
draft: true
visibility: unlisted
date: 2026-06-25
theme: THEME-07
ideas: [IDEA-0073, IDEA-0103, IDEA-0120, IDEA-0167, IDEA-0168]
meetings_referenced: [2025-09-10, 2026-05-27, 2026-06-17, 2026-06-24]
---

## The replicant analogy

Fulvio brought *Blade Runner 2049* into the room one Wednesday in late May. He
wasn't being clever for its own sake. The interesting thing about the replicants in
that film, he pointed out, is that they don't know what they are from experience.
They know what they are from a manifest. Someone wrote it down and handed it to them.

Modern LLMs are in exactly the same position. They know they're LLMs because the
system prompt told them. Not because they have any privileged self-knowledge.

That has a few practical consequences the group keeps bumping into.

## They honestly say things that are honestly wrong

When you correct an LLM, three things may be true and you cannot tell which:

1. It concluded it was wrong only when you said so.
2. It "knew" it was wrong all along but generated the predictive answer anyway.
3. It could have known if asked the right question.

This isn't deception. They can't choose to deceive you. The predictive nature of
generation means the wrong answer is sometimes the highest-probability answer given
the context, and the model has no separate verification path. If you ask it to
self-reflect on how it knows what it knows, it gets confused — because it doesn't,
really.

## Therefore: your input is the eval

If the model can't ground itself in reality, something else has to. And in practice,
that something is the user. David's framing: "they're looking at you as the author
and the authority." Which sounds like sycophancy and partly is — but it's also a
structural fact. Your correction *is* the evaluation signal. Your context *is* the
ground truth. Without you in the loop, the model has nothing to converge toward.

This reframes a few things:

- "Hallucination" is the wrong word. The model didn't hallucinate; it produced its
  best prediction given thin context. The fix isn't to scold the model; it's to give
  it more context, or — more interestingly — to position your input as an assertion
  the model evaluates, rather than a question the model answers.

- Safety filters are easier to slip around than people think. Fulvio noted, only
  half-jokingly, that during some penetration work the safeguards never engaged
  because he framed his queries as "here's what I think, evaluate it" rather than
  "tell me how to do X." Shift the modality and the guard shifts with it.

- The grounding work is the work. The reason corpus-building, wiki-style substrates,
  and the project-state pattern matter is precisely because they're how you give the
  model a real eval surface. The model isn't the bottleneck. The context is.

## The "prompt engineering" exit

The group has started saying out loud what was implied: prompt engineering as a
distinct skill is becoming a temporary historical artifact. Once context windows are
large, retrieval is reliable, and the model can refer back to a structured corpus,
"prompting" reduces to: stating what you actually want, in terms the model can
ground in.

The skill that replaces it is harder and older. Critical thinking. Workflow design.
Understanding the system you're inside well enough to ask the right question. The
things engineers used to call "knowing what to build."

## What this changes about trust

Reputation over compliance. Behavior over agreement. Ying made a version of this
argument long before the group got to LLMs explicitly — that trust comes from how
you've shown up, not from what you've signed. That principle now reads as the right
foundation for human-LLM interaction too. The model can't sign anything that holds.
What it can do is consistently produce work whose quality you've learned to evaluate.
The trust is in the loop, not in the system prompt.

## Open question

If your input is the eval, what happens when the input is itself LLM-generated?
We don't have an answer. The group has flagged it; the substrate will track it.
