# Experiments — heavy track

Bounded, runnable artifacts built from the highest-signal "buildable" ideas in
the corpus. Each folder has the artifact, a captured `run-output.txt` where
relevant, and an `experiment.md` recording the claim, build, and verdict.

| ID | Source idea | Theme | Artifact | Verdict |
|---|---|---|---|---|
| EXP-0001 | IDEA-0332 Git Gists as data substrate | THEME-07 | `substrate.py` — hash/anchor/sign/verify CLI | real — gist is convenience over a SHA-256 trust root |
| EXP-0002 | IDEA-0230 Signal harvesting / four layers | THEME-12 | `harvest.py` — runs over all 109 meetings | real — cross-confirms the published narrative |
| EXP-0003 | IDEA-0273 Blade Runner baseline test | THEME-06 | `baseline.py` — interview rubric + scorer | real but bounded — proves cheap auth is invertible |

Run any of them: `python3 experiments/EXP-NNNN-*/[script].py`
