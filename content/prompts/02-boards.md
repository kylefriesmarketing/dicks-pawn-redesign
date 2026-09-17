# Storyboard prompts — EP01 "5 Myths About Pawn Shops"

Model `gpt_image_2` · `21:9` · `2k` · `quality: high` · 6.5 credits each.

Each sheet is eight 9:16 vertical slots in ONE horizontal row. Those eight slots
become the eight internal hard cuts of one 15-second clip. **Generate them
sequentially** — board K passes board K-1 as a trailing reference so the counter,
light direction and guitar wall stay put across the whole 45 seconds.

`medias` order must match the `@ImageN` declarations written into each prompt.

| Board | Role | Myths | medias (in order) |
|---|---|---|---|
| 1 | HOOK | 1-2 | character |
| 2 | MAIN | 3-4 | character, board 1 |
| 3 | CLOSER | 5 + CTA | character, board 2 |

Shared IDs:
- character `9024359d-0dd1-48a7-9665-e942806a4964`
- board 1 `fdf7972f-04ee-4e2f-a23d-a288505bc67d`

---

## Shared blocks

Every board prompt is built from these three blocks plus its own eight slot
lines. Copy them verbatim; they are what keep the sheet from collapsing into a
grid or growing a tenth panel.

**HEADER** (board 1 version — for K>1 see the variant below):

```
@Image1 is the character reference - the same man appears in every slot with
identical face, hair, body, build and identity, wearing the identical navy blue
short-sleeve work polo and rich gold satin cape in all eight slots. No changes to
his features, hair, proportions or wardrobe between slots.

A single ultra-wide horizontal storyboard sheet composed of exactly EIGHT
equal-size 9:16 vertical slots arranged in ONE HORIZONTAL ROW, separated by thin
white gutters on a clean white background, total sheet aspect 21:9. Do NOT make
two rows and do NOT make a grid - exactly eight panels in one row, never ten,
never twelve. All eight slots are active photorealistic UGC iPhone-style stills
that tell one continuous 15-second video clip as eight sequential beats - slot 1
is beat 1 (opening), slot 8 is beat 8 (closing). There are no placeholder slots.
Each adjacent pair of slots is a DIFFERENT camera setup - a different POV (selfie
vs static camera), a different distance band (tight/macro vs medium vs wide), and
a different action - so every beat boundary reads as a crisp hard cut, never a
morph.

Setting in all eight slots is the same American pawn shop sales floor from the
character reference: he stands BEHIND a long glass jewelry display counter filled
with gold chains and rings, a row of hanging guitars on the back wall, bright
daylight coming from the storefront windows mixed with warm overhead shop light.
Same environment, same time of day, same light direction in every slot. Outfit
stays identical across all slots.
```

**HEADER variant for K>1** — insert after the `@Image1` sentence:

```
@Image2 is the previous board in this same video - preserve its exact identity,
location, counter, light direction, time of day and wardrobe. This board
continues the same unbroken scene; nothing about the room or the man changes.
```

...and renumber the character declaration accordingly (`@Image1` character,
`@Image2` previous board).

**FOOTER** (identical on all three boards):

```
Rendering rules: every slot is an exact 9:16 vertical rectangle, all eight slots
identical in size, arranged in ONE HORIZONTAL ROW (do NOT make two rows or a grid
- exactly eight panels in one row, never ten, never twelve) with thin white
gutters on a clean white background, total sheet aspect 21:9. All eight slots are
active - there are no placeholder slots. No two adjacent slots share both their
POV and their distance band. Active slots are photorealistic iPhone-style UGC
stills with natural light and casual real-life feel. The character's identity,
face, hair, build, polo and gold cape are identical across all eight panels. The
character has exactly two hands; selfie POV occupies one hand with the phone,
leaving one hand for action; every slot names each hand's single role, the idle
hand parked explicitly, and the total simultaneous hand-roles never exceed two.
POV may change between slots; every POV change aligns with a hard cut, never a
smooth transition. Each prop holds exactly one state per slot. No on-image text
of any kind: no header, no metadata, no captions, no pop-text, no badges, no
numbers, no subtitles, no watermarks, no slot labels. No legible text, no
readable signage, no price tags, no receipts and no numbers anywhere on any prop,
wall, window or display case. No shallow depth of field, no bokeh, no lens flare,
no beauty filter, no cinematic color grade. No fisheye lens, no ultra-wide
distortion. No mirror or reflection shots. No deformed hands. No third arm, no
extra hands, no duplicated limbs. No additional brands or logos. No firearms or
weapons anywhere in the shop. No invented claims.
```

