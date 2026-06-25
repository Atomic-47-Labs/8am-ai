# EXP-0003 — Baseline interview harness

- **Source idea:** IDEA-0273 — "Blade Runner 2049 and Authentication Challenges" (THEME-06, grade 73.7)
- **Type:** runnable artifact + rubric (§10 taxonomy: *tool/prompt*)
- **Status:** built ✅ · demo run ✅
- **Date:** 2026-06-25

## The claim being tested

David's worry (via Blade Runner's baseline test): when candidates run an LLM
co-pilot during an interview, the interview stops testing the person. You have
to "queue off more than the spoken word" and probe for things an
LLM-on-the-side answers *too* cleanly. Can you operationalize even a cheap
first-pass version of that?

## What was built

`baseline.py` — a question bank where each question is tagged with the signal
it's designed to expose, plus a language-only scorer with four humble flags:

| flag | catches |
|---|---|
| `lexical_polish` | essayish answers: connective-heavy, contraction-free |
| `hedge_absence` | opinion/self questions answered with zero hedging |
| `latency_proxy` | quick-recall questions answered with a long structured essay |
| `specificity_gap` | "tell me about a time *you*…" answered with generic definitions |

## The finding — honest, two-sided

**It works on obvious cases and fails on subtle ones — which is exactly the
point.** On the demo set the scorer correctly separates:

```
[REVIEW 0.50] opinion    — "React is superior. Firstly… Furthermore… Consequently…"   (spoof-looking)
[OK     0.00] opinion    — "Honestly React, only because I'd find more people…"        (human)
[WATCH  0.25] experience — "the best practice is to assess the situation…"             (generic)
[OK     0.00] experience — "Our migration broke prod at 9am. I rolled back…"           (human)
```

But a first version had the heuristics **backwards** — it flagged the genuine
concrete human answer and passed the generic one, because "no contractions +
some length" caught a punchy real reply. Fixing it (count *we/our* as
first-person, require *multiple* connectives for the polish flag) sorted the
obvious cases right.

That near-miss **is the result.** It demonstrates David's actual claim: you
cannot reliably authenticate on the spoken word alone. A cheap text scorer is
trivially inverted, and an LLM coached to add contractions and a hedge defeats
every flag here in one line of prompt. The harness is useful as a *structured
interview rubric* — it tells you which signal each question targets — not as
an AI detector. The honest conclusion matches the corpus: the baseline test
has to queue off richer signal (latency, follow-up depth, live probing) than
any after-the-fact text analysis can supply.

## Provenance

Idea mined from `transcripts/05-27-26/` (the Blade Runner discussion).
Verdict: **real but bounded** — built and runs; its main value is making the
*limits* of cheap authentication concrete, which is what the group concluded.
