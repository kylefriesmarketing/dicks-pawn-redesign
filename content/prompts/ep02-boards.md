# Storyboard prompts — EP02 "Only One's Real"

Model `gpt_image_2` · `21:9` · `2k` · `quality: high` · 6.5 credits each.

Two plain gold chains on the counter. One is real, one is plated brass. Five
tests, each of which fails to settle it, and the reveal on the last beat. Same
machine as EP01: three sheets, eight 9:16 slots each, one horizontal row, eight
hard cuts per 15-second clip.

## Why this episode is not a list

The research (`content/research/ep02-viral-research.md`) is unambiguous: for real
pawn shops the formats that reliably clear a million views are transactions and
**live authenticity tests** — fake Rolex 11.9M, acid test 582K — while numbered
lists and FAQs on the same accounts run 10-25× lower. This is the one proven
mega-format an AI host can actually perform, and it has a genuine stakes →
escalation → payoff spine: a stake set in the first line, five tests that each
end on "still can't tell", the answer withheld to the last beat, an abrupt end.

The numerals still count 1-5 and the card system is unchanged (kicker `TEST`), so
it reads as the same series. What changes is that every beat is a **prop plus a
verdict**, not a claim.

## The one rule that makes it renderable: identity by position

The two chains look identical on purpose — plain gold-tone curb chains, no
stamp, no tag, no clasp label, no charm. Seedance cannot be trusted to keep two
similar objects distinct across 24 cuts by appearance. So they are told apart
**only by where they sit**:

- the **TRAY CHAIN** lies on a small plain black velvet tray — this is the fake
- the **GLASS CHAIN** lies on the bare counter glass beside it — this is real

Every slot that shows a chain says which one it is by where it sits or where it
was picked up from. Each board's opening staging puts both back in their places.
Nothing ever switches trays. If a render swaps them, that beat is cut or carded,
never explained.

## Props, all textless

| Prop | Rule |
|---|---|
| Two plain gold-tone curb chains | Identical; no stamp, tag, label or charm |
| Small plain black velvet tray | Matte, no lip text, no logo |
| Plain black disc magnet | No markings |
| Flat matte-black gold-testing stone | No text |
| Small brown-glass dropper bottle | **Completely unlabeled** — say it every time |
| Jeweler's loupe | Plain brass or black, unbranded |

The acid beat (board 2, slot 7) is the hardest render in the series. It passed a
5-second 480p smoke test on 2026-09-23 before any board was generated: two
streaks on the stone, one fizzing and fading to a dull green, one unchanged, the
bottle unlabeled, one clean hand. The prompt wording that produced that result is
reused verbatim in slot 7 and in clip 2 cut 7. If a full-resolution render fails
it, the fallback is a full-bleed card over the kept audio — never a re-roll.

## Reference chain

| Board | Role | Tests | medias (in order) |
|---|---|---|---|
| 1 | HOOK | 1-2: magnet, weight | character, **EP01 board 1** `fdf7972f-04ee-4e2f-a23d-a288505bc67d` |
| 2 | MAIN | 3-4: loupe, acid | character, EP02 board 1 |
| 3 | CLOSER | 5: the jeweler; reveal; CTA | character, EP02 board 2 |

Character `9024359d-0dd1-48a7-9665-e942806a4964` — **never regenerate.**

Board 1 anchors to EP01's board 1 so the room matches the episode already
shipped; within EP02, board K chains board K−1. Sequential, never parallel.

## Shared blocks

**HEADER, FOOTER and the de-slop prompt are byte-identical to
`ep01-boards.md`.** Copy them from there. All three boards use the K>1 header
variant (two reference images). Board 1's `@Image2` sentence reaches back an
episode:

```
@Image2 is a board from the previous episode of this same series, shot in the
same location on the same day - preserve its exact identity, location, counter,
light direction, time of day and wardrobe. This board continues the same unbroken
scene; nothing about the room or the man changes.
```

Boards 2 and 3 use the EP01 wording verbatim (`@Image2 is the previous board in
this same video...`).

**Every counting beat is TIGHT.** Board 1 slots 4 and 7, board 2 slots 2 and 5,
board 3 slot 2. All five of EP01's numerals landed tight or medium-close, which is
why each badge reads in sync with the counting hand.

---

## Board 1 — HOOK (tests 1-2: the magnet, the weight)

Insert after the header, before the footer:

```
Opening staging: the clip opens on the second chain landing - his right hand is
already releasing a plain gold-tone chain onto the bare counter glass as the
frame begins, directly beside a small plain black velvet tray that already holds
an identical chain. Two chains side by side, one on velvet, one on glass.

The two chains are identical in look - plain gold-tone curb chains, no stamp, no
tag, no clasp label, no charm - and are told apart ONLY by position: the TRAY
CHAIN lies on the black velvet tray, the GLASS CHAIN lies on the bare glass
beside it. Every slot that shows a chain says which one it is by where it sits or
where it was picked up from. Nothing ever switches trays.

The character has exactly two hands. In selfie POV slots one hand is occupied by
the phone, so only one hand is available for action. Every slot names what EACH
hand is doing - one role per hand, the idle hand parked explicitly - never more
than two simultaneous hand-roles. POV may change between slots; every POV change
aligns with a hard cut, never a smooth transition.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium distance: he stands behind the glass counter, his right hand just
releasing a plain gold-tone chain onto the bare glass, the chain settling into a
loose pile; beside it a small plain black velvet tray with the identical chain
lying on it; left hand planted flat on the glass; eyebrows lifted, mouth open
mid-word; gold cape over both shoulders; daylight raking across the counter.

Slot 2 - exact 9:16 vertical still, selfie POV, tight distance: he holds the
phone himself at arm's length, head and shoulders filling the frame, slightly
off-center with a natural tilt; right hand holds the phone (wrist faintly visible
at the frame edge), left hand raised open palm-up at chest height as if weighing
a question; one eyebrow up, a dry half-smile; warm overhead light on his face.

Slot 3 - exact 9:16 vertical still, static camera POV, wide distance: full body
behind the counter, the gold cape hanging the length of his back, the guitar wall
and the long jewelry case in frame, both chains visible on the counter in front
of him - one on the black tray, one on the glass; his right arm sweeps open along
the display case beside him, left hand parked resting on the counter edge; bright
ambient shop daylight.

Slot 4 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, brows up; his right hand is raised into the bottom of
frame with the index finger extended straight up counting off the first point,
left hand parked flat on the counter glass below frame; warm overhead light.

Slot 5 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the counter, no face in frame - the black velvet tray with its chain
and, beside it on the bare glass, the other chain; his right fingertips hold a
small plain black disc magnet, touching it to the chain on the tray; neither
chain moves or lifts; left hand absent from frame; warm specular glints on both
chains.

Slot 6 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length, walking half a step along the counter, framing off-center
with a natural tilt; left hand holds the phone (forearm grazing the frame edge),
right hand flat and level in a small cancelling wave - nothing happened; a small
shrug; storefront light behind him.

Slot 7 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, mouth mid-word; his left hand rises into frame with two
fingers extended and clearly separated counting off the second point, right hand
parked flat on the counter glass below the frame line; warm overhead light.

Slot 8 - exact 9:16 vertical still, static camera POV, medium close-up distance:
both palms up at chest height - the chain lifted from the black tray draped
across his left palm, the chain lifted from the bare glass draped across his
right palm - his eyes on his hands, brows raised high and HELD, lips closed, head
tipped a few degrees, genuinely unsure; daylight from the storefront on his face.
This slot is an unresolved beat - the expression reads as still-deciding, never
as concluding.
```

---

## Board 2 — MAIN (tests 3-4: the loupe, the acid)

```
Opening staging: the clip opens mid-inspection - a small plain jeweler's loupe is
already pressed to his right eye as the frame begins, and the clasp end of the
chain lifted from the black velvet tray is held up to it. Both chains started
this clip back in their places: the TRAY CHAIN on the black velvet tray, the
GLASS CHAIN on the bare glass. He lifts one at a time and returns it to where it
came from.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium close-up distance: leaning in over the counter, a small plain jeweler's
loupe held to his right eye by his right hand, the clasp end of the chain lifted
from the tray held up to the loupe in his left hand, his head tilted into it;
warm overhead light; the black tray and the chain on the bare glass visible on the
counter below.

Slot 2 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, eyebrows lifted; his right hand is raised into frame
with three fingers extended and clearly separated counting off the third point,
left hand parked flat on the counter glass below frame; warm overhead light.

Slot 3 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway, no face in frame - the loupe held in his right hand a few centimetres
above the clasp of the chain lying on the bare glass, the loupe glass magnifying
the links beneath it; left hand absent from frame; warm specular light on the
gold.

Slot 4 - exact 9:16 vertical still, selfie POV, medium distance: he holds the
phone at arm's length, framing off-center with a natural tilt; right hand holds
the phone (hand faintly visible at the frame edge), left hand flat and tilting
side to side in a so-so gesture; a small headshake, mouth pulled to one side;
storefront daylight behind him.

Slot 5 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, chin lifted; his left hand is raised into frame with
four fingers extended and clearly separated counting off the fourth point, right
hand parked flat on the counter below the frame line; warm overhead light.

Slot 6 - exact 9:16 vertical still, static camera POV, medium close-up distance:
leaning over the counter, eyes down; a flat matte-black gold-testing stone lies
on the glass and his right hand drags the chain lifted from the black tray across
it, leaving a short gold streak; his left hand holds the stone steady at its
edge; the other chain lies on the bare glass beside the stone; warm shop light.

Slot 7 - exact 9:16 vertical still, static camera POV, macro distance: tight
cutaway on the flat matte-black gold-testing stone on the counter glass, no face
in frame - two short gold-coloured streaks side by side, a clear drop sitting on
each; the left streak, from the chain on the glass, bright and unchanged under
its drop; the right streak, from the chain on the tray, fizzing with tiny bubbles
and fading into a dull greenish smear; his right hand holds a small plain
brown-glass dropper bottle, completely unlabeled, just above the stone; left hand
absent from frame; warm shop light glinting on the wet drops.

Slot 8 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest, his eyes lifting from the counter to the lens, brows
raised high and HELD, lips closed, a beat of stillness; warm overhead light.
This slot is an unresolved beat - the expression reads as watching-and-waiting,
never as concluding.
```

