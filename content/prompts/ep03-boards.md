# Storyboard prompts — EP03 "5 Questions We Get Every Single Day"

Model `gpt_image_2` · `21:9` · `2k` · `quality: high` · 6.5 credits each.

Same machine as EP01: three sheets, eight 9:16 vertical slots each, one
horizontal row. Those eight slots become the eight internal hard cuts of one
15-second clip. **Not produced yet** — these prompts are written and ready.

## What is different from EP01, and why it matters to the boards

EP01 was a countdown. EP03 is a **relay**. Each clip ends on a question the
*next* clip answers:

| | ends on | next clip opens on |
|---|---|---|
| Clip 1 | "Two — do I need good credit?" | "You need NO credit." |
| Clip 2 | "Four — is my stuff safe?" | "Safe and insured, the whole time." |

That changes the staging at exactly four slots, and nowhere else:

- **Slot 8 of boards 1 and 2 is a held question**, not a resolved beat. Brows up
  and *staying* up, mouth closing on a question, the counting hand still in
  frame. EP01's clips 1 and 2 ended on settled, satisfied faces. If these land
  settled, the cliffhanger dies and the viewer leaves at the clip boundary —
  which is the single most expensive place in the episode to lose them.
- **Slot 1 of boards 2 and 3 is an answer landing on frame one.** No windup, no
  breath, no re-entry. He is already mid-gesture as the frame opens.

Everything else — the host, the room, the light, the eight-beat grammar, the
hand rules, the de-slop pass — is EP01's, unchanged.

## Reference chain

Board 1 anchors to **EP01's board 1** so the room matches the episode already
shipped. Within EP03, board K chains board K−1 as usual. Sequential, never
parallel.

| Board | Role | Questions | medias (in order) |
|---|---|---|---|
| 1 | HOOK | Q1 + Q2 asked | character, **EP01 board 1 (de-slopped)** |
| 2 | MAIN | Q2 answered, Q3, Q4 asked | character, EP03 board 1 |
| 3 | CLOSER | Q4 answered, Q5 + CTA | character, EP03 board 2 |

Shared IDs:
- character `9024359d-0dd1-48a7-9665-e942806a4964` — **never regenerate**
- EP01 board 1 `fdf7972f-04ee-4e2f-a23d-a288505bc67d`

`medias` order must match the `@ImageN` declarations in the prompt.

---

## Shared blocks

**HEADER, FOOTER and the de-slop prompt are byte-identical to
`ep01-boards.md`.** Copy them from there rather than retyping — they are what
keep the sheet from collapsing into a grid or growing a tenth panel, and they
are the most drift-prone text in the whole pipeline.

All three EP03 boards use the **K>1 header variant** (two reference images), so
`@Image1` is the character and `@Image2` is the chained board. Board 1's
`@Image2` sentence needs one word changed, because its chain reaches back an
episode rather than a slot:

```
@Image2 is a board from the previous episode of this same series, shot in the
same location on the same day - preserve its exact identity, location, counter,
light direction, time of day and wardrobe. This board continues the same unbroken
scene; nothing about the room or the man changes.
```

Boards 2 and 3 use the EP01 wording verbatim (`@Image2 is the previous board in
this same video...`).

---

## One rule EP01 established that EP03 must not break

**Every counting beat is TIGHT or MEDIUM CLOSE-UP. Never wide, never macro.**

All five of EP01's numerals landed on a tight or medium-close shot, and that is
why each badge reads in sync with the host's counting hand — badge "1" while one
finger is up, badge "5" while the hand is open. Stage a count at wide distance
and the fingers are four pixels across; the badge then looks pasted on rather
than counted out, and there is no fixing it in post.

EP03's counting beats are board 1 slots 2 and 8, board 2 slots 4 and 8, and
board 3 slot 3. Check them before you submit.

---

## Board 1 — HOOK (Q1, and Q2 asked)

Insert after the header, before the footer. Opening staging line first:

