# Dick's Pawn Superstore — "Behind the Counter" video series
## Handoff packet · everything needed to rebuild or continue the series

**Prepared by:** Kyle Fries Marketing — Kyle Fries · Kylefriesmarketing@gmail.com · 806-544-8098
**Client:** Dick's Pawn Superstore, Grand Strand, South Carolina (contact: Jill)
**Status:** Episode 1 is produced and delivered. Episodes 2–5 are written and unproduced.
**Date:** 18 September 2026

---

## 0. Read this part first — the tool gap

Episode 1 was generated on **Higgsfield**, using **Seedance 2.5** (ByteDance) for
the video. That model produces 15-second 9:16 clips with **native synchronised
speech** from a text prompt plus reference images — the host's voice in the
finished video is not dubbed, not TTS, and not lip-synced afterwards. It comes
out of the video model itself, in one pass.

**You almost certainly do not have that model.** Plan around it honestly:

| Job | What was used | Closest thing you likely have |
|---|---|---|
| Locked host portrait | `soul_2` (Higgsfield) | Any strong image model — this is the easiest piece to reproduce |
| 21:9 eight-slot storyboards | `gpt_image_2` | Same — image generation is the portable part |
| 15s talking clip w/ native voice | `seedance_2_5` omni_reference | **Sora, or an equivalent video model.** If yours has no synchronised speech, you must split it: silent video + separate TTS + lip-sync pass, and you will lose the natural mouth timing that makes this format work |
| Post-production | ffmpeg + faster-whisper + libass | Same tools, any Linux box |

Everything in sections 1–7 below is **model-agnostic**. The specs, the script,
the claim rules, the beat structure and the graphics spec all port cleanly.
Section 8 is the paid-for list of traps — read it before spending a single
credit anywhere, because most of those traps are properties of diffusion models
in general, not of Seedance specifically.

**One honest warning about the voice.** If your pipeline cannot produce
synchronised native speech, do not simply generate silent footage and narrate
over it. This format lives or dies on the host appearing to actually say the
lines to camera. A voiceover over B-roll is a different, weaker format — still
worth making, but do not present it as the same thing.

---

## 1. What is in this packet

```
00-START-HERE.md              ← you are here
01-series-bible.md            The format, the host, the claim allowlist, all 5 episode scripts
02-prompts/
  00-runbook.md               Costs, run order, defect triage, the three things that bite
  01-character.md             The locked host prompt + why the logo cannot be prompted
  02-boards.md                The eight-slot storyboard prompts (all 3 boards, verbatim)
  03-clips.md                 The three 15s clip prompts (verbatim, cut by cut)
  04-post-production-notes.md How EP01 was assembled, the two defects, the graphics spec
03-reference/
  super-dick-host-LOCKED.jpg  THE host. Every frame of the series derives from this one file
  dicks-pawn-logo.png         The real diamond-D mark. Composite it; never prompt it
  ep01-board1..3.jpg          The three storyboards actually used
  ep01-final-frames.jpg       Contact sheet of the finished video
  ep01-clips-raw.jpg          Contact sheet of the raw clips, before edit
  ep01-fact-card.jpg          The designed card that replaced one bad beat
  store-photos/01..04.jpg     Real photographs of the store — the set ground truth
04-build/
  burn.py                     The graphics burn, exactly as run
  factcard.py                 The replacement-card generator
  caps.ass                    The finished caption track
05-full-conversation.md       The complete client conversation, 136 turns, unedited
06-final-video/
  ep01-5-myths-720p.mp4       The finished episode (720p reference copy, 5.4 MB)
07-commercial/
  dicks-pawn-proposal-and-agreement.pdf   The signed-form proposal + agreement
```

