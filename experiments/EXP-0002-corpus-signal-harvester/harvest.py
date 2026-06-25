#!/usr/bin/env python3
"""
EXP-0002 — Corpus signal harvester.
Source idea: IDEA-0230 "Project State's Four Layers and Signal Harvesting"
(THEME-12 signal-harvesting), grade 74.4.

The signal-harvesting thread claims that the valuable knowledge in a group is
*distributed across everything it has said* and stays invisible until
something reads the whole record at once. This experiment tests that claim by
actually running it: it reads all 109 meetings' mentions + ideas and surfaces
cross-meeting signals no single meeting would reveal.

It instantiates the four layers the corpus describes:
  agents  — this script (the reader)
  schema  — mentions.yaml + idea.yaml (structured records)
  data    — the transcripts/ corpus
  time    — meeting dates, which turn co-occurrence into trajectory

Output: the top tool/entity co-occurrences and their first→last appearance —
i.e. which concepts traveled together across the two years.

Run:  python3 harvest.py            (reads ../../transcripts and ../../themes)
"""
import os, yaml, itertools
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TX = os.path.join(ROOT, "transcripts")

def load():
    """Return list of (meeting_date, set(mentions))."""
    rows = []
    for d in sorted(os.listdir(TX)):
        mp = os.path.join(TX, d, "mentions.yaml")
        if not os.path.isfile(mp):
            continue
        y = yaml.safe_load(open(mp)) or {}
        mentions = {m["value"] for m in (y.get("mentions") or [])}
        if mentions and y.get("meeting"):
            rows.append((y.get("meeting"), mentions))
    # sort chronologically by ISO meeting date (folder names sort wrong)
    rows.sort(key=lambda r: r[0])
    return rows

def main():
    rows = load()
    n = len(rows)
    # entity frequency + first/last seen
    freq = Counter()
    first = {}
    last = {}
    for date, ms in rows:
        for m in ms:
            freq[m] += 1
            first.setdefault(m, date)
            last[m] = date
    # co-occurrence: pairs of entities mentioned in the same meeting
    pair = Counter()
    for _, ms in rows:
        for a, b in itertools.combinations(sorted(ms), 2):
            pair[(a, b)] += 1

    print(f"corpus signal harvest — {n} meetings with mentions\n")

    print("== most persistent entities (by meetings present) ==")
    for m, c in freq.most_common(12):
        print(f"  {c:3d} mtgs  {first[m]} → {last[m]}  {m}")

    print("\n== strongest co-occurrences (entities that travel together) ==")
    for (a, b), c in pair.most_common(12):
        print(f"  {c:3d} mtgs  {a}  +  {b}")

    print("\n== arrivals: entities whose FIRST appearance is 2026 ==")
    newcomers = sorted([(first[m], m, freq[m]) for m in freq if first[m] >= "2026-01-01"])
    for f, m, c in newcomers[:12]:
        print(f"  first {f}  ({c} mtgs)  {m}")

    print("\n== departures: entities last seen in 2024 (faded) ==")
    faded = sorted([(last[m], m, freq[m]) for m in freq if last[m] < "2025-01-01"])
    for l, m, c in faded[:12]:
        print(f"  last {l}  ({c} mtgs)  {m}")

if __name__ == "__main__":
    main()
