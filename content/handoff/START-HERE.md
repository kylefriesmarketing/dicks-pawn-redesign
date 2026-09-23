# Dick's Pawn Superstore — "Behind the Counter"
## Build brief: **Episode 3 — "5 Questions We Get Every Single Day"**

**Prepared by:** Kyle Fries Marketing — Kyle Fries · Kylefriesmarketing@gmail.com · 806-544-8098
**Client:** Dick's Pawn Superstore, Grand Strand, South Carolina (contact: Jill)
**Date:** 23 September 2026

**Your job is EP03.** Episodes 1 and 2 are already produced and delivered — EP01
ships in this packet as the reference build, so you can see exactly what the
target looks like before you spend anything. Do not rebuild either. Match them.
(EP02, "Only One's Real", was produced in-house after this packet was first
written; its prompts ride along in `02-prompts/ep02-*.md` for reference only.)

---

## 0. Read this part first — the tool gap

EP01 was generated on **Higgsfield**, using **Seedance 2.5** (ByteDance) for the
video. That model produces 15-second 9:16 clips with **native synchronised
speech** from a text prompt plus reference images — the host's voice in the
finished video is not dubbed, not TTS, and not lip-synced afterwards. It comes
out of the video model itself, in one pass.

**You almost certainly do not have that model.** Plan around it honestly:

| Job | What was used | Closest thing you likely have |
|---|---|---|
| Locked host portrait | `soul_2` (Higgsfield) | **Already done — reuse the file in this packet.** Do not regenerate |
| 21:9 eight-slot storyboards | `gpt_image_2` | Any strong image model — this is the portable part |
| 15s talking clip w/ native voice | `seedance_2_5` omni_reference | **Sora, or equivalent.** If yours has no synchronised speech you must split it: silent video + separate TTS + lip-sync, and you will lose the natural mouth timing this format runs on |
| Post-production | ffmpeg + faster-whisper + libass | Same tools, any Linux box |

Everything else in this brief is **model-agnostic**. The specs, the script, the
claim rules, the beat structure and the graphics spec port cleanly.

**One honest warning about the voice.** If your pipeline cannot produce
synchronised native speech, do not simply generate silent footage and narrate
over it. This format lives or dies on the host appearing to actually say the
lines to camera. A voiceover over B-roll is a different, weaker format — still
worth making, but do not present it as the same thing.

---

## 1. What is in this packet

```
00-START-HERE.md              ← you are here
01-series-bible.md            Format, host, claim allowlist, all 5 episode scripts

02-prompts/
  00-runbook.md               Costs, run order, defect triage, the things that bite
  01-character.md             The locked host + why the logo cannot be prompted
  ep03-boards.md              ★ BUILD THIS — EP03's three 8-slot storyboards
  ep03-clips.md               ★ BUILD THIS — EP03's three 15s clip prompts
  ep03-graphics.md            ★ BUILD THIS — what changes in the burn for EP03
  ep01-boards.md              Reference: the produced episode's boards
  ep01-clips.md               Reference: the produced episode's clips
  post-production-notes.md    How EP01 was assembled, its two defects, its graphics

03-reference/
  super-dick-host-LOCKED.jpg  THE host. Every frame of the series derives from this
  dicks-pawn-logo.png         The real diamond-D. Composite it; never prompt it
  ep01-board1..3.jpg          EP01's boards — EP03 board 1 chains board 1 of these
  ep01-final-frames.jpg       Contact sheet of the finished EP01
  ep01-clips-raw.jpg          Contact sheet of EP01's raw clips, before edit
  ep01-fact-card.jpg          The designed card that replaced one bad beat
  store-photos/01..04.jpg     Real photographs of the store — the set ground truth

04-build/
  burn.py                     The graphics burn, as run on EP01
  factcard.py                 The replacement-card generator
  caps.ass                    EP01's finished caption track, as a format example

05-full-conversation.md       The complete client conversation, 136 turns, unedited
06-reference-video/
  ep01-5-myths-720p.mp4       EP01, finished. **The target. Watch it first**
07-commercial/
  dicks-pawn-proposal-and-agreement.pdf   The proposal + agreement
```

