#!/usr/bin/env python3
import os, glob, yaml, json
from collections import defaultdict, Counter
from itertools import combinations
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx

ROOT="/Users/davidolsson/WORKSONA/8am-ai"
INK="#2b2622"; ACCENT="#9c4a2f"; BG="#faf7f1"; MUTE="#8a8178"

# thread (theme) display names, type, descriptor
TN={'THEME-01':'agentic workflow','THEME-02':'ai and education','THEME-03':'context engineering',
'THEME-04':'developer productivity','THEME-05':'future and society','THEME-06':'hiring and authentication',
'THEME-07':'llm evaluation and trust','THEME-08':'meta / meeting cadence','THEME-09':'people and team',
'THEME-10':'product and business','THEME-11':'project-state substrate','THEME-12':'signal harvesting',
'THEME-13':'system vs design thinking','THEME-14':'tool stack'}
TYPE={'THEME-01':'Build','THEME-03':'Build','THEME-04':'Build','THEME-11':'Build','THEME-12':'Build','THEME-14':'Build',
'THEME-13':'Method','THEME-08':'Method',
'THEME-09':'Human','THEME-02':'Human',
'THEME-10':'Market',
'THEME-06':'Trust','THEME-07':'Trust',
'THEME-05':'Philosophy'}
DESC={'THEME-01':'How agents got built, pointed, and let loose.',
'THEME-02':'If the tools can do the work, what is school for.',
'THEME-03':'The model is the commodity; the context is the lever.',
'THEME-04':"A working developer's log of the moving bottleneck.",
'THEME-05':'The philosophical edge — the human after.',
'THEME-06':'Authenticating a person who runs an LLM mid-interview.',
'THEME-07':"They don't know how they know — your input is the eval.",
'THEME-08':'The group examining its own cadence.',
'THEME-09':'The social layer where AI gains are won or lost.',
'THEME-10':'From product to process; access is the scarce thing.',
'THEME-11':'The structured-memory substrate the facility runs on.',
'THEME-12':'Reading across everything said to surface the glue.',
'THEME-13':'Atomic tasks to architecture — the spine.',
'THEME-14':'The churn of named tools — tried and dropped.'}
TYPE_COLOR={'Build':'#9c4a2f','Method':'#4a6b8a','Human':'#5b8a4a','Market':'#b58a2f','Trust':'#7a4a8a','Philosophy':'#6b6b6b'}

# ---- load ideas
ideas=[yaml.safe_load(open(p)) for p in glob.glob(f"{ROOT}/ideas/*/idea.yaml")]
# ---- load themes
themes={}
for p in glob.glob(f"{ROOT}/themes/*/theme.yaml"):
    t=yaml.safe_load(open(p)); themes[t['id']]=t

# per-theme idea list and meeting set
mtg_themes=defaultdict(set)      # meeting -> set(theme)
theme_mtgs=defaultdict(set)      # theme -> set(meeting)
theme_ideas=defaultdict(list)
for i in ideas:
    m=i['source']['meeting']
    for t in (i.get('theme_refs') or []):
        if t in TN:
            mtg_themes[m].add(t); theme_mtgs[t].add(m); theme_ideas[t].append(i)

# ---- co-occurrence edges (themes sharing a meeting)
edge=Counter()
for m,ts in mtg_themes.items():
    for a,b in combinations(sorted(ts),2):
        edge[(a,b)]+=1

# ---- trajectory: theme's share of ideas in 2026 vs corpus baseline
recent=lambda i: i['source']['meeting']>='2026-01-01'
corpus_recent=sum(1 for i in ideas if recent(i))/max(1,len(ideas))
def traj(t):
    its=theme_ideas[t]
    if not its: return 'dormant'
    r=sum(1 for i in its if recent(i))/len(its)
    ratio=r/corpus_recent if corpus_recent else 0
    return 'rising' if ratio>=1.25 else ('fading' if ratio<=0.7 else 'steady')

