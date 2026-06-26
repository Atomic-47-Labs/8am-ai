#!/usr/bin/env python3
"""Regenerate the ideas-index body: lead with published articles (linked + summarised),
link each theme to its chapter, then the full 759-idea register."""
import os, glob, yaml
from collections import defaultdict

ROOT="/Users/davidolsson/WORKSONA/8am-ai"
BASE="https://scsiwyg.com/8am-ai"

TN={'THEME-01':'agentic workflow','THEME-02':'ai and education','THEME-03':'context engineering',
'THEME-04':'developer productivity','THEME-05':'future and society','THEME-06':'hiring and authentication',
'THEME-07':'llm evaluation and trust','THEME-08':'meta / meeting cadence','THEME-09':'people and team',
'THEME-10':'product and business','THEME-11':'project-state substrate','THEME-12':'signal harvesting',
'THEME-13':'system vs design thinking','THEME-14':'tool stack'}
# theme -> (chapter slug, chapter title)
CHAP={'THEME-01':('from-scrubs-to-swarms','From scrubs to swarms'),
'THEME-03':('the-model-is-the-commodity','The model is the commodity'),
'THEME-10':('product-to-process','Product to process'),
'THEME-04':('the-tool-churn-log','The tool-churn log'),
'THEME-13':('atomic-to-architecture','Atomic to architecture'),
'THEME-02':('teaching-in-the-rubble','Teaching in the rubble'),
'THEME-08':('the-meeting-as-method','The meeting as method'),
'THEME-12':('mining-the-glue','Mining the glue'),
'THEME-09':('the-social-layer','The social layer'),
'THEME-05':('the-philosophical-edge','The philosophical edge'),
'THEME-07':('how-do-you-know','How do you know'),
'THEME-06':('authenticating-the-human','Authenticating the human'),
'THEME-11':('mining-the-glue','Mining the glue'),
'THEME-14':('the-tool-churn-log','The tool-churn log')}

# published articles, grouped, with summaries
GROUPS=[
 ("the arc",[
   ("two-years-of-8am-ai","Two years of 8am AI","The whole corpus read end to end — 109 meetings, 14 themes, 759 ideas — and the clearest arc through it: agents, from hand-authored scrubs to autonomous swarms."),
 ]),
 ("chapters — one per theme",[
   ("from-scrubs-to-swarms","From scrubs to swarms","Agents across two years: hand-built scrubs in 2024, MCP orchestration in 2025, autonomous swarms in 2026. The hard part kept climbing the stack."),
   ("the-model-is-the-commodity","The model is the commodity","The corpus's clearest conviction, held for two years: the model is the commodity, the context is the lever. Ends on the question it couldn't close — how do you know."),
   ("product-to-process","Product to process","The business thread's reversal — from selling AI as a product to selling it as a process. When the build gets cheap, market access becomes the scarce thing."),
   ("the-tool-churn-log","The tool-churn log","A working developer's log of two years of tool churn, kept with its failures. AI made the code cheap and the coordination expensive."),
   ("atomic-to-architecture","Atomic to architecture","The promotion nobody assigned: the tools pushed everyone from doing atomic tasks to designing systems. The spine the whole corpus hangs on."),
   ("teaching-in-the-rubble","Teaching in the rubble","The group's conscience. If the tools can do the work, what is school for — and what happens to students who can't yet evaluate what AI gives them."),
   ("the-meeting-as-method","The meeting as method","The thread about the container, not the work. Showing up loosely every Wednesday for two years turned out to be the most durable thing the group made."),
   ("mining-the-glue","Mining the glue","The primitive the group kept reinventing until it became the method: read across everything said, surface the glue no one person can track. This blog is an instance of it."),
   ("the-social-layer","The social layer","The layer where every individual AI gain compounds or evaporates: other humans. AI made the individual more capable and the team more confusing."),
   ("the-philosophical-edge","The philosophical edge","Where the group stops talking shop and asks what it means. Cambridge Analytica to AI sovereignty to Neuralink. Holds continuity and rupture without resolving them."),
   ("how-do-you-know","How do you know","The corpus's central question, left open. A model can't tell you how it reached its answer — so what in your process tells you it's good, independent of the thing that made it."),
   ("authenticating-the-human","Authenticating the human","When the candidate can run an LLM live, the interview stops testing the person. The smallest serious thread, and the one with the most immediate teeth."),
 ]),
 ("notes from the record",[
   ("the-ninety-five-percent","The ninety-five percent","A figure the group kept landing on. AI gets you ninety-five percent of the way; the last five is human — and the last five is the part that was ever worth anything."),
   ("forty-fourth-of-forty-seven","Forty-fourth of forty-seven","A survey lands cold: Canada ranks 44th of 47 in AI readiness, and the reason is cultural, not technical. The thread where the local vantage becomes the point."),
   ("the-hundred-meeting-simulation","The hundred-meeting simulation","The reflexive moment. The group fed its own meeting history into a simulation, and it predicted the group would overload and need to reallocate work. It did."),
   ("the-franchise","The franchise","A recurring idea the group never quite shipped: 8am-ai.com as a pattern others could run. Not a product to sell — a loop to copy. The recipe is here."),
   ("the-arrivals-log","The arrivals log","Run a harvester over every mention in 109 meetings and it dates the field's turning points on its own. When MCP arrived, when the swarm landed, what stayed constant."),
   ("what-got-dropped","What got dropped","401 action items across two years: 89 done, 40 open, 272 dropped. The dropped ones aren't failures — they're a group letting go of more than it kept, on purpose."),
 ]),
 ("experiments — ideas built instead of written",[
   ("the-gist-as-a-trust-root","The gist as a trust root","EXP-0001. The highest-graded trust idea became a program that runs. Hash, anchor, sign, verify — and the finding that the gist is convenience over a SHA-256 you already had."),
   ("the-baseline-test","The baseline test","EXP-0003. A scorer for the texture of real understanding that failed in the most useful way — it flagged the human and passed the bot. Cheap authentication is invertible."),
 ]),
 ("explainers — for the group",[
   ("what-8am-ai-remembers","What 8am AI remembers","The memory of the group in plain terms. Not a database — a folder of files you can read. What an idea, a theme, and a directive actually look like."),
   ("the-workers-behind-8am-ai","The workers behind 8am AI","The skills that fill the memory in. Small workers, each with one job — harvest, classify, grade, draft, publish — and a conductor that decides what runs next."),
 ]),
 ("index & reference",[
   ("themes-index","The themes","All 14 themes, each defined, sized, spanned, with cited ideas."),
   ("meetings-index","The meetings","Every meeting: idea count, roster size, dominant theme."),
   ("threads-index","The threads","A knowledge-graph map: threads as nodes, shared meetings as edges, typed and tracked."),
   ("state-of-the-corpus","State of the corpus","A live read of the substrate with the pipeline diagram and the charts."),
   ("theme-engagement","Theme engagement over time","Which threads rose, which faded, and when the field turned."),
   ("definitions","Definitions","Every term used across the corpus and pipeline, defined once."),
 ]),
]