`05-full-conversation.md` is the raw record — every client instruction, every
correction, every reversal, in order. If something in this brief seems
arbitrary, the reason is in there. Two things worth knowing about it: the client
changes his mind (the editor's cost was included, then removed), and the later
half is about the contract, not the video.

---

## 2. The format

One host. One counter. One numbered list. Forty-five seconds, vertical.

Three 15-second clips, hard-cut together. Each clip is **eight internal beats**
of roughly 1.9 seconds. Red numerals burn in on the counting beats.

It works for three reasons, and all three are worth preserving:

1. **The number is a progress bar.** "Five myths" promises an end. Viewers stay
   for the countdown — that is what carries retention past the 3-second cliff.
2. **Myth-busting is argument bait.** Half the comments will be people insisting
   the myth is true. That is the algorithm's favourite signal.
3. **It costs nothing to repeat.** Same host, same counter, same light. Only the
   list changes. Episode 12 is as cheap as episode 2.

The format is a container. The series bible fills it.

---

## 3. The host — "Super Dick"

The client's About page already promises him: *"if you spot Super Dick around
town — that's our promise on the move."* The logo is a diamond cut into a hero
shield. The brand was already superhero-coded; the series just puts a face on it.

**He is a man in a polo with a cape, not a costume.** A foam mascot head cannot
lip-sync, cannot hold an expression, and reads as uncanny. A real guy working the
counter who happens to be wearing a cape is funnier, warmer, and renders cleanly.

| Axis | Locked value |
|---|---|
| Age / read | Late thirties, American, coastal-Carolina everyman |
| Build | Athletic-but-normal, broad shoulders, well-proportioned |
| Hair | Short dark brown, neat, slightly tousled at the front |
| Face | Light stubble, faint laugh lines, natural skin texture, visible pores |
| Top | Navy `#133564` short-sleeve **cotton pique** work polo, collar open |
| Emblem | The real diamond-D, **composited in post** at 150px on the left chest |
| Cape | Rich gold `#c9a24b` satin, tied at the throat, over BOTH shoulders |
| Head | Bare. Own hair. No cowl, no mask, ever |
| Voice | Warm, dry-witted, conversational — never salesy |
| Accent | Neutral American. No forced drawl |

**Persona sentence — carry verbatim into every prompt or the performance drifts:**

> A warm, dry-witted counter guy who has heard every myth a thousand times and
> enjoys knocking them down — easy-going, conversational, never salesy.

### Three wardrobe findings that cost real money to learn

**The garment decides the realism.** A spandex superhero suit renders as CGI
almost regardless of prompt — smooth synthetic fabric has no weave, no wrinkle
behaviour and no matte falloff, so the model has nothing to render honestly and
defaults to flat saturated colour. A **cotton pique polo** forces visible knit,
creasing at the sleeve hems and rumpling at the shoulders. Every photoreal
version in this series is cotton; every plastic-looking one is spandex.

**No head covering.** A cowl prompted plainly renders as a swim cap; prompted
with structure it renders as a balaclava with eye holes. Beyond looking wrong, a
masked figure in a video whose first line is "it's all stolen" is the worst
available optic. Bare head keeps the whole face readable for lip-sync anyway.

**The cape is gold, not red.** Navy + red is Superman's palette and the logo is
already a shield. Gold ties to Dick's Bullion, catches shop light, and keeps red
free to mean one thing only — the on-screen numerals and the CTA. Three colours,
three jobs: navy is the host and the counter world, gold is the hero accent,
red is numbers and calls to action and nothing else.

### The logo problem, and how it was actually solved

The obvious move is to prompt the diamond onto his chest. **It does not work.**
Four separate attempts, all failing the same way:

| Chest instruction | Result |
|---|---|
| "small embroidered diamond crest badge" | Diamond rendered, filled with gibberish letters |
| "solid flat diamond patch, no lettering, no interior detail" | Bigger blue sticker, still gibberish |
| "plain navy, NO patch, NO badge" | Clean, but no mark at all |
| "diamond shield emblem, deep blue, white and red border" | Rendered as a Superman shield, not their diamond |

Image models hallucinate lettering into any branded shape, and negating it ("no
text") makes it worse — the model attends to the noun and drops the negation.

**The fix is compositing, not prompting.** Generate a completely plain polo, then
composite the real `dicks-pawn-logo.png` onto the chest:

```bash
convert dicks-pawn-logo.png -resize 150x150 lg.png
composite -geometry +455+1155 lg.png host.png super-dick-host.png
```

150px at 1536×2048, left chest. Larger crowds the cape; smaller stops reading
once there is motion. `03-reference/super-dick-host-LOCKED.jpg` is the finished
result — **use that file directly** rather than rebuilding it.

What this buys and does not buy: the character reference now carries the real
logo, so every downstream frame renders a far closer likeness than a described
one would. But a video model still **repaints** it each frame — expect a good
approximation on screen, not a pixel-exact mark. For a genuinely exact logo,
trust the persistent corner logo burned in post, which already is exact.

### Never regenerate the host

One image, reused across the entire series, referenced by every board and every
clip. Regenerating it mid-series is how a series quietly loses its face between
episodes. If you rebuild the host on a different model, rebuild **all five
episodes** on that host — do not mix.

---

## 4. The set

An early read of the store photos made knotty pine the dominant wall and produced
rooms that did not look like the shop. The client's exact words: *"the background
doesn't look enough like the reference photos way to much pine wall."* The real
ratio is the reverse:

- **White horizontal-grooved slatwall is most of the wall**, densely hung with merchandise
- **Knotty pine is accent columns and trim** between the slatwall panels
- Drop ceiling of acoustic tiles with recessed fluorescent panels **and** black track-lighting rails
- Warm medium-brown wood-look plank laminate floor
- Counters: grey speckled laminate tops, wood-panelled fronts, navy blue trim
- Glass cases lit and packed with gold chains
- A row of hanging guitars on the back wall (Dick's Music is a real department)

And the store is **busy**. Sparse, tidy renders read as a showroom; the real place
is stocked wall to wall. Say *"cluttered, well-stocked, lived-in — a working shop,
not a showroom"* and it lands.

`03-reference/store-photos/` holds four real photographs of the actual store.
Check every render against them before accepting it.

---

## 5. The claim allowlist — this is the hard rule

**Nothing goes on camera that is not on this list.** Every line is sourced from
the company's own published pages. This is not caution for its own sake — a pawn
shop making a financial claim it cannot support is a real regulatory problem,
and "we pay the most in town" is exactly the line that invites one.

| Claim | Source |
|---|---|
| Family-owned, established 1987 | about.html |
| Five locations on the Grand Strand | about.html, locations.html |
| 4.9 stars, 2,000+ Google reviews | site header, verified on the Google listing |
| BBB A+ rated | about.html |
| Member, National Pawn Brokers Association | about.html |
| Pawn loans require no credit check | sell.html FAQ |
| Not repaying a pawn loan never affects your credit score | sell.html FAQ |
| Pawned items are stored securely and fully insured | sell.html FAQ |
| SC law requires government photo ID on all pawn and buy transactions | sell.html FAQ |
| Free, no-obligation appraisals | sell.html |
| Experienced jewelers on staff at every location, every day | services.html |
| Layaway available with no credit needed | services.html |
| 14-day returns, nationwide shipping | services.html |

### Off-limits on camera

- **Firearms or weapons anywhere in frame.** This is written into every board
  prompt and every clip prompt as an explicit negative, and EP01 shipped with
  zero firearms in any frame. Real pawn shops carry them; this series does not
  show them. Platform ad policy and brand safety both point the same way.
- **Dick's Title Loans.** A legitimate service, but title lending is a regulated
  high-risk financial product and short-form video is the wrong venue. Website only.
- **Interest rates, loan terms, APR, or any "better than a bank" comparison.**
- **Any specific payout figure, percentage, or "we pay X% of value."**
- **Invented staff history.** Super Dick is a **host**, not a testimonial. He
  never says "in my fifteen years here" — he presents facts, not memories.
- **No other real brand logos** anywhere in frame.
- **No readable text baked into generation** — see §7.

---

## 6. The script (EP01, as produced) and the four unproduced episodes

Density is tuned to the render: **~30–35 spoken words per 15-second clip.** More
than that and the model rushes the delivery; less and it ad-libs to fill.
`CAPS` marks a volume spike. An em-dash marks a hard beat, not a pause.

### EP01 — 5 Myths About Pawn Shops ✅ produced

> **Clip 1 · myths 1–2**
> *[incredulous scoff]* Five myths about pawn shops. Number one — it's ALL stolen.
> South Carolina law: every transaction takes a government photo ID. Number two —
> it's all junk. We keep real jewelers on staff, every store.
>
> **Clip 2 · myths 3–4**
> Number three — pawning hurts your credit. It CAN'T. No credit check, and it
> never touches your score. Number four — your stuff disappears. It's stored safe
> and insured till you come get it.
>
> **Clip 3 · myth 5 + CTA**
> Number five — we're hoping you never pay it back. Wrong again. We'd rather see
> you walk out with your ring than keep it. Family-owned since nineteen
> eighty-seven. Five stores, Grand Strand.

The bracketed scoff is a clip-1-only opener device. Clips 2 and 3 open
mid-thought — no greeting, no re-introduction. The viewer never left.

**EP02–EP05 are fully written in `01-series-bible.md` §4** — "5 Questions We Get
Every Single Day", "5 Things You Didn't Know We Take", "5 Things We Do That
Aren't Pawn", and "5 Mistakes People Make Before Walking In". They are scripted
to the same density and drawn from the same allowlist. They are ready to shoot.

---

## 7. How a clip is actually built

### 7a. The eight-slot storyboard

Each storyboard is **one ultra-wide 21:9 sheet containing exactly eight 9:16
vertical slots in a single horizontal row**, white gutters, white background.
Those eight slots become the eight internal hard cuts of one 15-second clip.

Two things about this that matter more than they look:

**Generate the boards sequentially, never in parallel.** Board K passes board
K−1 as a trailing reference image, so the counter, the light direction and the
guitar wall stay put across the whole 45 seconds. Submitting them in parallel
breaks continuity and you will see the room change between clips.

**Every adjacent pair of slots must differ in both POV and distance band.** A
different camera setup (selfie vs. locked-off static), a different distance
(tight/macro vs. medium vs. wide), and a different action. That is what makes
each beat boundary read as a crisp hard cut rather than a morph.

The full prompts — header block, eight slot lines, footer block, all three
boards — are in `02-prompts/02-boards.md`, verbatim and ready to copy.

### 7b. The clip, and the six rules that break it

Cut timings are fixed for 15 seconds and must sum exactly:

```
0-1.9 · 1.9-3.8 · 3.8-5.6 · 5.6-7.5 · 7.5-9.4 · 9.4-11.3 · 11.3-13.1 · 13.1-15
```

1. **`Hard cut to.` verbatim at the end of cuts 1–7.** Seven markers, none after
   cut 8. Without them the eight beats melt into one continuous shot.
2. **Static cuts say *locked-off, zero movement*.** Never write `handheld`,
   `drift`, `sway` or `micro-shake` inside a static cut — the words leak motion in.
3. **Selfie cuts never mention the phone as an object.** The camera *is* the
   phone. Writing "holds the phone" makes the model show a man holding a phone.
4. **The voice starts within 0.4s of frame one, and frame one is already
   mid-motion.** A clip that opens at rest is dead before its first sentence.
5. **Two hands, always.** Count the hand roles in every cut. More than two spawns
   a third arm — this happens constantly and it is entirely preventable.
6. **Clips 2 and 3 open mid-thought.** No greeting, no re-introduction.

The three complete clip prompts are in `02-prompts/03-clips.md`, cut by cut.

### 7c. Post-production — the part that is fully portable

All of this is ffmpeg, faster-whisper and libass. It runs anywhere.

**Assemble in one encode.** Trim, concat and loudness-normalise together —
and normalise **each clip to −14 LUFS before the concat**, not once at the end.
Clips come back up to 3 dB apart and a global pass leaves that step audible.

One gotcha: `aresample` after `loudnorm` drops the channel layout and the filter
graph dies with *"Cannot select channel layout."* Always follow `loudnorm` with
`aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo`.

**Then re-transcribe the assembled master, at word level.** Every graphic is
timed from the real audio of the real edit — never from a pre-edit timing shifted
by arithmetic. **Measure, don't offset.**

This matters more than it sounds. Because the timings come from the real audio,
each badge also lands in sync with the host's counting hand — badge "1" appears
while he is holding up one finger, badge "5" while his hand is open with five.
Timing from the script would drift, because the model distributes its eight beats
slightly differently every single time.

EP01's measured badge cues, post-cut: **1 → 2.72s · 2 → 8.62s · 3 → 13.82s ·
4 → 21.80s · 5 → 28.82s.**

**Graphics spec (EP01, as shipped):**

| Element | Spec |
|---|---|
| Numeral badge | Red `#d63031`, 170×170, at (80, 220), Montserrat ExtraBold |
| Label bar | Navy `#133564`, **fixed 760×170** at (250, 220), 90% opacity |
| Kicker | Gold `#c9a24b` "MYTH", 32px |
| Myth text | White, 42px |
| Hold | 1.9s |
| Logo | `dicks-pawn-logo.png` at 140px, bottom-left, persistent |
| Captions | ASS track via libass, two styles: `Cap` MarginV 300, `CapHigh` MarginV 610 |

The label bar is a **fixed width regardless of text length** so the five cards
read as one system rather than five different widths. Don't let it auto-size.

**The myths are labelled as myths on purpose.** "ALL STOLEN" in large type on a
pawn shop's own video is a bad screenshot unless it is unmistakably framed as the
claim being debunked. The gold "MYTH" kicker does that work. **Do not drop it.**

Captions are burned for the full script — the client asked for this explicitly,
and it is correct: most of these views are sound-off.

**Use a subtitle track, not stacked drawtext.** Thirty-seven caption events as
individual `drawtext` filters is unmanageable and slow; one `.ass` file through
`subtitles=caps.ass:fontsdir=...` is clean, fast and editable.

**Fix the transcriber's proper nouns.** Whisper reliably mangles two words in
this script: *"pawning"* → "ponching", and *"Grand Strand"* → "grand strain" or
"grand strad". `burn.py` carries an explicit `FIX` dict for exactly this. Any
new episode will need its own.

`04-build/burn.py` is the real script, as run. It is ~170 lines and readable.

---

## 8. Every trap already paid for

Read this section before generating anything. Most of these are properties of
diffusion video models in general, not of one vendor's model.

### Never bake text into generation

Numbers, signage, price tags, the logo — all of it renders as gibberish lettering
and none of it is editable afterwards. Burn every piece of text in post, where it
is crisp, on-brand, and one line of code away from being changed. This is also
why the host's polo is generated **completely plain**.

### Triage a bad defect before paying to re-render it

The model ships defects at a fairly steady rate — an ad-lib, a repeated line, a
cutaway to something irrelevant. **Almost none of them need a re-render.** A
re-roll is expensive *and* non-deterministic: it may hand you a different defect,
and it will certainly hand you different timings, invalidating every cue you measured.

The eight-slot structure is what makes defects cheap to fix. Eight beats means
eight hard cuts the model has already made, and a defect inside one beat can be
removed or replaced on those boundaries with no visible seam.

Work it in this order:

1. **Transcribe the raw clip** and read it against the script. This catches
   repeated lines, ad-libs and dropped words that a contact sheet never will.
2. **List the scene cuts** — `select=gt(scene,0.35)` finds the model's own beat boundaries.
3. **Is the defect bounded by two cuts?** Cut that beat out. Free, seamless.
4. **Is the audio over it worth keeping?** If the picture is bad but the line is a
   claim you want, keep the track and replace only the *picture* for that beat
   with a designed full-bleed card. Free, and usually better than what it replaced.
5. **Only then consider a re-render.** By this point you will rarely need one.

**EP01 hit cases 3 and 4 in the same build and shipped without re-rendering either:**

- *Clip 1 delivered "Number two, it's all junk" twice* — at 8.46–9.72 and again at
  10.26–12.10. The duplicate sat entirely inside one beat bounded by the model's
  own hard cuts, so `8.333 → 10.083` came out losslessly. The *second* delivery
  was kept, because the beat after it is the two-finger close-up.
- *Clip 2 put a blank gold card beside a padded shipping mailer* under the line
  "no credit check… never touches your score" — accidentally the visual language
  of a credit-card offer arriving in the mail, which is the exact opposite of the
  claim. The audio was worth keeping, so only the picture was replaced, with a
  designed full-bleed fact card (`03-reference/ep01-fact-card.jpg`, generated by
  `04-build/factcard.py`).

### Check the pixels before paying

A downscaled contact sheet is for spotting candidates, not judging them. Pull
full-resolution frames, and for a colour question sample the region's mean RGB
across the beat. One earlier build nearly paid for a re-render to fix what turned
out to be blown-out backlight that merely *looked* like a wardrobe break.

### QA checklist before stitching

Evenly spaced frames plus 2–3 mid-word frames, checked for: doubled lip edges, a
third hand, face drift between cuts, wardrobe changes, and baked-in text. Re-run
only the failing clip index, never the batch.

### Watch for a preset intercepting your submission

On Higgsfield, a batch submission can come back `submission_failed` saying a
preset "was recommended instead of submitting a job" — no job created, nothing
charged. This run was offered a preset called "IN THE DARK", which would have
thrown a moody night grade over a bright daylight pawn shop. **Never accept a
preset you did not choose**; it silently overrides the entire Style & Mood block.
If your platform has an equivalent auto-styling feature, turn it off.

### Read what the API actually ran

Reference-image roles get silently coerced (`role: "image"` → `image_references`).
Harmless in itself, but it means the parameters you wrote are not always the
parameters that ran. Read the response's adjustments rather than assuming.

---

## 9. What EP01 actually is, as a file

**`06-final-video/ep01-5-myths-720p.mp4`** — 43.5s · 720×1280 · h264 + AAC · 5.4 MB.

This is a **downscaled reference copy** for review. The delivered master is
**1080×1920, 27.2 MB**, mean −18.6 dB, peak −1.4 dB, 37 caption events, zero
caption overlaps, ready to post to TikTok, Reels and Shorts as-is.

Watch it before rebuilding anything. It is the target.

---

## 10. The commercial context

`07-commercial/dicks-pawn-proposal-and-agreement.pdf` is the live proposal and
agreement with the client. Relevant facts if you are producing against it:

- **$5,000/month**, cancel any time, no term commitment, no notice period.
- Cadence starts at **one video per week** while the pipeline is proven, with an
  explicit stated goal of ramping to 2–4 per week as it stabilises.
- Videos are **posted, maintained and analysed** across Instagram, Facebook and
  TikTok — production is not the whole job.
- **AI generation is disclosed to the client in writing, on page 1.** Keep it
  that way. Do not let anything in this pipeline become something the client did
  not knowingly agree to.
- There is a **$10,000/month** full-production tier (location crew, lighting,
  sound, hired talent). The $5,000 tier is the AI-host pipeline in this packet
  plus in-store filming with the client's own staff.
- **No results are guaranteed.** Nothing in any deliverable should imply a
  promised outcome, reach number, or revenue figure.

---

## 11. If you are rebuilding EP01 from scratch

Shortest honest path:

1. **Use `03-reference/super-dick-host-LOCKED.jpg` as-is.** Do not regenerate the
   host. It already carries the real logo composited at the right size, and it is
   the single point of continuity for the whole series.
2. **Generate three storyboards sequentially** from `02-prompts/02-boards.md`,
   each chaining the previous one. Check them against `03-reference/ep01-board1..3.jpg`
   and against the real store photos.
3. **Generate three 15s clips** from `02-prompts/03-clips.md`. Honour the six
   rules in §7b exactly — they are the difference between eight hard cuts and one
   mushy continuous shot.
4. **Transcribe and triage before assembling.** §8. This is free and it is where
   the defects are.
5. **Assemble in one encode**, per-clip loudness normalisation, then re-transcribe
   the master at word level.
6. **Burn the graphics** with `04-build/burn.py` against your new timings.

If your video model cannot do native synchronised speech, stop at step 3 and
decide deliberately how you are handling voice — do not discover it at step 5.

---

*Questions on any of this: Kyle Fries · Kylefriesmarketing@gmail.com · 806-544-8098*