`05-full-conversation.md` is the raw record — every client instruction, every
correction, every reversal, in order. If something here seems arbitrary, the
reason is in there.

---

## 2. The format

One host. One counter. One numbered list. Forty-five seconds, vertical.

Three 15-second clips, hard-cut together. Each clip is **eight internal beats**
of roughly 1.9 seconds. Red numerals burn in on the counting beats.

It works for three reasons, and all three are worth preserving:

1. **The number is a progress bar.** "Five questions" promises an end. Viewers
   stay for the countdown — that is what carries retention past the 3s cliff.
2. **It is argument bait.** Half the comments will be people insisting they know
   better. That is the algorithm's favourite signal.
3. **It costs nothing to repeat.** Same host, same counter, same light. Only the
   list changes. Episode 12 is as cheap as episode 2.

### What makes EP03 different from EP01

EP01 was a **countdown**. EP03 is a **relay**: each clip ends on a question the
*next* clip answers.

| | ends on | next clip opens on |
|---|---|---|
| Clip 1 | "Two — do I need good credit?" | "You need NO credit." |
| Clip 2 | "Four — is my stuff safe?" | "Safe and insured, the whole time." |

That is a stronger retention device than a straight count and it costs nothing —
but it puts real load on four specific beats, and if you get those wrong the
episode is worse than EP01 rather than better:

- **The last beat of clips 1 and 2 must play as an unanswered question.** Brows
  up and *staying* up, mouth closing, a beat of waiting. EP01's clips ended on
  settled, satisfied faces. If these land settled, the relay breaks at the clip
  boundary — the single most expensive place in the episode to lose a viewer.
- **The first beat of clips 2 and 3 is an answer landing on frame one.** No
  windup, no breath, no re-introduction. Already mid-gesture as the frame opens.

The prompts in `ep03-clips.md` say this explicitly, in the cut text. Don't trim
those sentences to save prompt length — they are the episode's whole structure.

---

## 3. The host — "Super Dick"

The client's About page already promises him: *"if you spot Super Dick around
town — that's our promise on the move."* The logo is a diamond cut into a hero
shield. The brand was already superhero-coded; the series puts a face on it.

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

### Use the file. Do not regenerate the host.

`03-reference/super-dick-host-LOCKED.jpg` already carries the real logo
composited at the right size. One image, referenced by every board and every
clip in every episode. Regenerating it mid-series is how a series quietly loses
its face between episodes — and EP03's whole job is to look like it was shot the
same afternoon as EP01.

If you rebuild the host on a different model anyway, you have to rebuild **EP01
as well**. Do not mix.

### Three wardrobe findings that cost real money to learn

**The garment decides the realism.** A spandex superhero suit renders as CGI
almost regardless of prompt — smooth synthetic fabric has no weave, no wrinkle
behaviour and no matte falloff, so the model has nothing to render honestly and
defaults to flat saturated colour. A **cotton pique polo** forces visible knit,
creasing at the sleeve hems and rumpling at the shoulders. Every photoreal
version in this series is cotton; every plastic-looking one is spandex.

**No head covering.** A cowl prompted plainly renders as a swim cap; prompted
with structure it renders as a balaclava with eye holes. Beyond looking wrong, a
masked figure in a pawn shop video is the worst available optic. Bare head keeps
the whole face readable for lip-sync anyway.

**The cape is gold, not red.** Navy + red is Superman's palette and the logo is
already a shield. Gold ties to Dick's Bullion, catches shop light, and keeps red
free to mean one thing only — the on-screen numerals and the CTA. Three colours,
three jobs: navy is the host and the counter world, gold is the hero accent, red
is numbers and calls to action and nothing else.

### The logo problem, and how it was solved

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

**The fix is compositing, not prompting.** A completely plain polo, then the real
`dicks-pawn-logo.png` composited on:

```bash
convert dicks-pawn-logo.png -resize 150x150 lg.png
composite -geometry +455+1155 lg.png host.png super-dick-host.png
```

150px at 1536×2048, left chest. This is already done — the packet file is the
finished result. What it buys: every downstream frame renders a far closer
likeness than a described mark would. What it does not buy: a video model still
**repaints** the logo each frame, so expect a good approximation on screen, not a
pixel-exact mark. For a genuinely exact logo, trust the corner logo burned in
post — that one already is exact.

