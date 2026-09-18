# Graphics spec — EP02 "5 Questions We Get Every Single Day"

The burn is EP01's, with four changes. Geometry, colours, fonts, the caption
system and the closing card are all untouched — that is what makes five episodes
look like a series instead of five videos.

Run `content/build/burn.py` against the **re-transcribed EP02 master**. Never
reuse EP01's timings; never shift a timing by arithmetic. Measure, don't offset.

---

## Change 1 — the card texts

```python
QUESTIONS = {1:"SELL OR PAWN?",    2:"DO I NEED CREDIT?",
             3:"WHAT DO I BRING?", 4:"IS MY STUFF SAFE?",
             5:"WHAT'S IT WORTH?"}
```

Longest is 17 characters; EP01's longest was 21 ("YOUR STUFF DISAPPEARS"), so
every card clears the **fixed 760px bar** without reflow. Keep the bar fixed —
letting it auto-size is what makes a series look like five different videos.

The kicker changes from `MYTH` to `QUESTION`, and the hook card from
`5 MYTHS, BUSTED` to `5 QUESTIONS, ANSWERED`:

```python
card("hook", None, "DICK'S PAWN SUPERSTORE", "5 QUESTIONS, ANSWERED", 0.0, 2.55)
for n in range(1,6):
    card(n, n, "QUESTION", QUESTIONS[n], cues[n], cues[n]+hold(n))
```

**The kicker is doing less work here than it did on EP01, and that is fine.** On
EP01 the gold kicker was load-bearing: "ALL STOLEN" in 42px white on a pawn
shop's own video is a bad screenshot unless something on screen frames it as the
claim being debunked. A question mark does that job by itself. The kicker stays
because the series needs one card system, not because EP02 needs defending.

---

## Change 2 — the cue detector, which will otherwise fail outright

EP01 counted with *"Number one"*, *"Number two"*. EP02 counts with bare ordinals:
*"One — what's the difference…"*. So this line in `burn.py`:

```python
if w["t"].strip(".,!?-")==NUM[n] and i and words[i-1]["t"].strip(".,!?-")=="NUMBER":
```

finds nothing, and the build dies on `no spoken cue for myth 1`. Verified
against EP02's script: **all five badges fail.**

A bare-ordinal match is not the fix either, because EP02 says "five" three extra
times — *"**Five** questions"* in the first breath, *"same **five**"* four words
later, and *"**Five** stores, Grand Strand"* in the CTA. Match the ordinal alone
and badge 1 fires on word one.

What works is requiring the ordinal to **start a sentence**, since every count in
this script follows a completed one:

```python
def starts_sentence(i):
    return i > 0 and words[i-1]["t"].endswith((".", "!", "?"))

cues={}; used=-1.0
for n in range(1,6):
    for i,w in enumerate(words):
        if w["s"] <= used: continue
        if w["t"].strip(".,!?-")==NUM[n] and starts_sentence(i):
            cues[n]=w["s"]; used=w["s"]; break
    else:
        raise SystemExit(f"no spoken cue for question {n}")
```

Run against EP02's script this lands all five correctly and skips all three
decoys — the sequential `used` guard is what keeps badge 5 on *"Five — how do you
decide"* rather than on the CTA's *"Five stores"*:

```
badge 1   ...SAME FIVE. ONE - WHAT'S THE DIFFERENCE...
badge 2   ...COME BACK. TWO - DO I NEED...
badge 3   ...YOUR SCORE. THREE - WHAT DO I...
badge 4   ...OUR RULE. FOUR - IS MY STUFF...
badge 5   ...WHOLE TIME. FIVE - HOW DO YOU...
```

**This depends on Whisper punctuating the sentence breaks.** `base.en` does, but
not infallibly. Sanity-check the printed cues against the beat map before
accepting a build — they should land near:

| Badge | Predicted | From |
|---|---|---|
| 1 | ~2.3s | clip 1 beat 2 |
| 2 | ~13.4s | clip 1 beat 8 |
| 3 | ~20.7s | clip 2 beat 4 |
| 4 | ~28.2s | clip 2 beat 8 |
| 5 | ~33.9s | clip 3 beat 3 |

Anything more than ~1.5s off its prediction means the detector caught a decoy.
These are predictions from the storyboard, **not** timings to burn — Seedance
distributes its eight beats slightly differently on every render.

---

## Change 3 — badges 2 and 4 hold across the clip cut, on purpose

EP02's structure puts the second and fourth questions in the **last beat of a
clip**, with the answer opening the next one. At a flat 1.9s hold the card would
vanish within a frame or two of the cut, right as the viewer most needs to know
what is being answered.

Hold those two longer so the question is still on screen when the answer lands:

```python
HOLD  = 1.9
BRIDGE = 2.7                      # badges 2 and 4 span the clip boundary
def hold(n): return BRIDGE if n in (2,4) else HOLD
```

This is the one place EP02's graphics genuinely differ in behaviour rather than
in text, and it exists because the episode is a relay rather than a countdown.
Check it on the finished file: the card for "DO I NEED CREDIT?" should still be
up as he says "You need NO credit."

---

## Change 4 — the constants to re-measure

| Constant | EP01 | EP02 |
|---|---|---|
| `DUR` | 43.466 | re-measure from the assembled master |
| `CTA` | 38.458 | re-detect — the cut before "Five stores, Grand Strand" |
| `INSERT` | (19.542, 21.458) | **delete unless EP02 hits its own defect** |

`INSERT` was EP01's fact-card patch over a bad beat. It is not a standing
feature; it only exists if triage finds something to replace.

`CTA_ANCHOR` now derives from `CTA`, so setting `CTA` is enough — it used to be a
second hard-coded copy of the same number, which is exactly the kind of thing
that silently survives an episode change.

---

## What does not change

Everything else, deliberately:

| | |
|---|---|
| Badge | Red `#d63031`, 170×170 at (80, 220), Montserrat ExtraBold 110px |
| Bar | Navy `#133564`, fixed 760×170 at (250, 220), 90% opacity |
| Kicker | Gold `#c9a24b`, 32px |
| Card text | White, 42px |
| Hook card | 0.0–2.55s, full-width 930px, no numeral |
| Logo | `assets/dp-logo.png` at 140px, bottom-left, persistent |
| `dickspawn.com` | White 40px, top-right, drop shadow |
| Captions | ASS via libass; `Cap` MarginV 300, `CapHigh` MarginV 610 above the closing card |
| Closing card | `FREE APPRAISAL - NO OBLIGATION` / `5 STORES - (843) 646-7166` / `SHIPS ANYWHERE IN THE US` |

The closing card is identical to EP01's on purpose. It is the series' signature,
it matches EP02's spoken close ("Free look, no obligation. Five stores, Grand
Strand"), and a viewer who sees two episodes should see the same card twice.

## Transcription fixes

Keep EP01's `FIX` dict — EP02 says "pawning" and "Grand Strand" too, and Whisper
mangles both the same way every time:

```python
FIX = {"PONCHING":"PAWNING", "STRAIN":"STRAND", "STRAD":"STRAND"}
```

Read the printed captions before accepting the build. EP02 adds "resells" and
"insured", neither of which has misfired yet, but neither of which has been
through this transcriber either.
