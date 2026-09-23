"""Graphics burn for the 28s "We aren't dicks" title-loan spot.

Runs in the Higgsfield sandbox next to ad.mp4 and logo.png. Derived from
burn.py (EP01) with the EP02 sentence-initial cue detector, three badges instead
of five, a title-loan CTA card, and two output variants from one render:

  phone   URL top-right + phone number on the card   (Reels / Shorts)
  tiktok  no URL, no number, no address anywhere      (TikTok, from Sept 24 2026
          "trade" includes sharing contact or location information)

Writes words.json, caps.ass, lbl/*.txt, cards-phone.txt, cards-tiktok.txt and
meta.json (DUR, CTA, cues) for the shell to read. Never bakes a rate, payment,
term or "guaranteed" — those are Reg Z / SC 37-3-304 tripwires, not style calls.
"""
import json, re, subprocess

W, H = 1080, 1920
NAVY = "0x133564"; GOLD = "0xc9a24b"; RED = "0xd63031"
FONT = "/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf"
SRC = "ad.mp4"
HOLD = 1.9
KICK = "TITLE LOAN"
BODY = {1: "YOUR TITLE SECURES IT", 2: "KEEP DRIVING", 3: "READ THE TERMS FIRST"}
FIX = {"DIX": "DICKS", "DICKS'": "DICKS", "DICK": "DICKS"}
CTA_LINES = {
    "phone":  ["DICK'S TITLE LOANS", "SOUTH CAROLINA RESIDENTS ONLY", "1-843-663-AUTO"],
    "tiktok": ["DICK'S TITLE LOANS", "SOUTH CAROLINA RESIDENTS ONLY"],
}
URL = {"phone": "dickstitleloans.com", "tiktok": None}