# ---- load
ideas=[yaml.safe_load(open(p)) for p in glob.glob(f"{ROOT}/ideas/*/idea.yaml")]
by_theme=defaultdict(list)
for i in ideas:
    for t in (i.get('theme_refs') or ['unsorted']): by_theme[t].append(i)
order=sorted([t for t in TN], key=lambda t:-len(by_theme.get(t,[])))

L=[]
L.append(f"All {len(ideas)} ideas mined from the corpus — and the {sum(len(g[1]) for g in GROUPS[:5])} articles written from them. "
   "This page leads with what got published: every article, linked, with a one-line summary. "
   "Below is the full register of all ideas, grouped by theme and sorted by grade, so you can see the raw material the articles were drawn from. "
   "A bullet marked ● in the register became part of a published chapter.")
L.append(""); L.append("---"); L.append("")
L.append("## the published articles")
L.append("")
for gname, items in GROUPS:
    L.append(f"### {gname}")
    L.append("")
    for slug,title,summ in items:
        L.append(f"- **[{title}]({BASE}/{slug})** — {summ}")
    L.append("")
L.append("---"); L.append("")
L.append("## the full register")
L.append("")
L.append(f"All {len(ideas)} ideas, grouped by theme and sorted by grade. Each line is one idea: its grade, "
         "the meeting it came from, and its one-line summary. The chapter link under each theme is the article "
         "drawn from that cluster.")
L.append("")
for t in order:
    items=sorted(by_theme[t], key=lambda x:-x.get('grade',0))
    if not items: continue
    npub=sum(1 for i in items if i.get('phase')=='published')
    L.append(f"### {TN[t]} — {len(items)} ideas, {npub} published")
    if t in CHAP:
        cs,ct=CHAP[t]
        L.append("")
        L.append(f"*Read: [{ct}]({BASE}/{cs})*")
    L.append("")
    for i in items:
        mark='●' if i.get('phase')=='published' else ('◍' if i.get('phase')=='experimented' else '○')
        L.append(f"- {mark} `{i.get('grade')}` · {i['source']['meeting']} · {i['summary']}")
    L.append("")
uns=by_theme.get('unsorted',[])
if uns:
    L.append(f"### unsorted — {len(uns)} ideas")
    L.append("")
    for i in sorted(uns,key=lambda x:-x.get('grade',0)):
        L.append(f"- ○ `{i.get('grade')}` · {i['source']['meeting']} · {i['summary']}")
    L.append("")
L.append("---"); L.append("")
L.append("● published in a chapter · ◍ built as an experiment · ○ in the queue or backlog. "
         "Grades run 0 to 100. Every idea cites its meeting; nothing here is unattributed.")
open("/tmp/idx-ideas2.md","w").write("\n".join(L)+"\n")
print("wrote /tmp/idx-ideas2.md", os.path.getsize("/tmp/idx-ideas2.md"),"bytes")
print("articles linked:", sum(len(g[1]) for g in GROUPS))
