# Output

## `ep01-5-myths-FINAL.mp4` — the deliverable

**43.4s · 1080×1920 · h264 + AAC · 28.6 MB** — ready to post to TikTok, Reels
and Shorts as-is. Fully captioned.

"5 Myths About Pawn Shops", hosted by Super Dick behind the jewelry counter.
Three 15-second Seedance 2.5 clips stitched with hard cuts, then the graphics
burned on: a red numbered badge, a navy bar carrying a gold "MYTH" kicker and
the myth in white, and the real diamond-D logo bottom-left.

**The myths are labelled as myths on purpose.** "IT'S ALL STOLEN" in large type
on a pawn shop's own video is a bad screenshot unless it is unmistakably framed
as the claim being debunked. The gold kicker does that work; don't drop it.

The label bar is a fixed 760px regardless of text length so the five cards read
as one system rather than five different widths.

### How the numbers were placed

Not by planned beats — by a **word-level Whisper transcript of the finished
audio**. The badge appears on the frame where the word is actually spoken:

| Badge | Spoken at |
|---|---|
| 1 | 2.78s |
| 2 | 8.96s |
| 3 | 13.58s |
| 4 | 21.30s |
| 5 | 28.14s |

These are the **post-cut** cues. When the ad-lib beat was removed the whole
timeline shifted, so the audio was re-transcribed rather than the old numbers
being shifted by arithmetic. Measure, don't offset — it is the same discipline
that put the badges on the spoken word in the first place.

This matters more than it sounds. Because the timings came from the real audio,
each badge also lands in sync with the host's counting hand — badge "1" appears
while he's holding up one finger, badge "5" while his hand is open with five.
Timing them from the script would have drifted, because Seedance distributes the
eight beats slightly differently from the plan every time.

Graphics spec: red `#d63031` badge 170×170 at (80, 220); navy `#133564` bar
760×170 at (250, 220) at 90% opacity; gold `#c9a24b` "MYTH" kicker at 32px;
white myth text at 42px; all Montserrat ExtraBold, ~1.9s hold. Logo scaled to
140px, bottom-left — it moved down from top-right when the label bar took over
the top strip.

### ffmpeg gotcha that cost a render

Myths 1 and 2 first came back with the badge and kicker but **no myth text**.
Both contain an apostrophe ("IT'S"), and passing them through `text=` inside a
`-filter_complex` string meant the quote had to survive both shell and ffmpeg
filter parsing. It didn't — ffmpeg silently drew an empty string rather than
erroring, so the render "succeeded" and only a frame check caught it.

Use `textfile=` and write each label to its own file. It sidesteps filter
escaping completely and any punctuation is then safe.

Two smaller ones from the same pass: ffmpeg refuses to overwrite an existing
output and will hang the script waiting on a prompt, so pass `-y`; and
re-uploading to an already-fetched presigned URL serves the **stale** file from
the CDN edge for a while, so reserve a fresh `media_upload` for each revision
rather than reusing the slot.

## The ad-lib cut

Seedance improvised a line at ~4.9s that Whisper read as *"Come on, it's Olin"* —
almost certainly a slurred re-emphasis of "it's stolen". It was the weakest
second in the video.

It was removed for free, with no visual seam, by cutting **4.500 → 6.375s**.
That span is exactly one beat, bounded on both sides by hard cuts the model had
already made (scene detection put them at 4.5 and 6.375), and the transcript
confirmed it contained the ad-lib and nothing else — "stolen" ends at 4.38,
"South" begins at 6.60.

**When generated speech goes wrong, look for the beat boundaries before paying
to re-render.** An eight-cut clip gives you eight places to cut losslessly. The
re-roll would have been 135 credits and non-deterministic — it might have
produced a different ad-lib.

The audio was also loudness-normalised to −14 LUFS (the social platform target)
in the same pass, lifting the mean from −23.9 dB to −18.2 dB.

## On-screen graphics

| Element | Timing | Content |
|---|---|---|
| Hook card | 0 – 2.55s | DICK'S PAWN SUPERSTORE / 5 MYTHS, BUSTED |
| Myth cards | on each cue | badge + MYTH kicker + the claim |
| URL | persistent | dickspawn.com, top-right |
| CTA card | 37.6s – end | FREE APPRAISAL - NO OBLIGATION / 5 STORES - (843) 646-7166 / SHIPS ANYWHERE IN THE US |
| Captions | whole script | lower third, white on black outline |
| Logo | persistent | bottom-left |

The URL sits at y=112, above the y=220 card strip, so it never collides. The
cards all share one geometry (170px tall, navy, gold kicker over white body) so
the hook, the five myths and the CTA read as one system.

## Claim check on the closing card

"Ships anywhere in the US" was verified against the site before it went on
screen — `index.html` and `services.html` both state nationwide shipping. Every
on-screen claim traces to a page in this repo; see the allowlist in the series
bible. **Nothing goes on a card that isn't already published.**

## Captions

Burned from the same word-level Whisper transcript, as an **ASS subtitle track**
rather than ~37 stacked `drawtext` filters. libass handles timing, wrapping and
escaping natively — which is exactly where the apostrophe bug bit — and the
style lives in one place instead of being repeated per line.

Chunking: at most 3 words or 22 characters, broken early on a sentence end or a
gap over 0.55s. The sentence-end rule matters — without it lines ran across
sentences ("ALL STOLEN. SOUTH"), which reads badly at speed.

Two corrections the transcript needed before burning:

- **Whisper heard "Grand Strand" as "grand strad."** Burned in, that would have
  misspelled the region the whole business is named around. A `FIX` map in the
  build corrects local proper nouns; add to it per episode.
- **37 chunks produced 20 overlapping pairs** once end times were padded by
  0.06s for readability. Overlapping ASS events stack on screen. Each end time
  is now clamped to the next start minus 0.01s.

**Never burn a machine transcript without reading it first.** It will be right
about the common words and wrong about exactly the proper nouns that matter to
a local advertiser.

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
