# Output

## `ep01-5-myths-FINAL.mp4` — the deliverable

**45.2s · 1080×1920 · h264 + AAC · 28.8 MB** — ready to post to TikTok, Reels
and Shorts as-is.

"5 Myths About Pawn Shops", hosted by Super Dick behind the jewelry counter.
Three 15-second Seedance 2.5 clips stitched with hard cuts, red brand badges
burned on the numbers, and the real diamond-D logo composited top-right.

### How the numbers were placed

Not by planned beats — by a **word-level Whisper transcript of the finished
audio**. The badge appears on the frame where the word is actually spoken:

| Badge | Spoken at |
|---|---|
| 1 | 2.72s |
| 2 | 10.75s |
| 3 | 15.68s |
| 4 | 23.22s |
| 5 | 30.12s |

This matters more than it sounds. Because the timings came from the real audio,
each badge also lands in sync with the host's counting hand — badge "1" appears
while he's holding up one finger, badge "5" while his hand is open with five.
Timing them from the script would have drifted, because Seedance distributes the
eight beats slightly differently from the plan every time.

Graphics spec: red `#d63031` badge, 170×170 at (80, 220), white Montserrat
ExtraBold numeral, ~1.9s hold. Logo scaled to 150px at top-right.

## Measured QA — all three clips

| Check | Clip 1 | Clip 2 | Clip 3 |
|---|---|---|---|
| Resolution | 1080×1920 | 1080×1920 | 1080×1920 |
| Hard cuts detected | 7 | 7 | 5 |
| Audio mean / peak (dB) | −23.9 / −3.2 | −24.9 / −3.7 | −22.4 / −2.8 |
| Identity holds across cuts | yes | yes | yes |
| Baked-in text | none | none | none |

Clip 3 registers 5 scene cuts rather than 7 because two of its boundaries fall
between visually similar wide shots and sit under the 0.35 detection threshold —
the beats are present in the frames, the detector just doesn't flag them.

### One false alarm worth recording

Clip 2's beat-4 thumbnail looked like the navy polo had turned **white** — a
wardrobe break that would have cost a 135-credit re-run. It wasn't one. Sampling
the chest region's mean RGB across the beat returned dark/navy on every frame,
and full-resolution crops confirmed it: the "white" was blown-out backlight on
his shoulder against the storefront window.

**Check the pixels before paying for a re-render.** A downscaled contact sheet
is for spotting candidates, not for judging them.

## `ep01-motion-test.mp4` — the 5-second pipeline validation

480p, 5.04s, 15 credits. Run before committing to 1080p, back when the budget was
tight. Two of board 1's eight beats at ~2.5s each, because eight cuts inside five
seconds gives each beat 0.6s — too fast to judge lip-sync. It proved the hard cut
fires, identity survives it, and the speech is continuous. Kept as the cheap
smoke test for future format changes.

## Not in git

The clean master (no burned graphics) and the individual clips are gitignored —
they'd add ~55 MB per episode. Regenerate them from `content/prompts/`, or pull:

- clean master: `https://d2ol7oe51mr4n9.cloudfront.net/user_3H46sCHMdJedqIphe86QCDd6jdZ/e1d6b662-2166-40f0-9040-3e8d9a80271c.mp4`

Keep the clean master if you plan to re-cut the graphics — re-burning from the
final would stack two generations of h264 compression.
