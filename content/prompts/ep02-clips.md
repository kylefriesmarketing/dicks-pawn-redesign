# Clip prompts — EP02 "5 Questions We Get Every Single Day"

Model `seedance_2_5` · `9:16` · `1080p` · `duration: 15` · `mode: omni_reference`
· `generate_audio: true` · **135 credits each**.

Speech renders natively from the `Audio:` line — never make a separate
`generate_audio` call. Write nothing new at submit time: these three prompts go
out as one `generate_video_batch`.

`medias` per clip, in order: the **de-slopped EP02 board** for that clip, then
the character reference `9024359d-0dd1-48a7-9665-e942806a4964`.

Cut timings are fixed for 15s and must sum exactly:
`0-1.9 · 1.9-3.8 · 3.8-5.6 · 5.6-7.5 · 7.5-9.4 · 9.4-11.3 · 11.3-13.1 · 13.1-15`

## The six rules from EP01 still apply, unchanged

1. `Hard cut to.` verbatim at the end of cuts 1-7. Seven markers, none after
   cut 8. Without them the eight beats melt into one continuous shot.
2. Static cuts say *locked-off, zero movement*. Never write `handheld`, `drift`,
   `sway` or `micro-shake` inside a static cut — the words leak motion in.
3. Selfie cuts never mention the phone as an object. The camera **is** the
   phone. Writing "holds the phone" makes Seedance show a man holding a phone.
4. The voice starts within 0.4s of frame one, and frame one is already
   mid-motion. A clip that opens at rest is dead before its first sentence.
5. Two hands, always. Count the hand roles in every cut; more than two spawns a
   third arm.
6. Clips 2 and 3 open mid-thought. No greeting, no re-introduction.

## Two rules EP02 adds

7. **Cuts 1-8 of clips 1 and 2 end on a raised, held question.** The last line
   of each of those clips is a question the next clip answers, and the face has
   to carry it — brows up and staying up, mouth closing, a beat of waiting. If
   the model resolves the expression, the relay breaks at the clip boundary,
   which is the worst place in the episode to lose a viewer. The cut-8 text
   below says so explicitly; do not trim that sentence to save prompt length.
8. **Every counting beat is TIGHT or MEDIUM CLOSE-UP.** Never wide, never macro.
   All five of EP01's numerals landed on a tight or medium-close shot, which is
   why each badge reads in sync with the counting hand. At wide distance the
   fingers are a few pixels across and the badge looks pasted on.

## Word budget

Density target is 30-35 spoken words per clip. Clip 1 is 34, clip 3 is 31, and
**clip 2 is 37 — the tightest in the series so far.** If the delivery comes back
rushed or the last question gets clipped, the pre-authorised trim is the phrase
*"not our rule"*, leaving "That's South Carolina law." That keeps the claim, the
attribution and the cliffhanger, and buys back three words. Make that decision
by listening to the render, not by pre-emptively cutting it.

---

## Clip 1 — HOOK (Q1, and Q2 asked)

Spoken: *"Five questions, every day, same five. One — what's the difference
between selling and pawning? Sell it, we keep it. Pawn it, we hold it and you
come back. Two — do I need good credit?"*