```
Opening staging: the clip opens on an open hand - he is already holding all five
fingers spread toward the lens as the frame begins, counting out the promise of
the list before he has finished the first sentence.

The character has exactly two hands. In selfie POV slots one hand is occupied by
the phone, so only one hand is available for action. Every slot names what EACH
hand is doing - one role per hand, the idle hand parked explicitly - never more
than two simultaneous hand-roles. POV may change between slots; every POV change
aligns with a hard cut, never a smooth transition.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium close-up distance: he stands behind the glass counter with his right hand
raised toward the lens, all five fingers spread and clearly separated, eyebrows
lifted, mouth open mid-word; left hand planted flat on the counter glass; gold
cape over both shoulders; daylight from the storefront raking across the counter.

Slot 2 - exact 9:16 vertical still, selfie POV, tight distance: he holds the phone
himself at arm's length, head and shoulders filling the frame, slightly off-center
with a natural tilt; right hand holds the phone (wrist faintly visible at the
frame edge), left hand raised into the bottom of frame with the index finger
extended straight up counting off the first point; warm overhead light on his
face.

Slot 3 - exact 9:16 vertical still, static camera POV, wide distance: full body
behind the counter, the gold cape hanging the length of his back, the guitar wall
and the whole length of the jewelry case in frame; his right arm sweeps open along
the display case beside him, left hand parked resting on the counter edge; bright
ambient shop daylight.

Slot 4 - exact 9:16 vertical still, static camera POV, medium distance: he slides
a small plain gold-tone ring across the counter glass toward himself and closes
his hand over it, chin dipping, a flat matter-of-fact expression; right hand
closing over the ring on the glass, left hand parked flat on the glass beside it;
the ring is completely plain with no stone, no engraving, no markings.

Slot 5 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the counter glass - the plain gold-tone ring sitting alone on the
polished surface under the case lighting, no face in frame; his fingertips are
lifting away from it at the top of frame, left hand absent from frame; warm
specular glint on the gold and on the glass.

Slot 6 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length while walking slowly along behind the counter, framing
off-center with a natural tilt; left hand holds the phone (forearm grazing the
frame edge), right hand traces a single wide out-and-back arc through the air;
storefront light sliding across his face as he moves.

Slot 7 - exact 9:16 vertical still, static camera POV, wide distance: he has
turned slightly and gestures with an open arm back toward the bright storefront
doorway across the sales floor; right arm extended open toward the entrance, left
hand parked resting at his belt; daylight flooding in from the doorway behind the
gesture.

Slot 8 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, eyebrows raised high and HELD, mouth closing on a
question, head tipped a few degrees to one side and waiting; his left hand is
raised into frame with two fingers extended counting off the second point, right
hand parked flat on the counter glass below the frame line; warm overhead light.
This slot is an unanswered question - the expression must read as asking, not as
concluding.
```

---

## Board 2 — MAIN (Q2 answered, Q3, and Q4 asked)

```
Opening staging: the clip opens mid-answer. He is already sweeping a flat palm
across in front of him as the frame begins - the answer to the question the
previous clip ended on, landing with no windup and no re-introduction.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium close-up distance: he is behind the counter mid-gesture, his right hand
sweeping flat and level across in front of his chest in a single clean cancelling
motion, brows down, jaw set, an emphatic matter-of-fact expression; left hand
parked hanging at his side; daylight across the counter.

Slot 2 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length, walking a few steps along the counter, framing off-center
with a natural tilt; right hand holds the phone (hand faintly visible at the frame
edge), left hand taps down once on the counter glass indicating the case beneath
it; storefront daylight behind him.

Slot 3 - exact 9:16 vertical still, static camera POV, wide distance: full body
behind the counter, the full gold cape visible against the guitar wall, giving one
firm single shake of the head; left hand open at waist height palm-down, right
hand parked hanging at his side; even daylight across the sales floor.

Slot 4 - exact 9:16 vertical still, static camera POV, medium close-up distance:
he leans in slightly, eyebrows lifted in a question; his right hand is raised into
frame with three fingers extended and clearly separated, counting off the third
point, left hand parked flat on the counter glass; warm overhead light on his
face.

Slot 5 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the counter glass - a plain gold-tone ring beside a completely blank
unmarked white card the size of a driver's licence and a small blank paper pad, no
face in frame; his right hand is setting the blank card down flat beside the ring,
left hand absent from frame; soft directional light. The card and the pad are
totally blank - no text, no photograph, no numbers, no barcode, no lines, no
printing of any kind.

Slot 6 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length, framing loose and off-center; left hand holds the phone
(forearm at the frame edge), right hand gestures outward toward the bright
storefront windows as if indicating something beyond the building; daylight from
the windows filling the background behind him.

Slot 7 - exact 9:16 vertical still, static camera POV, wide distance: he stands
behind the counter with both arms opened out at his sides, palms turned up in a
clean hands-off shrug, shoulders lifted, the gold cape spread by the movement;
left arm open palm-up, right arm open palm-up; bright even daylight.

Slot 8 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, eyebrows raised high and HELD, lips closing on a
question, chin lifted and waiting; his left hand is raised into frame with four
fingers extended and clearly separated, counting off the fourth point, right hand
parked flat on the counter below the frame line; warm overhead light. This slot is
an unanswered question - the expression must read as asking, not as concluding.
```

