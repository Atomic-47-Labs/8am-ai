#!/usr/bin/env python3
"""
EXP-0003 — Baseline interview harness ("Voight-Kampff for LLM-spoofed answers").
Source idea: IDEA-0273 "Blade Runner 2049 and Authentication Challenges"
(THEME-06 hiring-and-authentication), grade 73.7.

The group's worry: candidates run an LLM co-pilot during interviews, so the
interview stops testing the person. David's framing (via Blade Runner's
baseline test) — you have to queue off more than the spoken word, and probe
for things an LLM-on-the-side answers *too* cleanly.

This is a bounded, runnable realization: a question bank tagged with the
signal each question is meant to expose, plus a scorer that flags
LLM-spoofed-looking responses on simple, language-only heuristics. It does
NOT claim to detect AI reliably — it makes the *baseline-test pattern*
concrete and shows what a cheap first-pass screen looks like.

Heuristics (all language-only, deliberately humble):
  - latency_proxy   : response far longer/more structured than the prompt asks
  - hedge_absence   : no "I think / not sure / it depends" on an opinion Q
  - lexical_polish  : low contraction rate + high connective density (essayish)
  - specificity_gap : opinion/experience Q answered with generic definitions

Run:  python3 baseline.py            (runs the built-in demo cases)
      python3 baseline.py score "<question tag>" "<answer text>"
"""
import sys, re, json

QUESTION_BANK = [
    {"id": "q1", "tag": "experience", "signal": "specificity_gap",
     "q": "Tell me about a time a project went sideways. What did *you* personally do in the first hour?"},
    {"id": "q2", "tag": "opinion", "signal": "hedge_absence",
     "q": "React or Angular for a new internal tool — pick one and defend it in two sentences."},
    {"id": "q3", "tag": "recall", "signal": "latency_proxy",
     "q": "Off the top of your head, what's a tool you stopped using this year and why?"},
    {"id": "q4", "tag": "self", "signal": "lexical_polish",
     "q": "What's something you're bad at that you've stopped apologizing for?"},
]

CONNECTIVES = ("furthermore","moreover","additionally","consequently","therefore",
               "however","thus","hence","in conclusion","firstly","secondly")
HEDGES = ("i think","i'm not sure","not sure","it depends","probably","i guess",
          "honestly","maybe","i'd say","off the top")

def score(tag, answer):
    a = answer.strip()
    low = a.lower()
    words = re.findall(r"[a-zA-Z']+", a)
    nwords = max(1, len(words))
    flags = {}

    # lexical_polish: essayish = low contractions AND multiple connectives.
    # (require both, so short punchy human answers don't trip it)
    contractions = sum(1 for w in words if "'" in w)
    contr_rate = contractions / nwords
    conn = sum(low.count(c) for c in CONNECTIVES)
    flags["lexical_polish"] = conn >= 2 and contr_rate < 0.02

    # hedge_absence on opinion/self questions
    has_hedge = any(h in low for h in HEDGES)
    flags["hedge_absence"] = (tag in ("opinion", "self")) and not has_hedge and nwords > 20

    # latency_proxy: very long, very structured answer to a quick recall question
    flags["latency_proxy"] = (tag == "recall") and nwords > 60

    # specificity_gap: experience question answered without first-person detail
    firstperson = len(re.findall(r"\b(i|my|me|we|our|us)\b", low))
    flags["specificity_gap"] = (tag == "experience") and firstperson < 2 and nwords > 15

    triggered = [k for k, v in flags.items() if v]
    risk = len(triggered) / 4.0
    return {
        "tag": tag, "words": nwords, "contraction_rate": round(contr_rate, 3),
        "connectives": conn, "has_hedge": has_hedge, "first_person": firstperson,
        "flags": triggered,
        "spoof_risk": round(risk, 2),
        "verdict": "REVIEW" if risk >= 0.5 else ("WATCH" if risk > 0 else "OK"),
    }

DEMO = [
    ("opinion",
     # essayish, hedge-free, connective-heavy — looks LLM-spoofed
     "React is the superior choice. Firstly, it has a larger ecosystem. "
     "Furthermore, its component model promotes reusability. Consequently, "
     "teams onboard faster, and therefore maintenance costs decrease over time."),
    ("opinion",
     # human: short, hedged, opinionated
     "Honestly React, only because I'd find more people who already know it. "
     "Angular's fine, I just don't want to argue about modules all week."),
    ("experience",
     # generic, no first-person — specificity gap
     "When a project goes sideways, the best practice is to assess the situation, "
     "communicate with stakeholders, and re-prioritize the backlog accordingly."),
    ("experience",
     # human: concrete, first-person
     "Our migration broke prod at 9am. I rolled back the deploy first, then sat "
     "with Priya and we diffed the two configs until we found the bad env var."),
]

def main(argv):
    if len(argv) >= 4 and argv[1] == "score":
        print(json.dumps(score(argv[2], argv[3]), indent=2)); return 0
    print("Baseline interview harness — demo run\n")
    for tag, ans in DEMO:
        r = score(tag, ans)
        print(f"[{r['verdict']:6s}] risk={r['spoof_risk']}  tag={tag:10s} flags={r['flags']}")
        print(f"          “{ans[:70]}…”\n")
    print("Question bank:")
    for q in QUESTION_BANK:
        print(f"  {q['id']} [{q['tag']}/{q['signal']}] {q['q']}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