---

## 4. The set

An early EP01 read made knotty pine the dominant wall and produced rooms that did
not look like the shop. The client's exact words: *"the background doesn't look
enough like the reference photos way to much pine wall."* The real ratio is the
reverse:

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
Check every render against them.

**EP03 anchors to EP01's room, not to a fresh reading of the photos.** Board 1 of
EP03 takes EP01's board 1 as a reference image, so the counter, the light
direction and the guitar wall land where they already are. Two episodes shot in
visibly different rooms is the failure mode this avoids.

---

## 5. The claim allowlist — this is the hard rule

**Nothing goes on camera that is not on this list.** Every line is sourced from
the company's own published pages. This is not caution for its own sake — a pawn
shop making a financial claim it cannot support is a real regulatory problem.

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

**EP03 leans on this list harder than EP01 did.** Four of its five answers are
direct claims: no credit check, ID required by state law, stored safe and
insured, free no-obligation appraisal. All four are on the list. Do not let a
rewrite drift them — "no credit check" must not become "bad credit OK", and
"stored safe and insured" must not become "guaranteed".

### Off-limits on camera

- **Firearms or weapons anywhere in frame.** Written into every board and clip
  prompt as an explicit negative; EP01 shipped with zero firearms in any frame.
  Real pawn shops carry them; this series does not show them.
- **Dick's Title Loans.** Legitimate, but title lending is a regulated high-risk
  financial product and short-form video is the wrong venue. Website only.
- **Interest rates, loan terms, APR, or any "better than a bank" comparison.**
- **Any specific payout figure, percentage, or "we pay X% of value."**
  EP03's fifth answer is about *how* value is decided — brand, model, condition,
  resale. It must never become *how much*.
- **Invented staff history.** He is a **host**, not a testimonial. He never says
  "in my fifteen years here" — he presents facts, not memories.
- **No other real brand logos** anywhere in frame. See §8, the guitar wall.
- **No readable text baked into generation.** See §7c.

---

## 6. The EP03 script

Density is tuned to the render: **~30–35 spoken words per 15-second clip.** More
and the model rushes; less and it ad-libs to fill. `CAPS` marks a volume spike.
An em-dash marks a hard beat, not a pause.

> **Clip 1 · Q1, and Q2 asked** *(34 words)*
> Five questions, every day, same five. One — what's the difference between
> selling and pawning? Sell it, we keep it. Pawn it, we hold it and you come
> back. Two — do I need good credit?
>
> **Clip 2 · Q2 answered, Q3, Q4 asked** *(37 words)*
> You need NO credit. Pawn loans run on your item, not your score. Three — what
> do I bring? Your item and a government photo ID. That's South Carolina law, not
> our rule. Four — is my stuff safe?
>
> **Clip 3 · Q4 answered, Q5 + CTA** *(31 words)*
> Safe and insured, the whole time. Five — how do you decide what it's worth?
> Brand, model, condition, and what it actually resells for. Free look, no
> obligation. Five stores, Grand Strand.

**Clip 2 is the tightest in the series so far at 37 words.** If the render comes
back rushed or clips the last question, the pre-authorised trim is *"not our
rule"*, leaving "That's South Carolina law." That keeps the claim, the
attribution and the cliffhanger, and buys back three words. Make that call by
listening to the render, not by pre-emptively cutting it.

EP04–EP06 are written in `01-series-bible.md` §4 and ready when you are.

---

## 7. How a clip is built

### 7a. The eight-slot storyboard

One ultra-wide 21:9 sheet, **exactly eight 9:16 vertical slots in a single
horizontal row**, white gutters, white background. Those eight slots become the
eight internal hard cuts of one 15-second clip.

**Generate the boards sequentially, never in parallel.** Board K passes board
K−1 as a trailing reference, so the counter, the light and the guitar wall stay
put. Parallel submission breaks continuity and you will see the room change.

EP03's chain, from `ep03-boards.md`:

| Board | medias (in order) |
|---|---|
| 1 | character, **EP01 board 1 (de-slopped)** |
| 2 | character, EP03 board 1 |
| 3 | character, EP03 board 2 |