---

## Board 3 — CLOSER (Q4 answered, Q5, and the invitation)

```
Opening staging: the clip opens mid-answer. His palm is already coming down onto
the top of the glass case as the frame begins - reassurance delivered as a
physical gesture before the sentence finishes.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium distance: he pats the top of the glass display case twice with an open
palm, a settled easy expression, shoulders relaxed; right hand flat patting the
case top, left hand parked hanging at his side; gold chains visible under the
glass beneath his hand.

Slot 2 - exact 9:16 vertical still, selfie POV, tight distance: he holds the phone
close, head and shoulders filling the frame, looking directly into the lens with a
calm reassuring expression and a small single nod; right hand holds the phone
(hand faintly visible at the frame edge), left hand open palm-up at chest height;
warm daylight on his face.

Slot 3 - exact 9:16 vertical still, static camera POV, medium close-up distance:
he raises his right hand toward the lens with all five fingers spread and clearly
separated, counting off the fifth point, eyebrows lifted in a question; left hand
planted flat on the counter glass; daylight raking across the counter.

Slot 4 - exact 9:16 vertical still, static camera POV, wide distance: he has
stepped across to the back wall and stands beside the row of hanging guitars, his
right arm extended gesturing along the length of the row, left hand parked at his
side, the full gold cape down his back; even ambient shop daylight. Every guitar
headstock is completely plain and unbranded - no maker logos, no model names, no
lettering of any kind anywhere on any instrument.

Slot 5 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on his hands only, no face in frame - his left hand holds a jeweler's
loupe up to the light while his right hand turns the plain gold-tone ring beneath
it; exactly two hands in frame and nothing else; warm specular light across the
gold and the loupe glass.

Slot 6 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length as he walks back toward his place behind the counter,
framing off-center with a natural tilt; left hand holds the phone (forearm at the
frame edge), right hand open palm-up in a casual easy that-is-how gesture; the
jewelry cases sliding past behind him.

Slot 7 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, warm and direct into the lens with a genuine unforced
half-smile, mid-sentence; right hand parked flat on the counter glass below the
frame line, left hand parked at his side; storefront daylight on his face.

Slot 8 - exact 9:16 vertical still, static camera POV, wide distance: he stands
back behind the counter with both arms open wide at his sides, the full gold cape
spread and catching the light, the guitar wall behind him and the lit jewelry
cases running away on either side, an easy open expression; left arm open at his
side, right arm open at his side; bright even daylight. The lower third of the
frame is open counter surface and floor only - keep it visually quiet and
uncluttered, with nothing important in it.
```

**Why slot 8 has that last sentence.** The closing card — logo, phone, "five
stores" — burns into the lower third of the final beat. EP01 got away with it
because its last shot was a walk-away into an empty doorway. Stage a busy lower
third here and the card lands on top of merchandise.

---

## De-slop pass

Identical to EP01. Import each finished board with `media_import_url`, run
`seedream_v5_pro` at `21:9` / `2k` with that imported ID as `image_references`,
using the preservation prompt in `ep01-boards.md` verbatim. The cleaned job ID
replaces the raw board everywhere downstream.

On a moderation failure retry once with `seedream_v5_lite`; if that also fails,
keep the raw board and note the degradation.
