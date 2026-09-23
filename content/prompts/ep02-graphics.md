# Graphics spec — EP02 "Only One's Real"

EP01's burn with the EP03 cue detector and five changes. Geometry, colours,
fonts, captions and the closing card are untouched.

## The card texts

```python
TESTS = {1:"THE MAGNET", 2:"THE WEIGHT", 3:"THE LOUPE", 4:"THE ACID", 5:"THE JEWELER"}
KICK  = "TEST"
```

Longest body is 11 characters; the fixed 760px bar stays fixed.

## No hook card

EP01 opened on a 2.55s text card ("5 MYTHS, BUSTED"). Higgsfield's virality
predictor scored that opening as the flattest three seconds of every clip, and
the research on hooks is unanimous that the first frame should be the image,
not a title. EP02 opens on the second chain landing on the glass. Delete the
`card("hook", ...)` line.

## The cue detector

Use the sentence-initial ordinal detector from `ep03-graphics.md` verbatim
(`starts_sentence(i)` + the sequential `used` guard). EP02 has four decoys and
the detector clears all of them:

| Decoy | Where | Why it is skipped |
|---|---|---|
| "**Two** chains." | clip 1, word 1 | `i > 0` fails — no preceding word |
| "**Five** tests to find it." | clip 1, ~4s | badge 5 is only searched after badge 4 |
| "**One** of these is fading." | clip 2, ~28s | badge 1 already claimed at ~6s |
| "**Five** stores, Grand Strand." | clip 3, end | after badge 5 |

"Only **one's** real" and "This **one's** real" are `ONE'S`, never `ONE`.

Predicted cues, storyboard-derived (never burn these — re-transcribe):

| Badge | Predicted | Beat |
|---|---|---|
| 1 | ~5.8s | clip 1 cut 4 |
| 2 | ~11.5s | clip 1 cut 7 |
| 3 | ~17.0s | clip 2 cut 2 |
| 4 | ~22.6s | clip 2 cut 5 |
| 5 | ~31.2s | clip 3 cut 2 |

## Holds

`HOLD = 1.9` for all five. There is no question-to-answer relay across the clip
cuts in this episode (the held beats are "still can't tell" and "one of these is
fading"), so the EP03 bridge holds do not apply.

## Closing card and the end

The standard series card (`FREE APPRAISAL - NO OBLIGATION` / `5 STORES - (843)
646-7166` / `SHIPS ANYWHERE IN THE US`) rises on the **detected scene cut before
"Five stores"** — clip 3 cut 8, the arms-open wide — and the master ends
**0.45s after the last word**, not on a held card. `DUR = last_word_end + 0.45`,
exactly as `burn-ad.py` does it.

## Transcription fixes

```python
FIX = {"PONCHING":"PAWNING", "STRAIN":"STRAND", "STRAD":"STRAND", "LOOP":"LOUPE", "LOUP":"LOUPE"}
```

Read the printed captions before accepting the build. "Loupe" is the new word
most likely to misfire.

## The one designed fallback

If the full-resolution acid beat (clip 2 cut 7) does not fizz the way the smoke
test did, keep the audio and replace the picture for that beat with a full-bleed
card from `factcard.py`: kicker `FACT`, big line `GOLD SITS THERE.`, rule, sub
`FAKE FIZZES AND FADES.` That is the EP01 mailer fix again — free, and planned
rather than patched.
