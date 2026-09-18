# Output

## `ep01-5-myths-FINAL.mp4` — the deliverable

**43.5s · 1080×1920 · h264 + AAC · 27.2 MB** — ready to post to TikTok, Reels
and Shorts as-is. Fully captioned.

"5 Myths About Pawn Shops", hosted by Super Dick behind the jewelry counter.
Three 15-second Seedance 2.5 clips stitched with hard cuts, then the graphics
burned on: a red numbered badge, a navy bar carrying a gold "MYTH" kicker and
the myth in white, and the real diamond-D logo bottom-left.

**The myths are labelled as myths on purpose.** "ALL STOLEN" in large type on a
pawn shop's own video is a bad screenshot unless it is unmistakably framed as
the claim being debunked. The gold kicker does that work; don't drop it.

The label bar is a fixed 760px regardless of text length so the five cards read
as one system rather than five different widths.

### How the numbers were placed

Not by planned beats — by a **word-level Whisper transcript of the finished
audio**. The badge appears on the frame where the word is actually spoken:

| Badge | Spoken at |
|---|---|
| 1 | 2.72s |
| 2 | 8.62s |
| 3 | 13.82s |
| 4 | 21.80s |
| 5 | 28.82s |

These are the **post-cut** cues, re-measured from the assembled master. The
build never shifts an old timing by arithmetic — every edit is followed by a
fresh transcription. Measure, don't offset.

This matters more than it sounds. Because the timings come from the real audio,
each badge also lands in sync with the host's counting hand — badge "1" appears
while he's holding up one finger, badge "5" while his hand is open with five.
Timing them from the script would drift, because Seedance distributes the eight
beats slightly differently from the plan every time.

Graphics spec: red `#d63031` badge 170×170 at (80, 220); navy `#133564` bar
760×170 at (250, 220) at 90% opacity; gold `#c9a24b` "MYTH" kicker at 32px;
white myth text at 42px; all Montserrat ExtraBold, 1.9s hold. Logo scaled to
140px, bottom-left.

## Two defects the raw clips shipped with

Both were caught by transcribing and eyeballing the clips **before** assembly,
and both were fixed for free. Neither needed a re-render.

### 1. Clip 1 said "Number two, it's all junk" twice

Seedance delivered the line, cut, and delivered it again. The transcript found
it immediately; the scene-cut list showed why it was cheap to fix:

```
 8.46 – 9.72   "Number two, it's all junk."   <- first, inside beat [8.333, 10.083)
10.26 – 12.10  "Number two, it's all junk."   <- second, kept
```

The duplicate sat **entirely inside one beat**, bounded on both sides by hard
cuts the model had already made. Cutting `8.333 → 10.083` removes it with no
visual seam — and the join still registers as a scene cut in the master, which
is the proof that the two shots either side are distinct enough to read as an
intentional cut rather than a jump.

The second delivery was kept rather than the first because the beat that follows
it is the two-finger close-up — the best shot for myth 2.

### 2. Clip 2 cut away to a shipping mailer

For the full beat `[6.208, 8.125)` the host vanishes and the shot is a blank
gold card being set down next to a **padded mailing envelope** on a granite
counter. The line underneath it is *"no credit check, and it never touches your
score."*

A blank gold card beside a mailer is the visual language of a credit-card offer
arriving in the post — the exact opposite of the claim being made. It had to go.

But the audio over it carries a claim worth keeping, so the beat could not just
be cut like the duplicate above. Instead the **video** for that beat is replaced
by a full-bleed fact card (`content/build/factcard.py`) reading NO CREDIT CHECK
/ IT NEVER TOUCHES YOUR CREDIT SCORE, with the audio untouched.

That turns the worst 1.9 seconds in the video into the strongest: the single
most persuasive fact in the script now gets the whole frame, and it is bracketed
by the same hard cuts as every other beat, so it reads as a deliberate emphasis
card rather than a patch.

**When a generated beat is wrong, check whether the audio over it is worth
keeping before reaching for the re-roll.** If it isn't, cut on the model's own
beat boundaries. If it is, replace the picture and keep the track. A 1080p
re-render is 135 credits and non-deterministic — it may hand you a different
defect.

## Transcript corrections

Whisper got the common words right and the proper nouns wrong, again:

| Heard | Burned |
|---|---|
| "ponching" | PAWNING |
| "grand strain" | GRAND STRAND |

Last build it was "grand strad"; this build it was "grand strain". The `FIX` map
in `content/build/burn.py` carries both, plus "strad". **Never burn a machine
transcript without reading it first** — it will be wrong about exactly the
proper nouns that matter to a local advertiser, and "Grand Strand" is the region
the business is named around.

## On-screen graphics

| Element | Timing | Content |
|---|---|---|
| Hook card | 0 – 2.55s | DICK'S PAWN SUPERSTORE / 5 MYTHS, BUSTED |
| Myth cards | on each spoken cue | badge + MYTH kicker + the claim |
| Fact card | 19.54 – 21.46s | full-bleed NO CREDIT CHECK |
| URL | persistent | dickspawn.com, top-right |
| CTA card | 38.46s – end | FREE APPRAISAL - NO OBLIGATION / 5 STORES - (843) 646-7166 / SHIPS ANYWHERE IN THE US |
| Captions | whole script | lower third, white on black outline |
| Logo | persistent | bottom-left (suppressed under the fact card, which carries its own) |

The URL sits at y=112, above the y=220 card strip, so it never collides. The
cards all share one geometry (170px tall, navy, gold kicker over white body) so
the hook, the five myths and the CTA read as one system.