---

## Board 3 — CLOSER (test 5: the jeweler; the reveal; the invitation)

```
Opening staging: the clip opens on him already lifting the chain off the black
velvet tray between his right thumb and forefinger as the frame begins - the
suspect, held up to the light. The other chain lies on the bare glass. He knows;
the viewer is about to.

Slot 1 - exact 9:16 vertical photorealistic UGC iPhone still, static camera POV,
medium distance: behind the counter, the chain lifted from the black velvet tray
hanging from his right thumb and forefinger at chest height, catching the light;
left hand planted flat on the glass beside the chain lying on the bare glass; a
level, knowing expression; daylight across the counter.

Slot 2 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest; his right hand raised toward the lens with all five
fingers spread wide and clearly separated counting off the fifth point, brows up;
left hand planted flat on the counter glass below frame; warm overhead light.

Slot 3 - exact 9:16 vertical still, static camera POV, wide distance: he has
stepped back from the counter, full body, the gold cape down his back, the guitar
wall and the length of the jewelry case behind him; his right arm extended open,
gesturing along the case and the shop; left hand parked at his belt; even
ambient daylight. Every guitar headstock is completely plain and unbranded - no
maker logos, no model names, no lettering of any kind.

Slot 4 - exact 9:16 vertical still, selfie POV, medium close-up distance: he
holds the phone close; his left hand holds the chain from the black tray up
between his own eyes and the lens, close, eyes narrowed on it; right hand holds
the phone (hand faintly visible at the frame edge); warm daylight on his face.

Slot 5 - exact 9:16 vertical still, static camera POV, tight distance: close on
his face and upper chest; his right hand holds the chain lifted from the bare
glass up beside his face, a small confident nod, a settled expression; left hand
parked flat on the counter below frame; warm overhead light.

Slot 6 - exact 9:16 vertical still, static camera POV, medium distance: behind
the counter, his right hand holding the chain from the black tray up, a dry
half-grin, in the act of dropping it back onto the velvet; left hand flat on the
glass; the other chain lying on the bare glass; daylight across the counter.

Slot 7 - exact 9:16 vertical still, selfie POV, tight distance: he holds the
phone close, head and shoulders filling the frame, warm and direct into the lens
with a genuine unforced half-smile; right hand holds the phone (hand faintly
visible at the frame edge), left hand open palm-up at chest height in
invitation; storefront daylight on his face.

Slot 8 - exact 9:16 vertical still, static camera POV, wide distance: he stands
back behind the counter with both arms open wide at his sides, the full gold cape
spread and catching the light, the guitar wall behind him and the lit jewelry
cases running away on either side, both chains on the counter in front of him,
an easy open expression; left arm open at his side, right arm open at his side;
bright even daylight. The lower third of the frame is open counter surface and
floor only - keep it visually quiet and uncluttered, with nothing important in
it.
```

The closing card burns into the lower third of the final beat; a busy lower
third puts it on top of merchandise.

---

## De-slop pass

Identical to EP01: import each finished board with `media_import_url`, run
`seedream_v5_pro` at `21:9` / `2k` with that imported ID as `image_references`
and the preservation prompt from `ep01-boards.md` verbatim. The cleaned job ID
replaces the raw board everywhere downstream. On a moderation failure retry once
with `seedream_v5_lite`; if that also fails, keep the raw board and note it.