**Every adjacent pair of slots must differ in both POV and distance band** — a
different camera setup (selfie vs. locked-off static), a different distance
(tight/macro vs. medium vs. wide), a different action. That is what makes each
beat boundary read as a crisp hard cut rather than a morph.

**Every counting beat is TIGHT or MEDIUM CLOSE-UP. Never wide, never macro.** All
five of EP01's numerals landed tight or medium-close, which is why each badge
reads in sync with the counting hand — badge "1" while one finger is up, badge
"5" while the hand is open. Stage a count wide and the fingers are a few pixels
across; the badge then looks pasted on, and there is no fixing it in post.
EP03's counting beats are board 1 slots 2 and 8, board 2 slots 4 and 8, and
board 3 slot 3.

The header and footer blocks are shared across every episode and are byte-
identical in `ep01-boards.md` — copy them from there. They are the most
drift-prone text in the pipeline.

### 7b. The clip, and the eight rules that break it

Cut timings are fixed for 15 seconds and must sum exactly:

```
0-1.9 · 1.9-3.8 · 3.8-5.6 · 5.6-7.5 · 7.5-9.4 · 9.4-11.3 · 11.3-13.1 · 13.1-15
```

Six rules carried from EP01:

1. **`Hard cut to.` verbatim at the end of cuts 1–7.** Seven markers, none after
   cut 8. Without them the eight beats melt into one continuous shot.
2. **Static cuts say *locked-off, zero movement*.** Never write `handheld`,
   `drift`, `sway` or `micro-shake` inside a static cut — the words leak motion in.
3. **Selfie cuts never mention the phone as an object.** The camera *is* the
   phone. Writing "holds the phone" makes the model show a man holding a phone.
4. **The voice starts within 0.4s of frame one, and frame one is already
   mid-motion.** A clip that opens at rest is dead before its first sentence.
5. **Two hands, always.** Count the hand roles in every cut. More than two spawns
   a third arm — this happens constantly and is entirely preventable.
6. **Clips 2 and 3 open mid-thought.** No greeting, no re-introduction.

Two that EP03 adds:

7. **Clips 1 and 2 end on a raised, held question.** Brows up and staying up.
   See §2. This is in the cut text; keep it.
8. **Every counting beat is tight or medium close-up.** As above.

The three complete clip prompts are in `ep03-clips.md`, cut by cut, ready to
paste.

### 7c. Post-production — fully portable

All ffmpeg, faster-whisper and libass. Runs anywhere.

**Assemble in one encode.** Trim, concat and loudness-normalise together — and
normalise **each clip to −14 LUFS before the concat**, not once at the end.
Clips come back up to 3 dB apart and a global pass leaves that step audible.

One gotcha: `aresample` after `loudnorm` drops the channel layout and the filter
graph dies with *"Cannot select channel layout."* Always follow `loudnorm` with
`aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo`.

**Then re-transcribe the assembled master, at word level.** Every graphic is
timed from the real audio of the real edit — never from a pre-edit timing shifted
by arithmetic. **Measure, don't offset.**

This matters more than it sounds. Because the timings come from the real audio,
each badge lands in sync with the host's counting hand. Timing from the script
would drift, because the model distributes its eight beats slightly differently
every single time.

**Never bake text into generation.** Numbers, signage, price tags, the logo — all
of it renders as gibberish lettering and none of it is editable afterwards. Burn
every piece of text in post. This is also why the polo is generated plain.

**Use a subtitle track, not stacked drawtext.** EP01 had 37 caption events; as
individual `drawtext` filters that is unmanageable and slow. One `.ass` file
through `subtitles=caps.ass:fontsdir=...` is clean, fast and editable. Captions
are burned for the full script — most of these views are sound-off.

**`ep03-graphics.md` has the complete EP03 burn spec.** Three things there are
not optional:

- **The card texts and the `QUESTION` kicker** replace EP01's `MYTH` system.
  Geometry, colours and the fixed 760px bar stay exactly as they are — that fixed
  width is what makes five cards read as one system rather than five widths.