rows=[]
for t in TN:
    its=theme_ideas[t]
    npub=sum(1 for i in its if i.get('phase')=='published')
    avg=round(sum(i.get('grade',0) for i in its)/len(its),1) if its else 0
    # strongest neighbor
    nb=[(b if a==t else a, w) for (a,b),w in edge.items() if t in (a,b)]
    nb.sort(key=lambda x:-x[1])
    strongest=TN[nb[0][0]] if nb else '—'
    th=themes.get(t,{})
    rows.append({'id':t,'name':TN[t],'type':TYPE[t],'desc':DESC[t],
        'size':len(its),'pub':npub,'avg':avg,
        'span':f"{th.get('first_seen','?')} → {th.get('last_seen','?')}",
        'meetings':len(theme_mtgs[t]),'traj':traj(t),'neighbor':strongest})
rows.sort(key=lambda r:-r['size'])

# ================= GRAPH PNG =================
G=nx.Graph()
for r in rows: G.add_node(r['id'], size=r['size'], type=r['type'])
maxw=max(edge.values())
for (a,b),w in edge.items():
    if w>=4:  # prune weak links for legibility
        G.add_edge(a,b,weight=w)

plt.figure(figsize=(11,8.5)); ax=plt.gca(); ax.set_facecolor(BG)
plt.gcf().set_facecolor(BG)
pos=nx.spring_layout(G, k=0.9, iterations=300, seed=7, weight='weight')
# edges
for a,b,d in G.edges(data=True):
    w=d['weight']
    ax.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],
        color=INK, alpha=0.06+0.5*(w/maxw), lw=0.6+3.2*(w/maxw), zorder=1)
# nodes
for r in rows:
    if r['id'] not in pos: continue
    x,y=pos[r['id']]
    s=180+r['size']*9
    ax.scatter([x],[y], s=s, c=TYPE_COLOR[r['type']], edgecolors=BG, linewidths=1.5, zorder=2, alpha=0.92)
    lbl=r['name'].replace(' / ','/\n').replace(' ','\n',1) if len(r['name'])>16 else r['name']
    ax.annotate(r['name'], (x,y), textcoords="offset points", xytext=(0,-int(8+ (s**0.5)/2)),
        ha='center', va='top', fontsize=8.2, color=INK, zorder=3)
# legend
from matplotlib.lines import Line2D
leg=[Line2D([0],[0], marker='o', color='none', markerfacecolor=c, markersize=11, label=k)
     for k,c in TYPE_COLOR.items()]
ax.legend(handles=leg, loc='lower left', frameon=False, fontsize=9, title='thread type',
          title_fontsize=9, labelcolor=INK)
ax.set_title("The threads — themes as nodes, shared meetings as edges",
             fontsize=13, color=INK, loc='left', pad=14)
ax.text(0.0,1.005,"node size = ideas in the thread · edge weight = meetings two threads share (≥4 shown)",
        transform=ax.transAxes, fontsize=8.5, color=MUTE, va='bottom')
ax.axis('off'); plt.tight_layout()
out=f"{ROOT}/site/charts/threads-graph.png"
plt.savefig(out, dpi=150, facecolor=BG, bbox_inches='tight'); plt.close()
print("wrote", out)

# ================= MERMAID =================
# subgraphs by type; top edges only
ids_by_type=defaultdict(list)
for r in rows: ids_by_type[r['type']].append(r)
short={t:TN[t].split(' ')[0].replace('/','').title() for t in TN}
# nicer short ids
SID={'THEME-01':'agentic','THEME-02':'education','THEME-03':'context','THEME-04':'devprod',
'THEME-05':'future','THEME-06':'hiring','THEME-07':'eval','THEME-08':'cadence','THEME-09':'people',
'THEME-10':'product','THEME-11':'substrate','THEME-12':'signal','THEME-13':'system','THEME-14':'toolstack'}
ML=["```mermaid","graph LR"]
for typ,c in TYPE_COLOR.items():
    grp=ids_by_type.get(typ,[])
    if not grp: continue
    ML.append(f"  subgraph {typ}")
    for r in grp:
        ML.append(f"    {SID[r['id']]}([\"{r['name']}<br/>{r['size']} ideas\"])")
    ML.append("  end")
top=sorted(edge.items(), key=lambda x:-x[1])[:18]
for (a,b),w in top:
    style="==>" if w>=maxw*0.6 else ("-->" if w>=maxw*0.35 else "-.->")
    ML.append(f"  {SID[a]} {style} {SID[b]}")
# class styling per type
for typ,c in TYPE_COLOR.items():
    ids=",".join(SID[r['id']] for r in ids_by_type.get(typ,[]))
    if ids: ML.append(f"  classDef {typ} fill:{c},stroke:#2b2622,color:#fff;")
    if ids: ML.append(f"  class {ids} {typ};")