# ---------- transcribe, word level: measure, don't offset ----------
from faster_whisper import WhisperModel
model = WhisperModel("base.en", compute_type="int8")
segs, _ = model.transcribe(SRC, word_timestamps=True)
raw = [{"word": w.word, "start": w.start, "end": w.end} for s in segs for w in s.words]
json.dump(raw, open("words.json", "w"))
src_dur = float(subprocess.check_output(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", SRC]).decode().strip())

words = []
for w in raw:
    t = w["word"].strip().upper()
    t = re.sub(r"[^A-Z0-9'.,!?$()-]", "", t)
    base = t.strip(".,!?")
    if base in FIX: t = t.replace(base, FIX[base])
    if t: words.append({"t": t, "s": float(w["start"]), "e": float(w["end"])})
# "dicks" (the joke) vs "Dick's" (the brand): possessive only when TITLE follows
for i, w in enumerate(words):
    if w["t"].strip(".,!?") == "DICKS" and i + 1 < len(words) \
            and words[i + 1]["t"].strip(".,!?") == "TITLE":
        w["t"] = w["t"].replace("DICKS", "DICK'S")

# ---------- cues: sentence-initial ordinal + sequential guard ----------
# "Three things to know" at ~6s is a decoy; the guard skips it because badge 1
# claims "One" at ~9s first and every later search starts after that.
NUM = {1: "ONE", 2: "TWO", 3: "THREE"}
def starts_sentence(i): return i > 0 and words[i - 1]["t"].endswith((".", "!", "?"))
cues = {}; used = -1.0
for n in range(1, 4):
    for i, w in enumerate(words):
        if w["s"] <= used: continue
        if w["t"].strip(".,!?-") == NUM[n] and starts_sentence(i):
            cues[n] = w["s"]; used = w["s"]; break
    else:
        print(json.dumps(words, indent=0))
        raise SystemExit(f"no spoken cue for point {n}")

# ---------- CTA rises on the brand name after the list; end on the last word ----------
cta_word = next((w for w in words if w["t"].strip(".,!?") == "DICK'S" and w["s"] > cues[3]), None)
if cta_word is None:
    print(json.dumps(words, indent=0)); raise SystemExit("no CTA cue")
CTA = max(cta_word["s"] - 0.10, 0.0)
DUR = min(words[-1]["e"] + 0.45, src_dur)

# ---------- captions ----------
MAXW, MAXC, GAP = 3, 22, 0.55
chunks, cur = [], []
for w in words:
    if cur:
        p = cur[-1]; txt = " ".join(x["t"] for x in cur)
        if (len(cur) >= MAXW or len(txt) + 1 + len(w["t"]) > MAXC
                or w["s"] - p["e"] > GAP or p["t"].endswith((".", "!", "?"))):
            chunks.append(cur); cur = []
    cur.append(w)
if cur: chunks.append(cur)
ev = [{"s": c[0]["s"], "e": c[-1]["e"] + 0.06, "t": " ".join(x["t"] for x in c)} for c in chunks]
for i in range(len(ev) - 1):
    ev[i]["e"] = min(ev[i]["e"], ev[i + 1]["s"] - 0.01)
ev = [e for e in ev if e["e"] > e["s"]]
overlaps = sum(1 for i in range(len(ev) - 1) if ev[i]["e"] > ev[i + 1]["s"])

def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
head = f"""[Script Info]
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
def style(e): return "CapHigh" if e["e"] > CTA else "Cap"
open("caps.ass", "w").write(head + "\n".join(
    f"Dialogue: 0,{ts(e['s'])},{ts(e['e'])},{style(e)},,0,0,0,,{e['t']}" for e in ev) + "\n")

# ---------- cards ----------
import os; os.makedirs("lbl", exist_ok=True)
def card_filters(variant):
    f = []
    for n in range(1, 4):
        st, en = cues[n], cues[n] + HOLD
        bt = f"between(t,{st:.3f},{en:.3f})"
        open(f"lbl/n{n}.txt", "w").write(str(n))
        open(f"lbl/k{n}.txt", "w").write(KICK)
        open(f"lbl/b{n}.txt", "w").write(BODY[n])
        f.append(f"drawbox=x=80:y=220:w=170:h=170:color={RED}@1.0:t=fill:enable='{bt}'")
        f.append(f"drawbox=x=250:y=220:w=760:h=170:color={NAVY}@0.9:t=fill:enable='{bt}'")
        f.append(f"drawtext=fontfile={FONT}:textfile=lbl/n{n}.txt:fontcolor=white:fontsize=110:"
                 f"x=80+(170-text_w)/2:y=220+(170-text_h)/2-8:enable='{bt}'")
        f.append(f"drawtext=fontfile={FONT}:textfile=lbl/k{n}.txt:fontcolor={GOLD}:fontsize=32:x=278:y=250:enable='{bt}'")
        f.append(f"drawtext=fontfile={FONT}:textfile=lbl/b{n}.txt:fontcolor=white:fontsize=42:x=278:y=300:enable='{bt}'")
    lines = CTA_LINES[variant]
    bt = f"between(t,{CTA:.3f},{DUR + 1:.3f})"
    f.append(f"drawbox=x=60:y=1330:w=960:h={60 + 78 * len(lines)}:color={NAVY}@0.92:t=fill:enable='{bt}'")
    for i, line in enumerate(lines):
        p = f"lbl/cta_{variant}_{i}.txt"; open(p, "w").write(line)
        f.append(f"drawtext=fontfile={FONT}:textfile={p}:fontcolor={GOLD if i == 0 else 'white'}:"
                 f"fontsize={44 if i == 0 else 40}:x=(w-text_w)/2:y={1360 + i * 78}:enable='{bt}'")
    if URL[variant]:
        p = f"lbl/url_{variant}.txt"; open(p, "w").write(URL[variant])
        f.append(f"drawtext=fontfile={FONT}:textfile={p}:fontcolor=white:fontsize=40:"
                 f"x=w-text_w-70:y=112:shadowcolor=black@0.8:shadowx=3:shadowy=3")
    return ",".join(f)

open("cards-phone.txt", "w").write(card_filters("phone"))
open("cards-tiktok.txt", "w").write(card_filters("tiktok"))
meta = {"DUR": round(DUR, 3), "CTA": round(CTA, 3), "src_dur": round(src_dur, 3),
        "cues": {str(k): round(v, 2) for k, v in cues.items()},
        "caption_events": len(ev), "overlaps": overlaps,
        "last_word": words[-1]["t"], "last_word_end": round(words[-1]["e"], 2)}
json.dump(meta, open("meta.json", "w"), indent=1)
print(json.dumps(meta, indent=1))
print("\ncaptions:")
for e in ev: print(f"  {e['s']:6.2f}-{e['e']:6.2f}  {style(e):7s} {e['t']}")