```
Style & Mood: UGC iPhone aesthetic, bright natural daylight from storefront
windows mixed with warm overhead shop light, MIXED: starts STATIC locked-off,
hard-cuts between STATIC locked-off frozen frames and SELFIE front-facing
handheld, POV alternates per cut, social media vertical format, deep focus with
the background sharp, 23mm-wide phone look, mild HDR flattening and faint shadow
noise, pore-level skin with no smoothing.

Narrative Summary: Behind the jewelry counter of a family pawn shop, a caped
store host runs through the questions customers ask him every single day, answers
the first one with his hands on the glass, and ends on the second question still
hanging in the air, performed by a natural, engaged creator - genuine reactions,
lively but human, never staged screaming energy.

Dynamic Description:
Cut 1 (0-1.9s) - MEDIUM CLOSE-UP, STATIC locked-off camera: he is already
mid-motion as the frame opens, his right hand coming up toward the lens with all
five fingers spread wide and clearly separated, eyebrows lifting, his jaw already
moving on the first word; left hand planted flat on the counter glass; the gold
cape settles across both shoulders from the movement. Camera absolutely frozen
and locked off, zero movement of any kind. Hard cut to.
Cut 2 (1.9-3.8s) - TIGHT, SELFIE front-facing POV: the viewer sees exactly what
his front camera captures, head and shoulders filling the frame, framing slightly
off-center with a natural tilt; his left hand rises into the bottom of frame with
the index finger extended straight up counting off the first point, the other arm
is the one carrying the camera and only its wrist grazes the frame edge; one
eyebrow lifts and a dry half-smile starts at the corner of his mouth. Slight
natural handheld micro-shake from his grip. Hard cut to.
Cut 3 (3.8-5.6s) - WIDE, STATIC locked-off camera: full body behind the counter,
the gold cape hanging the length of his back, the guitar wall and the whole length
of the jewelry case filling the background; his right arm sweeps open along the
display case beside him, left hand parked resting on the counter edge; his head
tips to one side and his shoulders lift once in a small questioning motion.
Camera absolutely frozen and locked off, zero movement of any kind. Hard cut to.
Cut 4 (5.6-7.5s) - MEDIUM, STATIC locked-off camera: he slides a small plain
gold-tone ring across the counter glass toward himself and closes his hand over
it in one motion, chin dipping, expression flat and matter-of-fact; right hand
closing over the ring on the glass, left hand parked flat on the glass beside it;
the ring is completely plain with no stone, no engraving and no markings. Camera
absolutely frozen and locked off, zero movement of any kind. Hard cut to.
Cut 5 (7.5-9.4s) - MACRO, STATIC locked-off camera: tight on the counter glass -
the plain gold-tone ring sitting alone on the polished surface under the case
lighting, no face in frame; his fingertips lift away from it and out of the top of
the frame, left hand absent from frame; a warm specular glint crawls across the
gold as nothing else moves. Camera absolutely frozen and locked off, zero movement
of any kind. Hard cut to.
Cut 6 (9.4-11.3s) - MEDIUM, SELFIE front-facing POV: the viewer sees what his
front camera captures as he walks slowly along behind the counter, framing
off-center with a natural tilt; his right hand traces one wide out-and-back arc
through the air, the other arm carries the camera and only its forearm edge grazes
the frame; he blinks once and tips his head mid-word, storefront daylight sliding
across his face as he moves. Slight natural handheld micro-shake from his grip,
one autofocus adjustment mid-cut. Hard cut to.
Cut 7 (11.3-13.1s) - WIDE, STATIC locked-off camera: he has turned slightly and
gestures with an open arm back toward the bright storefront doorway across the
sales floor; right arm extended open toward the entrance, left hand parked resting
at his belt; his weight shifts onto his back foot and his chin lifts once. Camera
absolutely frozen and locked off, zero movement of any kind. Hard cut to.
Cut 8 (13.1-15s) - TIGHT CLOSE-UP, STATIC locked-off camera: close on his face
and upper chest; his left hand rises into frame with two fingers extended counting
off the second point, right hand parked flat on the counter glass below the frame
line; his eyebrows lift high and STAY lifted, his mouth closes on a question and
his head tips a few degrees to one side, waiting. The clip ends on an unanswered
question - the expression reads as asking, never as concluding, and the brows do
not come back down before the clip ends. Camera absolutely frozen and locked off,
zero movement of any kind.

Static Description: An American pawn shop sales floor - a long glass jewelry
display case packed with gold chains and rings, white horizontal-grooved slatwall
densely hung with merchandise, knotty pine accent columns between the panels, a
back wall hung with acoustic and electric guitars, warm brown wood-look plank
floor, bright daylight pouring in from the storefront windows behind him and warm
fluorescent shop light overhead. Cluttered, well-stocked and lived-in - a working
shop, not a showroom.

Audio: He speaks to camera, iPhone microphone audio with natural room tone:
"Five questions, every day, same five. One - what's the difference between selling
and pawning? Sell it, we keep it. Pawn it, we hold it and you come back. Two - do
I need good credit?"

Facial features clear and undistorted, consistent clothing throughout - the same
navy blue polo and gold satin cape in every cut. Shot on iPhone, natural lighting,
social media aesthetic, handheld micro-shake during selfie cuts, locked-off frozen
frame during static-camera cuts. No on-screen text, no subtitles, no captions, no
watermarks, no legible text on any object, no readable signage, no price tags, no
numbers on any prop, no real brand logos anywhere, no firearms or weapons, no
cinematic grade, no film grain, no bokeh, no lens flare, no fisheye lens, no
ultra-wide distortion, no slow motion, no beauty filter, no third arm, no extra
hands, no duplicated limbs, no deformed hands.
```