ML.append("```")
mermaid="\n".join(ML)

# ================= POST BODY =================
RAW="https://raw.githubusercontent.com/Atomic-47-Labs/8am-ai/main/site/charts/threads-graph.png"
L=[]
L.append("A thread is a theme tracked through time — a topic the group kept pulling on across "
         "meetings until it became a line you can follow. Fourteen threads hold the corpus. This is "
         "the map: each thread is a node, sized by how many ideas it carries; two threads are linked "
         "when they keep showing up in the same meeting. The [themes index]"
         "(https://scsiwyg.com/8am-ai/themes-index) defines each one; this page shows how they connect.")
L.append("")
L.append(f"![The threads graph]({RAW})")
L.append("")
L.append("The same map renders below as a graph you can read by type. Solid heavy links are the "
         "strongest co-occurrences; dotted links are weaker ties.")
L.append("")
L.append(mermaid)
L.append("")
L.append("---")
L.append("")
L.append("## thread types")
L.append("")
L.append("Every thread falls into one of six kinds. The type tells you what the thread is *for*.")
L.append("")
tdesc={'Build':'building the thing — agents, context, tooling, the substrate underneath.',
'Method':'how the work is structured — system thinking and the meeting cadence itself.',
'Human':'the people layer — teams, teaching, the social ground AI lands on.',
'Market':'where value is captured — product, process, access.',
'Trust':'how you know — evaluation, authentication, the integrity questions.',
'Philosophy':'the long view — the human after the tools.'}
for typ,c in TYPE_COLOR.items():
    grp=ids_by_type.get(typ,[])
    if not grp: continue
    names=", ".join(r['name'] for r in sorted(grp,key=lambda r:-r['size']))
    L.append(f"**{typ}** — {tdesc[typ]}  \n*threads:* {names}")
    L.append("")
L.append("---")
L.append("")
L.append("## every thread, described")
L.append("")
L.append("| thread | type | ideas | meetings | span | trajectory | closest thread |")
L.append("|---|---|---|---|---|---|---|")
for r in rows:
    L.append(f"| **{r['name']}** | {r['type']} | {r['size']} | {r['meetings']} | {r['span']} | {r['traj']} | {r['neighbor']} |")
L.append("")
L.append("Trajectory compares each thread's share of recent (2026) ideas against the corpus baseline: "
         "*rising* threads are pulling more weight lately, *fading* ones less, *steady* ones holding.")
L.append("")
L.append("---")
L.append("")
L.append("## reading the map")
L.append("")
# a couple of grounded observations computed from the data
hub=max(rows, key=lambda r: sum(w for (a,b),w in edge.items() if r['id'] in (a,b)))
risers=[r['name'] for r in rows if r['traj']=='rising']
faders=[r['name'] for r in rows if r['traj']=='fading']
strongest_edge=max(edge.items(), key=lambda x:x[1])
L.append(f"- **{hub['name']}** is the hub — it shares more meetings with other threads than any "
         "other, which is why it sits in the middle of the graph. The build work touches everything.")
L.append(f"- The tightest single tie is **{TN[strongest_edge[0][0]]}** ↔ **{TN[strongest_edge[0][1]]}** "
         f"({strongest_edge[1]} shared meetings). They are almost the same conversation.")
if risers:
    L.append(f"- Rising lately: {', '.join(risers)}. These are where the recent meetings keep going.")
if faders:
    L.append(f"- Fading: {', '.join(faders)}. Early-corpus threads that have quieted, not closed.")
L.append("")
L.append("The graph is generated from the records, not drawn by hand. Re-running the pipeline "
         "redraws it: nodes resize as threads grow, edges thicken as threads converge. The map is "
         "a view of the substrate, and the substrate is the meetings.")
L.append("")
open("/tmp/threads-body.md","w").write("\n".join(L)+"\n")
print("wrote /tmp/threads-body.md", os.path.getsize("/tmp/threads-body.md"),"bytes")
print("\n--- summary ---")
print("threads:",len(rows),"| edges:",len(edge),"| hub:",hub['name'],"| strongest:",TN[strongest_edge[0][0]],"~",TN[strongest_edge[0][1]],strongest_edge[1])
print("rising:",risers); print("fading:",faders)