- **The cue detector must change or the build dies.** EP01 counted with "Number
  one"; EP03 counts with bare ordinals. The existing matcher finds nothing and
  exits on badge 1 — verified, all five fail. A bare-ordinal match is not the fix
  either, because EP03 says "five" three extra times ("Five questions", "same
  five", "Five stores"). The working version requires the ordinal to start a
  sentence. Code and verification output are in `ep03-graphics.md`.
- **Badges 2 and 4 hold across the clip cut on purpose** (2.7s rather than 1.9s),
  so the question card is still on screen when the answer lands. That is the
  relay structure made visible.

**Fix the transcriber's proper nouns.** Whisper reliably mangles *"pawning"* →
"ponching" and *"Grand Strand"* → "grand strain"/"grand strad". `burn.py` carries
a `FIX` dict for exactly this. EP03 says both words too.

---

## 8. Every trap already paid for

Read this before generating anything. Most are properties of diffusion video
models in general, not of one vendor.

### Triage a bad beat before paying to re-render it

The model ships defects at a fairly steady rate — an ad-lib, a repeated line, a
cutaway to something irrelevant. **Almost none of them need a re-render.** A
re-roll is expensive *and* non-deterministic: it may hand you a different defect,
and it will certainly hand you different timings, invalidating every cue you
measured.

The eight-slot structure is what makes defects cheap. Eight beats means eight
hard cuts the model has already made, and a defect inside one beat can be removed
or replaced on those boundaries with no visible seam.

1. **Transcribe the raw clip** and read it against the script. This catches
   repeated lines, ad-libs and dropped words a contact sheet never will.
2. **List the scene cuts** — `select=gt(scene,0.35)` finds the model's own beats.
3. **Is the defect bounded by two cuts?** Cut that beat out. Free, seamless.
4. **Is the audio over it worth keeping?** If the picture is bad but the line is a
   claim you want, keep the track and replace only the *picture* for that beat
   with a designed full-bleed card. Free, and usually better.
5. **Only then consider a re-render.** By now you will rarely need one.

**EP01 hit cases 3 and 4 in the same build and shipped without re-rendering:**

- *Clip 1 delivered "Number two, it's all junk" twice* — 8.46–9.72 and again
  10.26–12.10. The duplicate sat entirely inside one beat bounded by the model's
  own hard cuts, so `8.333 → 10.083` came out losslessly. The *second* delivery
  was kept, because the beat after it is the two-finger close-up.
- *Clip 2 put a blank gold card beside a padded shipping mailer* under the line
  "no credit check… never touches your score" — accidentally the visual language
  of a credit-card offer in the mail, the exact opposite of the claim. The audio
  was worth keeping, so only the picture was replaced with a designed fact card
  (`03-reference/ep01-fact-card.jpg`, from `04-build/factcard.py`).

### EP03's own new trap: the guitar wall

EP01 kept the guitars soft and in the background. **EP03 clip 3 cut 4 walks the
host straight to them and points** — and real guitar headstocks carry maker
logos, which is exactly what the pipeline exists to avoid. The generic "no brand
logos" line in the negative tail does *not* reliably catch it when the shot is
*about* the guitars.

That is why the cut text names it a second time, in the positive, inside the
Dynamic Description: *"Every guitar headstock is completely plain and unbranded."*
Keep that sentence, and check that cut at full resolution before assembling. If a
headstock comes back legible it sits inside one beat bounded by two hard cuts, so
it comes out or gets replaced for free.

### EP03's new props

Four props EP01 did not use. Three are trivial; all four must be textless.

| Prop | Where | Rule |
|---|---|---|
| Plain gold-tone ring | C1 cuts 4–5, C2 cut 5, C3 cut 5 | No stone, no engraving, no markings |
| Blank licence-size card | C2 cut 5 | No text, photo, numbers, barcode or lines |
| Blank paper pad | C2 cut 5 | Same |
| Jeweler's loupe | C3 cut 5 | Plain brass or black, unbranded |

The blank card stands in for "a government photo ID" — the one prop in this
episode that would normally carry text, which is why the prompt names its
blankness five different ways.

### Check the pixels before paying

A downscaled contact sheet is for spotting candidates, not judging them. Pull
full-resolution frames, and for a colour question sample the region's mean RGB
across the beat. One EP01 build nearly paid for a re-render to fix what turned
out to be blown-out backlight that merely *looked* like a wardrobe break.

### QA checklist before stitching

Evenly spaced frames plus 2–3 mid-word frames, checked for: doubled lip edges, a
third hand, face drift between cuts, wardrobe changes, and baked-in text. Re-run
only the failing clip index, never the batch.

**For EP03, add two checks:** the last beat of clips 1 and 2 must read as a
question (brows up, unresolved), and clip 3 cut 4's headstocks must be blank.

### Watch for a preset intercepting your submission

On Higgsfield a batch can come back `submission_failed` saying a preset "was
recommended instead of submitting a job" — no job created, nothing charged. EP01
was offered a preset called "IN THE DARK", which would have thrown a moody night
grade over a bright daylight pawn shop. **Never accept a preset you did not
choose**; it silently overrides the entire Style & Mood block. If your platform
has an equivalent auto-styling feature, turn it off.

### Read what the API actually ran

Reference-image roles get silently coerced (`role: "image"` → `image_references`).
Harmless in itself, but the parameters you wrote are not always the parameters
that ran. Read the response's adjustments rather than assuming.

---

## 9. The reference build

**`06-reference-video/ep01-5-myths-720p.mp4`** — 43.5s · 720×1280 · h264 + AAC ·
5.4 MB. A downscaled review copy; the delivered master is **1080×1920, 27.2 MB**,
mean −18.6 dB, peak −1.4 dB, 37 caption events, zero caption overlaps.

**Watch it before you generate anything.** It is the target: the host, the room,
the pace, the card system, the caption rhythm, the closing card. EP03 should look
like it was shot the same afternoon.

---

## 10. The commercial context

`07-commercial/dicks-pawn-proposal-and-agreement.pdf` is the live agreement.
Relevant if you are producing against it:

- **$5,000/month**, cancel any time, no term commitment, no notice period.
- Cadence starts at **one video per week** while the pipeline is proven, with a
  stated goal of ramping to 2–4 per week as it stabilises.
- Videos are **posted, maintained and analysed** across Instagram, Facebook and
  TikTok — production is not the whole job.
- **AI generation is disclosed to the client in writing, on page 1.** Keep it
  that way.
- A **$10,000/month** full-production tier exists (location crew, lighting,
  sound, hired talent). The $5,000 tier is this pipeline plus in-store filming
  with the client's own staff.
- **No results are guaranteed.** Nothing in any deliverable should imply a
  promised outcome, reach number, or revenue figure.

---

## 11. Build order for EP03

1. **Watch `06-reference-video/ep01-5-myths-720p.mp4`.** Free, and it is the spec.
2. **Use `03-reference/super-dick-host-LOCKED.jpg` as-is.** Do not regenerate the
   host. It already carries the real logo at the right size and it is the single
   point of continuity for the series.
3. **Generate EP03's three storyboards sequentially** from `ep03-boards.md` —
   board 1 chaining **EP01's** board 1, then 2 chaining 1, then 3 chaining 2.
   Check against the real store photos and against EP01's boards. Verify the five
   counting beats are tight or medium close-up.
4. **De-slop each board** with the preservation prompt in `ep01-boards.md`.
5. **Generate three 15s clips** from `ep03-clips.md`. Honour all eight rules in
   §7b — rules 1–6 are the difference between eight hard cuts and one mushy shot,
   and rules 7–8 are the difference between EP03 and a worse EP01.
6. **Transcribe and triage before assembling** (§8). Free, and it is where the
   defects are. Check the two EP03-specific items: held questions, blank
   headstocks.
7. **Assemble in one encode**, per-clip loudness normalisation, then re-transcribe
   the master at word level.
8. **Burn the graphics** per `ep03-graphics.md` — new card texts, the fixed cue
   detector, and the 2.7s bridge hold on badges 2 and 4. Sanity-check the five
   printed cues against the predicted table before accepting the build.

If your video model cannot do native synchronised speech, stop at step 5 and
decide deliberately how you are handling voice — do not discover it at step 7.

---

*Questions on any of this: Kyle Fries · Kylefriesmarketing@gmail.com · 806-544-8098*