---

## Clip 2 — MAIN (Q2 answered, Q3, and Q4 asked)

Spoken: *"You need NO credit. Pawn loans run on your item, not your score. Three
— what do I bring? Your item and a government photo ID. That's South Carolina
law, not our rule. Four — is my stuff safe?"*

```
Style & Mood: UGC iPhone aesthetic, bright natural daylight from storefront
windows mixed with warm overhead shop light, MIXED: hard-cuts between STATIC
locked-off frozen frames and SELFIE front-facing handheld, POV alternates per cut,
social media vertical format, deep focus with the background sharp, 23mm-wide
phone look, mild HDR flattening and faint shadow noise, pore-level skin with no
smoothing.

Narrative Summary: Still behind the jewelry counter, the same caped store host
answers the credit question flatly, tells people exactly what to bring, points the
rule at the state rather than the shop, and ends on a fourth question left hanging,
performed by a natural, engaged creator - genuine reactions, lively but human,
never staged screaming energy.

Dynamic Description:
Cut 1 (0-1.9s) - MEDIUM CLOSE-UP, STATIC locked-off camera: the frame opens with
him already mid-gesture, his right hand sweeping flat and level across in front of
his chest in one clean cancelling motion, brows down, jaw set, an emphatic
matter-of-fact expression; left hand parked hanging at his side; he is already
speaking on frame one with no windup and no re-introduction. Camera absolutely
frozen and locked off, zero movement of any kind. Hard cut to.
Cut 2 (1.9-3.8s) - MEDIUM, SELFIE front-facing POV: the viewer sees what his
front camera captures as he walks a few steps along the counter, framing
off-center with a natural tilt; his left hand taps down once on the counter glass
indicating the case beneath it, the other arm carries the camera and only its hand
grazes the frame edge; his eyebrows lift on the tap and he gives one small nod.
Slight natural handheld micro-shake from his grip. Hard cut to.
Cut 3 (3.8-5.6s) - WIDE, STATIC locked-off camera: full body behind the counter,
the full gold cape visible against the guitar wall, giving one firm single shake
of the head; left hand open at waist height palm-down, right hand parked hanging
at his side; his shoulders drop half an inch as the headshake finishes. Camera
absolutely frozen and locked off, zero movement of any kind. Hard cut to.
Cut 4 (5.6-7.5s) - MEDIUM CLOSE-UP, STATIC locked-off camera: he leans in
slightly toward the lens, eyebrows lifted in a question; his right hand rises into
frame with three fingers extended and clearly separated, counting off the third
point, left hand parked flat on the counter glass; his eyes widen a fraction on
the count. Camera absolutely frozen and locked off, zero movement of any kind.
Hard cut to.
Cut 5 (7.5-9.4s) - MACRO, STATIC locked-off camera: tight on the counter glass -
a plain gold-tone ring beside a completely blank unmarked white card the size of a
driver's licence and a small blank paper pad, no face in frame; his right hand
sets the blank card down flat beside the ring and withdraws, left hand absent from
frame. The card and the pad are totally blank - no text, no photograph, no
numbers, no barcode, no lines and no printing of any kind. Camera absolutely
frozen and locked off, zero movement of any kind. Hard cut to.
Cut 6 (9.4-11.3s) - MEDIUM, SELFIE front-facing POV: the viewer sees what his
front camera captures, framing loose and off-center; his right hand gestures
outward toward the bright storefront windows as if indicating something beyond the
building, the other arm carries the camera and only its forearm grazes the frame;
his eyebrows raise once and settle, daylight from the windows flaring gently
behind him. Slight natural handheld micro-shake from his grip. Hard cut to.
Cut 7 (11.3-13.1s) - WIDE, STATIC locked-off camera: he opens both arms out at
his sides, palms turned up in a clean hands-off shrug, shoulders lifting, the gold
cape spread by the movement; left arm open palm-up, right arm open palm-up; his
head tips to one side as the shrug lands. Camera absolutely frozen and locked off,
zero movement of any kind. Hard cut to.
Cut 8 (13.1-15s) - TIGHT CLOSE-UP, STATIC locked-off camera: close on his face
and upper chest; his left hand rises into frame with four fingers extended
counting off the fourth point, right hand parked flat on the counter below the
frame line; his eyebrows lift high and STAY lifted, his chin comes up, his lips
close on a question and he holds the look. The clip ends on an unanswered question
- the expression reads as asking, never as concluding, and the brows do not come
back down before the clip ends. Camera absolutely frozen and locked off, zero
movement of any kind.

Static Description: An American pawn shop sales floor - a long glass jewelry
display case packed with gold chains and rings, white horizontal-grooved slatwall
densely hung with merchandise, knotty pine accent columns between the panels, a
back wall hung with acoustic and electric guitars, warm brown wood-look plank
floor, bright daylight pouring in from the storefront windows behind him and warm
fluorescent shop light overhead. Cluttered, well-stocked and lived-in - a working
shop, not a showroom.

Audio: He speaks to camera, iPhone microphone audio with natural room tone:
"You need NO credit. Pawn loans run on your item, not your score. Three - what do
I bring? Your item and a government photo ID. That's South Carolina law, not our
rule. Four - is my stuff safe?"

Facial features clear and undistorted, consistent clothing throughout - the same
navy blue polo and gold satin cape in every cut. Shot on iPhone, natural lighting,
social media aesthetic, handheld micro-shake during selfie cuts, locked-off frozen
frame during static-camera cuts. No on-screen text, no subtitles, no captions, no
watermarks, no legible text on any object, no readable signage, no price tags, no
numbers on any prop, no real brand logos anywhere, no firearms or weapons, no
cinematic grade, no film grain, no bokeh, no lens flare, no fisheye lens, no
ultra-wide distortion, no slow motion, no beauty filter, no third arm, no extra
hands, no duplicated limbs, no deformed hands.
```