---

## Board 1 — HOOK (produced)

Insert after the header, before the footer. Opening staging line first:

```
Opening staging: the clip opens on a direct challenge to the viewer - he leans in
over the counter toward the lens, weight on his forearms, as if answering an
accusation the viewer just made.

The character has exactly two hands. In selfie POV slots one hand is occupied by
the phone, so only one hand is available for action. Every slot names what EACH
hand is doing - one role per hand, the idle hand parked explicitly - never more
than two simultaneous hand-roles. POV may change between slots; every POV change
aligns with a hard cut, never a smooth transition.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium distance: he stands behind the glass counter and leans in toward the lens,
chin slightly down, eyebrows raised in a direct challenge; both forearms rest flat
on the counter glass - left forearm planted on the glass, right forearm planted on
the glass beside it; gold cape visible over both shoulders; daylight from the
storefront rakes across the counter.

Slot 2 - exact 9:16 vertical still, static camera POV, tight distance: head-and-
shoulders close on his face mid-sentence, one eyebrow lifted, a dry half-smile
starting; his right hand is raised just into the bottom of frame with the index
finger extended upward counting off a first point, left hand parked out of frame
at his side; soft warm overhead light on his face.

Slot 3 - exact 9:16 vertical still, static camera POV, wide distance: full body
behind the counter, the gold cape clearly hanging down his back, the guitar wall
and the length of the jewelry case visible; his right arm is extended open,
gesturing along the display case beside him, left hand parked resting on the
counter edge; bright ambient shop daylight.

Slot 4 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone himself at arm's length while walking slowly along behind the counter,
slightly off-center handheld framing with a natural tilt; left hand holds the
phone (wrist faintly visible at the frame edge), right hand open palm-up in a
casual come-on gesture; storefront light behind him.

Slot 5 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the inside of the glass jewelry case - rows of gold chains and rings
under the case lighting, no face in frame; his right hand rests on the polished
metal edge of the case at the top of frame, left hand absent from frame; warm
specular glints on the gold.

Slot 6 - exact 9:16 vertical still, static camera POV, wide distance: he has
stepped back from the counter, full torso and cape visible against the guitar
wall, shoulders lifted in an open shrug; right hand open at waist height palm-up,
left hand parked hanging at his side; even daylight across the sales floor.

Slot 7 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, mouth mid-word, head tilted slightly; his left hand is
raised into frame with two fingers extended counting off a second point, right
hand parked flat on the counter glass below frame; warm overhead light.

Slot 8 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length back at his spot behind the counter, casual imperfect
framing, caught mid-sentence with a relaxed unguarded face; right hand holds the
phone (hand faintly visible at the frame edge), left hand parked resting flat on
the counter glass; daylight from the storefront filling the background.
```

---

## Board 2 — MAIN (myths 3-4: credit, safekeeping)

```
Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium distance: he is back at his place behind the glass counter, both palms
laid flat on the glass, shoulders squared, expression flat and matter-of-fact;
left palm flat on the glass, right palm flat on the glass beside it; daylight
across the counter.

Slot 2 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face, brows drawn together in a small firm headshake; his right hand rises
into the bottom of frame with three fingers extended counting off a third point,
left hand parked out of frame at his side; warm overhead light.

Slot 3 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length, walking a few steps along the counter, framing off-center
with a natural tilt; left hand holds the phone (forearm grazing the frame edge),
right hand sweeps once flat through the air in a clean no gesture; storefront
daylight behind him.

Slot 4 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the counter surface - a plain unmarked padded storage envelope and a
small blank brass tag resting on the glass, no face in frame, no writing or
numbers on either object; his right hand sets the brass tag down beside the
envelope, left hand absent from frame; soft directional light.

Slot 5 - exact 9:16 vertical still, static camera POV, wide distance: full body
behind the counter, full gold cape visible, the guitar wall behind him; his left
arm extends to gesture toward a plain closed doorway at the back of the sales
floor, right hand parked resting on the counter edge; even ambient daylight.

Slot 6 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, chin lifted, a small reassuring nod; his left hand is
raised into frame with four fingers extended counting off a fourth point, right
hand parked flat on the counter below frame; warm overhead light.

Slot 7 - exact 9:16 vertical still, static camera POV, medium distance: he pats
the top of the glass display case twice with an open palm, a settled easy
expression; right hand flat patting the case top, left hand parked hanging at his
side; gold chains visible under the glass beneath his hand.

Slot 8 - exact 9:16 vertical still, selfie POV, tight distance: he holds the
phone close, head and shoulders filling the frame, caught mid-sentence looking
directly into the lens with a calm level expression; right hand holds the phone
(hand faintly visible at the frame edge), left hand parked resting on the counter
glass; daylight filling the background.
```

