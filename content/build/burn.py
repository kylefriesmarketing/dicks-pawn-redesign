import json, re, os

W,H = 1080,1920
NAVY="0x133564"; GOLD="0xc9a24b"; RED="0xd63031"
FONT="/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf"
DUR   = 43.466
INSERT = (19.542, 21.458)   # detected beat bounds of the mailer shot
CTA    = 38.458             # detected cut, 0.1s before "Family owned since 1987"
HOLD   = 1.9

MYTHS = {1:"ALL STOLEN", 2:"ALL JUNK", 3:"HURTS YOUR CREDIT",
         4:"YOUR STUFF DISAPPEARS", 5:"WE WANT TO KEEP IT"}
FIX = {"PONCHING":"PAWNING", "STRAIN":"STRAND", "STRAD":"STRAND"}

# ---------- words ----------
words=[]
for w in json.load(open("words.json")):
    t = w["word"].strip().upper()
    t = re.sub(r"[^A-Z0-9'.,!?$()-]", "", t)
    base = t.strip(".,!?")
    if base in FIX: t = t.replace(base, FIX[base])
    if t: words.append({"t":t,"s":float(w["start"]),"e":float(w["end"])})

# ---------- number cues: the frame the number is actually spoken ----------
NUM={1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE"}
cues={}; used=-1.0
for n in range(1,6):
    for i,w in enumerate(words):
        if w["s"]<=used: continue
        if w["t"].strip(".,!?-")==NUM[n] and i and words[i-1]["t"].strip(".,!?-")=="NUMBER":
            cues[n]=w["s"]; used=w["s"]; break
    else:
        raise SystemExit(f"no spoken cue for myth {n}")

# ---------- captions ----------
MAXW,MAXC,GAP = 3,22,0.55
chunks,cur = [],[]
for w in words:
    if cur:
        p=cur[-1]; txt=" ".join(x["t"] for x in cur)
        if (len(cur)>=MAXW or len(txt)+1+len(w["t"])>MAXC
            or w["s"]-p["e"]>GAP or p["t"].endswith((".","!","?"))):
            chunks.append(cur); cur=[]
    cur.append(w)
if cur: chunks.append(cur)

ev=[{"s":c[0]["s"],"e":c[-1]["e"]+0.06,"t":" ".join(x["t"] for x in c)} for c in chunks]
for i in range(len(ev)-1):                       # overlapping events stack on screen
    ev[i]["e"]=min(ev[i]["e"], ev[i+1]["s"]-0.01)
ev=[e for e in ev if e["e"]>e["s"]]
overlaps=sum(1 for i in range(len(ev)-1) if ev[i]["e"]>ev[i+1]["s"])

def ts(x): return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
head=f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Montserrat ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,2,2,80,80,300,1
Style: CapHigh,Montserrat ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,5,2,2,80,80,610,1

[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
CTA_ANCHOR = 38.458
def style(e): return "CapHigh" if e["e"] > CTA_ANCHOR else "Cap"
open("caps.ass","w").write(head+"\n".join(
    f"Dialogue: 0,{ts(e['s'])},{ts(e['e'])},{style(e)},,0,0,0,,{e['t']}" for e in ev)+"\n")
print("captions lifted above the closing card:",
      [e["t"] for e in ev if style(e)=="CapHigh"])

# ---------- cards ----------
os.makedirs("lbl", exist_ok=True)
f=[]
def card(idx, num, kick, body, st, en):
    bt=f"between(t,{st:.3f},{en:.3f})"
    kf=f"lbl/k{idx}.txt"; bf=f"lbl/b{idx}.txt"
    open(kf,"w").write(kick); open(bf,"w").write(body)
    x0 = 250 if num is not None else 80
    bw = 760 if num is not None else 930
    if num is not None:
        open(f"lbl/n{idx}.txt","w").write(str(num))
        f.append(f"drawbox=x=80:y=220:w=170:h=170:color={RED}@1.0:t=fill:enable='{bt}'")
    f.append(f"drawbox=x={x0}:y=220:w={bw}:h=170:color={NAVY}@0.9:t=fill:enable='{bt}'")
    if num is not None:
        f.append(f"drawtext=fontfile={FONT}:textfile=lbl/n{idx}.txt:fontcolor=white:fontsize=110:"
                 f"x=80+(170-text_w)/2:y=220+(170-text_h)/2-8:enable='{bt}'")
    f.append(f"drawtext=fontfile={FONT}:textfile={kf}:fontcolor={GOLD}:fontsize=32:x={x0}+28:y=250:enable='{bt}'")
    f.append(f"drawtext=fontfile={FONT}:textfile={bf}:fontcolor=white:fontsize=42:x={x0}+28:y=300:enable='{bt}'")

card("hook", None, "DICK'S PAWN SUPERSTORE", "5 MYTHS, BUSTED", 0.0, 2.55)
for n in range(1,6):
    card(n, n, "MYTH", MYTHS[n], cues[n], cues[n]+HOLD)

for i,line in enumerate(["FREE APPRAISAL - NO OBLIGATION",
                         "5 STORES - (843) 646-7166",
                         "SHIPS ANYWHERE IN THE US"]):
    open(f"lbl/cta{i}.txt","w").write(line)
    bt=f"between(t,{CTA:.3f},{DUR:.3f})"
    if i==0: f.append(f"drawbox=x=60:y=1330:w=960:h=270:color={NAVY}@0.92:t=fill:enable='{bt}'")
    f.append(f"drawtext=fontfile={FONT}:textfile=lbl/cta{i}.txt:"
             f"fontcolor={GOLD if i==0 else 'white'}:fontsize={44 if i==0 else 40}:"
             f"x=(w-text_w)/2:y={1360+i*78}:enable='{bt}'")

open("lbl/url.txt","w").write("dickspawn.com")
f.append(f"drawtext=fontfile={FONT}:textfile=lbl/url.txt:fontcolor=white:fontsize=40:"
         f"x=w-text_w-70:y=112:shadowcolor=black@0.8:shadowx=3:shadowy=3")

open("cards.txt","w").write(",".join(f))
print(json.dumps({"cues":{str(k):round(v,2) for k,v in cues.items()},
                  "caption_events":len(ev),"overlaps":overlaps,
                  "insert":INSERT,"cta":CTA,"dur":DUR}, indent=2))
print("\nfirst 6 captions:")
for e in ev[:6]: print(f"  {e['s']:6.2f}-{e['e']:6.2f}  {e['t']}")
print("last 4 captions:")
for e in ev[-4:]: print(f"  {e['s']:6.2f}-{e['e']:6.2f}  {e['t']}")