---

## Clip 3 — CLOSER (Q4 answered, Q5, and the invitation)

Spoken: *"Safe and insured, the whole time. Five — how do you decide what it's
worth? Brand, model, condition, and what it actually resells for. Free look, no
obligation. Five stores, Grand Strand."*

```
Style & Mood: UGC iPhone aesthetic, bright natural daylight from storefront
windows mixed with warm overhead shop light, MIXED: hard-cuts between STATIC
locked-off frozen frames and SELFIE front-facing handheld, POV alternates per cut,
social media vertical format, deep focus with the background sharp, 23mm-wide
phone look, mild HDR flattening and faint shadow noise, pore-level skin with no
smoothing.

Narrative Summary: The same caped store host closes out the list - reassures on
safekeeping, walks through how an item actually gets valued, and ends with an open
invitation to come in, performed by a natural, engaged creator - genuine
reactions, lively but human, never staged screaming energy.

Dynamic Description:
Cut 1 (0-1.9s) - MEDIUM, STATIC locked-off camera: the frame opens with his palm
already coming down onto the top of the glass display case, patting it twice, a
settled easy expression and relaxed shoulders; right hand flat patting the case
top, left hand parked hanging at his side; gold chains visible under the glass
beneath his hand, and he is already speaking on frame one. Camera absolutely
frozen and locked off, zero movement of any kind. Hard cut to.
Cut 2 (1.9-3.8s) - TIGHT, SELFIE front-facing POV: the viewer sees what his front
camera captures, head and shoulders filling the frame, looking straight into the
lens with a calm reassuring expression and one small slow nod; his left hand comes
up open palm-up at chest height, the other arm carries the camera and only its
hand grazes the frame edge; his eyes soften on the nod. Slight natural handheld
micro-shake from his grip. Hard cut to.
Cut 3 (3.8-5.6s) - MEDIUM CLOSE-UP, STATIC locked-off camera: he raises his right
hand toward the lens with all five fingers spread wide and clearly separated,
counting off the fifth point, eyebrows lifting into a question; left hand planted
flat on the counter glass; his head tilts a few degrees as the question lands.
Camera absolutely frozen and locked off, zero movement of any kind. Hard cut to.
Cut 4 (5.6-7.5s) - WIDE, STATIC locked-off camera: he has stepped across to the
back wall and stands beside the row of hanging guitars, his right arm extended
gesturing along the length of the row, left hand parked at his side, the full gold
cape down his back; he rocks once onto his back foot as he gestures. Every guitar
headstock is completely plain and unbranded - no maker logos, no model names and
no lettering of any kind anywhere on any instrument. Camera absolutely frozen and
locked off, zero movement of any kind. Hard cut to.
Cut 5 (7.5-9.4s) - MACRO, STATIC locked-off camera: tight on his hands only, no
face in frame - his left hand holds a jeweler's loupe up to the light while his
right hand slowly turns the plain gold-tone ring beneath it; exactly two hands in
frame and nothing else; warm specular light crawls across the gold and the loupe
glass as the ring turns. Camera absolutely frozen and locked off, zero movement of
any kind. Hard cut to.
Cut 6 (9.4-11.3s) - MEDIUM, SELFIE front-facing POV: the viewer sees what his
front camera captures as he walks back toward his place behind the counter,
framing off-center with a natural tilt; his right hand opens palm-up in a casual
easy that-is-how gesture, the other arm carries the camera and only its forearm
grazes the frame; the lit jewelry cases slide past behind him and he blinks once
mid-word. Slight natural handheld micro-shake from his grip, one autofocus
adjustment mid-cut. Hard cut to.
Cut 7 (11.3-13.1s) - TIGHT CLOSE-UP, STATIC locked-off camera: close on his face
and upper chest, warm and direct into the lens with a genuine unforced half-smile,
mouth mid-word; right hand parked flat on the counter glass below the frame line,
left hand parked at his side; his eyebrows lift once in easy invitation. Camera
absolutely frozen and locked off, zero movement of any kind. Hard cut to.
Cut 8 (13.1-15s) - WIDE, STATIC locked-off camera: he stands back behind the
counter and opens both arms wide at his sides, the full gold cape spreading and
catching the light, the guitar wall behind him and the lit jewelry cases running
away on either side, an easy open expression holding to the end; left arm open at
his side, right arm open at his side. The lower third of the frame is open counter
surface and floor only - visually quiet and uncluttered, with nothing important in
it. Camera absolutely frozen and locked off, zero movement of any kind.

Static Description: An American pawn shop sales floor - a long glass jewelry
display case packed with gold chains and rings, white horizontal-grooved slatwall
densely hung with merchandise, knotty pine accent columns between the panels, a
back wall hung with acoustic and electric guitars, warm brown wood-look plank
floor, bright daylight pouring in from the storefront windows behind him and warm
fluorescent shop light overhead. Cluttered, well-stocked and lived-in - a working
shop, not a showroom.

Audio: He speaks to camera, iPhone microphone audio with natural room tone:
"Safe and insured, the whole time. Five - how do you decide what it's worth?
Brand, model, condition, and what it actually resells for. Free look, no
obligation. Five stores, Grand Strand."

Facial features clear and undistorted, consistent clothing throughout - the same
navy blue polo and gold satin cape in every cut. Shot on iPhone, natural lighting,
social media aesthetic, handheld micro-shake during selfie cuts, locked-off frozen
frame during static-camera cuts. No on-screen text, no subtitles, no captions, no
watermarks, no legible text on any object, no readable signage, no price tags, no
numbers on any prop, no real brand logos anywhere, no firearms or weapons, no
cinematic grade, no film grain, no bokeh, no lens flare, no fisheye lens, no
ultra-wide distortion, no slow motion, no beauty filter, no third arm, no extra
hands, no duplicated limbs, no deformed hands.
```

---

## Props introduced in EP02, and the one new trap

EP02 needs four props EP01 did not use. Three are trivial; one is not.

| Prop | Where | Rule |
|---|---|---|
| Plain gold-tone ring | C1 cuts 4-5, C2 cut 5, C3 cut 5 | No stone, no engraving, no markings |
| Blank licence-size card | C2 cut 5 | No text, photo, numbers, barcode or lines |
| Blank paper pad | C2 cut 5 | Same |
| Jeweler's loupe | C3 cut 5 | Plain brass or black, unbranded |

**The new trap is the guitar wall.** EP01 kept the guitars soft and in the
background. EP02 cut 4 of clip 3 walks the host straight to them and points, and
real guitar headstocks carry maker logos — which is exactly the thing the whole
pipeline is built to avoid, and which the generic "no brand logos" line in the
negative tail does not reliably catch when the shot is *about* the guitars.
That is why the cut text names it a second time, in the positive, inside the
Dynamic Description. Keep that sentence.

Check cut 4 of clip 3 at full resolution before assembling. If a headstock comes
back with a legible mark, it sits inside one beat bounded by two hard cuts, so it
comes out or gets replaced for free — see the triage order in `00-runbook.md`.