---

## Board 3 — CLOSER (myth 5 + the invitation)

```
Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium distance: he leans in over the counter toward the lens with a wry look,
one eyebrow up; his right hand is raised with all five fingers spread counting off
the fifth point, left hand planted flat on the counter glass; daylight raking
across the counter.

Slot 2 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face, a single slow headshake and a breaking half-grin; right hand parked flat
on the counter below frame, left hand parked at his side, neither in frame; warm
overhead light on his face.

Slot 3 - exact 9:16 vertical still, selfie POV, wide distance: he holds the phone
at arm's length as he steps out from behind the end of the counter onto the sales
floor, the full gold cape swinging behind him, framing loose and off-center; left
hand holds the phone (forearm at the frame edge), right hand parked swinging
naturally at his side; bright storefront daylight ahead of him.

Slot 4 - exact 9:16 vertical still, static camera POV, medium distance: he stands
on the sales floor and gestures with an open arm back toward the bright storefront
doorway, inviting; right arm extended open toward the door, left hand parked
resting at his belt; daylight flooding in from the entrance behind him.

Slot 5 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the jewelry case interior - gold chains and rings under the case
lighting, no face in frame; no hands in frame; warm specular glints crawling
across the gold.

Slot 6 - exact 9:16 vertical still, static camera POV, wide distance: he stands
centered on the sales floor with both arms open wide at his sides, the full gold
cape spread and catching the light, guitar wall and jewelry cases flanking him,
an easy open expression; left arm open at his side, right arm open at his side;
bright even daylight across the floor.

Slot 7 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length, warm and direct into the lens, mid-invitation, a genuine
half-smile; right hand holds the phone (hand faintly visible at the frame edge),
left hand open palm-up at chest height; storefront daylight on his face.

Slot 8 - exact 9:16 vertical still, static camera POV, wide distance: seen from
behind and to one side as he walks away toward the bright storefront entrance, the
gold cape trailing behind him, jewelry cases and guitar wall on either side; both
arms swinging naturally at his sides; strong daylight silhouetting him in the
doorway.
```

---

## Mandatory de-slop pass

After each board completes, import its result URL with `media_import_url`, then
run `seedream_v5_pro` at `21:9` / `2k` with that imported ID as
`image_references` and this prompt. The cleaned job ID replaces the raw board
everywhere downstream.

```
KEEP EXACTLY the framing, composition, slot layout, camera distances, poses and
subjects of this horizontal storyboard sheet and every one of its side-by-side
vertical slots - no reframe, no zoom, no crop, no re-layout, no change to the
scene, or to any person's face / hair / body. Do not introduce any product,
package, brand, or sales prop. CHANGE ONLY micro-realism, applied identically in
every slot: true-to-life pore-level skin with natural texture and fine vellus
hair, real material detail, even natural daytime light with gentle highlight
roll-off and faint true sensor noise, a flat authentic iPhone photo, deep focus.
PRESERVE each face's exact shape / width / proportions 1:1 - do NOT squeeze /
narrow / slim / stretch any face. AVOID AI-slop: waxy plastic skin, airbrushed
poreless skin, beauty-filter smoothing, over-saturation, HDR glow / bloom / halos,
oversharpening, teal-orange grade, shallow depth of field, bokeh, cinematic /
DSLR look. No added text, no watermark, no baked slot labels.
```

On a moderation failure retry once with `seedream_v5_lite`; if that also fails,
keep the raw board and note the degradation.
