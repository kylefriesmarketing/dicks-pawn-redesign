"""Graphics burn for EP02 "Only One's Real".

Runs in the Higgsfield sandbox next to master.mp4 (the assembled, per-clip
loudness-normalised clean master) and logo.png. Derived from burn.py (EP01) and
burn-ad.py: five TEST badges, no hook card, the standard series CTA card rising
on the last scene cut before "Five stores", and the master cut 0.45s after the
last word rather than held on a card.

Every timing is measured from the assembled audio. Never shift a number from a
previous edit by arithmetic; re-run this after every cut.

Writes words.json, caps.ass, lbl/*.txt, cards.txt and meta.json.
"""
import json, re, subprocess, os

W, H = 1080, 1920
NAVY = "0x133564"; GOLD = "0xc9a24b"; RED = "0xd63031"
FONT = "/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf"
SRC = "master.mp4"
HOLD = 1.9
KICK = "TEST"
BODY = {1: "THE MAGNET", 2: "THE WEIGHT", 3: "THE LOUPE", 4: "THE ACID", 5: "THE JEWELER"}
FIX = {"PONCHING": "PAWNING", "STRAIN": "STRAND", "STRAD": "STRAND",
       "LOOP": "LOUPE", "LOUP": "LOUPE", "LOOPE": "LOUPE", "LOOCH": "LOUPE",
       "STRENGTH": "STRAND", "LOOKS": "LOOK",
       "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE"}
CTA_LINES = ["FREE APPRAISAL - NO OBLIGATION", "5 STORES - (843) 646-7166", "SHIPS ANYWHERE IN THE US"]
URL = "dickspawn.com"

# ---------- transcribe, word level ----------
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
# "Scratch, drop, wait" transcribes as "drop weight" — a homophone the FIX dict
# cannot touch, because "the weight" (test 2) is a real word in clip 1.
for i, w in enumerate(words):
    if w["t"].strip(".,!?") == "WEIGHT" and i > 0 and words[i - 1]["t"].strip(".,!?") == "DROP":
        w["t"] = w["t"].replace("WEIGHT", "WAIT")

# ---------- cues: sentence-initial ordinal + sequential guard ----------
# Decoys this script must clear: "Two chains" (word 1, no predecessor),
# "Five tests" (before badge 4 is claimed), "One of these is fading" (after
# badge 1 is claimed), "Five stores" (after badge 5). See ep02-graphics.md.
NUM = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE"}
# A comma counts as a boundary: on the assembled master whisper wrote "Under the
# glass, three, the loupe" and the strict full-stop rule found no cue for test 3.
# No decoy in this script follows a comma, and the sequential guard still holds.
def starts_sentence(i): return i > 0 and words[i - 1]["t"].endswith((".", "!", "?", ","))
def find_cue(n, strict):
    for i, w in enumerate(words):
        if w["s"] <= used: continue
        if w["t"].strip(".,!?-") == NUM[n] and (starts_sentence(i) if strict else i > 0):
            return w["s"]
cues = {}; used = -1.0
for n in range(1, 6):
    t = find_cue(n, True)
    if t is None:
        t = find_cue(n, False)
        if t is not None: print(f"warning: test {n} cue taken without a sentence boundary at {t:.2f}")
    if t is None:
        print(json.dumps(words, indent=0)); raise SystemExit(f"no spoken cue for test {n}")
    cues[n] = t; used = t

# ---------- CTA rises on the last scene cut before "Five stores" ----------
sc = subprocess.run(["ffmpeg", "-i", SRC, "-vf", "select=gt(scene\\,0.35),showinfo", "-f", "null", "-"],
                    capture_output=True, text=True).stderr
cuts = sorted(float(x) for x in re.findall(r"pts_time:([0-9.]+)", sc))
fs = next((w for i, w in enumerate(words)
           if w["t"].strip(".,!?") == "FIVE" and i + 1 < len(words)
           and words[i + 1]["t"].strip(".,!?") == "STORES"), None)
if fs is None:
    print(json.dumps(words, indent=0)); raise SystemExit("no 'Five stores' in transcript")
prior = [c for c in cuts if fs["s"] - 3.0 <= c <= fs["s"] + 0.05]
CTA = max(prior) if prior else max(fs["s"] - 0.10, 0.0)
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

# ---------- badge holds ----------
# Seedance placed the counting gestures one to four beats AFTER the spoken
# numbers in clips 1 and 2 (the word "Two" lands on the cancelling wave, the
# fingers come up on the next cut). A flat 1.9s hold would drop the badge
# before the fingers appear. So each badge starts on its spoken word and ends
# at the end of the beat that carries the gesture — read off the raw clips'
# scene cuts and contact sheets, offset to the master timeline, then snapped to
# the nearest detected cut in the master. Never shorter than HOLD.
# 3 = end of the loupe insert (c2 5.208), 4 = end of the trimmed four-finger
# beat (c2 9.458 minus the 0.375s dropped), 5 = end of the five-finger beat
# (c3 3.375), each offset to the master.
GESTURE_END_HINT = {1: 6.38, 2: 12.75, 3: 20.25, 4: 24.13, 5: 33.09}
def snap(t):
    near = [c for c in cuts if abs(c - t) <= 0.45]
    return min(near, key=lambda c: abs(c - t)) if near else t
def badge_end(n): return max(cues[n] + HOLD, snap(GESTURE_END_HINT.get(n, 0.0)))

# ---------- cards ----------
os.makedirs("lbl", exist_ok=True)
f = []
for n in range(1, 6):
    st, en = cues[n], badge_end(n)
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
bt = f"between(t,{CTA:.3f},{DUR + 1:.3f})"
f.append(f"drawbox=x=60:y=1330:w=960:h=270:color={NAVY}@0.92:t=fill:enable='{bt}'")
for i, line in enumerate(CTA_LINES):
    p = f"lbl/cta{i}.txt"; open(p, "w").write(line)
    f.append(f"drawtext=fontfile={FONT}:textfile={p}:fontcolor={GOLD if i == 0 else 'white'}:"
             f"fontsize={44 if i == 0 else 40}:x=(w-text_w)/2:y={1360 + i * 78}:enable='{bt}'")
open("lbl/url.txt", "w").write(URL)
f.append(f"drawtext=fontfile={FONT}:textfile=lbl/url.txt:fontcolor=white:fontsize=40:"
         f"x=w-text_w-70:y=112:shadowcolor=black@0.8:shadowx=3:shadowy=3")
open("cards.txt", "w").write(",".join(f))

meta = {"DUR": round(DUR, 3), "CTA": round(CTA, 3), "src_dur": round(src_dur, 3),
        "cues": {str(k): round(v, 2) for k, v in cues.items()},
        "badge_ends": {str(k): round(badge_end(k), 2) for k in cues},
        "scene_cuts": [round(c, 2) for c in cuts],
        "caption_events": len(ev), "overlaps": overlaps,
        "last_word": words[-1]["t"], "last_word_end": round(words[-1]["e"], 2)}
json.dump(meta, open("meta.json", "w"), indent=1)
print(json.dumps(meta, indent=1))
print("\ncaptions:")
for e in ev: print(f"  {e['s']:6.2f}-{e['e']:6.2f}  {style(e):7s} {e['t']}")