The CTA is anchored to the **detected scene cut at 38.458s**, which falls 0.1s
before "Family owned since 1987" — so the card comes up on the cut exactly as
he starts the closing credentials, over the arms-wide shot.

### Captions get lifted over the closing card

At the CTA the caption "FAMILY OWNED SINCE" landed directly under the card in
the same white, and read as a dangling fourth line of it. The four caption
events that overlap the CTA are now switched to a second ASS style with
`MarginV 610`, which puts them *above* the card with a clean gap.

Worth doing rather than simply dropping the captions there: the spoken line at
that moment (credentials) is different information from the card (appraisal,
phone, shipping), so a sound-off viewer would have lost half the close.

## Claim check on the closing card

"Ships anywhere in the US" was verified against the site before it went on
screen — `index.html` and `services.html` both state nationwide shipping. Every
on-screen claim traces to a page in this repo; see the allowlist in the series
bible. **Nothing goes on a card that isn't already published.**

## Captions

Burned from the same word-level Whisper transcript, as an **ASS subtitle track**
rather than ~37 stacked `drawtext` filters. libass handles timing, wrapping and
escaping natively, and the style lives in one place instead of per line.

Chunking: at most 3 words or 22 characters, broken early on a sentence end or a
gap over 0.55s. The sentence-end rule matters — without it lines run across
sentences ("ALL STOLEN. SOUTH"), which reads badly at speed.

37 events, 0 overlaps. Overlapping ASS events stack on screen, so each end time
is clamped to the next start minus 0.01s after the 0.06s readability pad.

## Measured QA — all three raw clips

| Check | Clip 1 | Clip 2 | Clip 3 |
|---|---|---|---|
| Resolution | 1080×1920 | 1080×1920 | 1080×1920 |
| Duration | 15.05s | 15.05s | 15.05s |
| Hard cuts detected | 7 | 7 | 6 |
| Audio mean / peak (dB) | −22.1 / −2.2 | −21.0 / −2.1 | −24.2 / −4.3 |
| Identity holds across cuts | yes | yes | yes |
| Baked-in text | none | none | none |
| Firearms in frame | none | none | none |

Master after assembly: 43.47s, mean −18.6 dB, peak −1.4 dB.

### Loudness is normalised per clip, not once at the end

The three clips came back 3 dB apart. A single loudnorm pass over the
concatenated audio hits −14 LUFS overall but leaves that clip-to-clip step
audible. Each clip's audio is now normalised to −14 LUFS **before** the concat,
so the level is even across the whole video.

## ffmpeg gotchas this pipeline has already paid for

- **Apostrophes in `text=`.** "IT'S" has to survive both shell and filter
  parsing, and ffmpeg draws an empty string rather than erroring — the render
  "succeeds" and only a frame check catches it. Use `textfile=`.
- **`-y`.** ffmpeg otherwise hangs the script waiting on an overwrite prompt.
- **Stale CDN on reused presigned URLs.** Re-PUTting to an already-fetched URL
  serves the old file from the edge. Reserve a fresh `media_upload` slot per
  revision — this build used three.
- **`aresample` after `loudnorm` drops the channel layout** and the filter graph
  fails to reinitialise. Use
  `aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo`.
- **`cmd &` backgrounds the whole compound**, so `cd x && ffmpeg ... &` leaves
  the following commands in the original directory looking for a log that isn't
  there. Use the sandbox's own `background:true` instead, which also gets a
  15-minute lease rather than being killed when the call returns.

## One false alarm worth keeping on record

An earlier build's clip 2 beat-4 thumbnail looked like the navy polo had turned
**white** — a wardrobe break that would have cost a 135-credit re-run. It
wasn't one. Sampling the chest region's mean RGB across the beat returned
dark/navy on every frame, and full-resolution crops confirmed it: the "white"
was blown-out backlight on his shoulder against the storefront window.

**Check the pixels before paying for a re-render.** A downscaled contact sheet
is for spotting candidates, not for judging them. The same discipline is what
confirmed the mailer cutaway above was genuinely as bad as it looked.

## `ep01-motion-test.mp4` — the 5-second pipeline validation

480p, 5.04s, 15 credits. Run before committing to 1080p, back when the budget
was tight. Two of board 1's eight beats at ~2.5s each, because eight cuts inside
five seconds gives each beat 0.6s — too fast to judge lip-sync. It proved the
hard cut fires, identity survives it, and the speech is continuous. Kept as the
cheap smoke test for future format changes.

## Reproducing the burn

`content/build/` holds the scripts, not just a description of them:

| File | What it is |
|---|---|
| `burn.py` | cues, captions and all the card filters |
| `factcard.py` | the full-bleed fact card |
| `caps.ass` | the generated subtitle track for this cut |
| `cards.txt` | the generated drawtext/drawbox chain |
| `words.json` | the word-level transcript the whole build is timed from |

They run in the Higgsfield sandbox (`sandbox_exec`), which is free — no credits
are spent on any of the post work. Only the boards and the clips cost anything.

## Why the clean master is in git

`ep01-clean-master.mp4` (35 MB, no burned graphics) is versioned alongside the
deliverable, and that is deliberate.

**Seedance output is not reproducible.** Re-running the same prompts with the
same boards and the same seedless config returns different footage — different
beat lengths, different ad-libs, a different closer. The prompts in
`content/prompts/` regenerate the *format*, not this cut. So the master is a
one-off artifact that cost 405 credits, and "regenerate it from the prompts" is
not a recovery path.

Keeping it also means the next graphics change re-burns from a clean source
instead of stacking a second generation of h264 on the finished file.

The raw per-clip files stay gitignored — the master is the same footage, already
trimmed and level-matched, so they add ~27 MB of nothing.
