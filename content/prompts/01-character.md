# Character prompt — Super Dick (the locked host)

Model `soul_2` · `3:4` · `2k` · one generation, reused across the entire series.

**Never regenerate this mid-series.** The returned `job_id` is the
`character_media_id` that every board and every clip references. Regenerating it
is how a series quietly loses its face between episodes.

## Prompt

```
A man in his late thirties, American, warm and quick-witted, a little weathered
like someone who works retail on his feet all day, with high model facial
features, symmetrical features, a well-proportioned solid build with broad
shoulders, and natural skin texture with visible pores, faint laugh lines at the
outer eyes, and light even stubble along the jaw. Short dark brown hair, neatly
cut, a little tousled at the front. Warm medium skin tone with a light coastal
tan. Wardrobe: a completely plain navy blue short-sleeve work polo, collar open
at the neck - the polo is plain navy fabric with NO patch, NO badge, NO emblem,
NO pocket, NO printing and NO decoration of any kind. Over it a rich gold satin
superhero cape, tied at the throat and sweeping back over BOTH shoulders so it
hangs down behind his back - clearly a flowing cape, never a shawl, never a wrap,
never draped over the front. Absolutely no text, no lettering, no letters, no
numbers, no writing, no signage and no readable characters anywhere in the entire
image. A warm, dry-witted counter guy who has heard every myth a thousand times
and enjoys knocking them down - easy-going, conversational, never salesy.
Expression: mid-action expression - in the middle of saying something, not
posing; eyebrows lifted slightly, eyes toward the lens, mouth barely parted.
Body: relaxed standing, shoulders square, weight easy on one leg, one hand
resting naturally, head level. Setting: inside a bright, tidy American pawn shop
- a long glass jewelry display case full of gold chains falling out of focus
behind him, a blurred row of hanging guitars on the back wall, warm overhead shop
light mixed with daylight from the storefront. Self-portrait selfie shot on
iPhone front-facing camera held by the subject at arm's length - head and
shoulders fill the frame, casual handheld framing, slight natural tilt, slightly
off-center, slightly imperfect, not posed. Phone-sensor grain and realistic skin
texture preserved, no retouch, no smooth-skin filter. No fisheye lens, no
ultra-wide distortion. Authentic UGC creator phone selfie, NOT editorial
portrait, NOT fashion magazine.
```

## The logo problem — read this before you change the prompt

The obvious move is to put the Dick's Pawn diamond on his chest. **Don't.**

Three generations were run to establish this:

| Attempt | Chest instruction | Result |
|---|---|---|
| 1 | "small embroidered diamond crest badge" | Diamond rendered, filled with gibberish letters |
| 2 | "solid flat diamond patch, no lettering, no interior detail" | Bigger blue sticker, *still* gibberish, cape degraded to a shawl |
| 3 | "plain navy, NO patch, NO badge, NO printing" | Chest clean, but cape degraded to a knotted scarf and the expression went gawky |

**Attempt 1 is the one in production.** Its badge renders as a small pale-blue
diamond with faint illegible stitching — at 1080p vertical, with the subject at
medium distance and moving, that reads as ordinary embroidery rather than as an
error. Attempt 1 also has the best cape drape (falling over both shoulders
rather than knotted at the throat) and the most usable mid-speech expression,
and those two things matter more than the badge because they are what the boards
and clips actually carry forward.

Image models hallucinate lettering into any branded shape, and the negative
instruction ("no text") reliably makes it worse, not better, because the model
attends to the noun and drops the negation. The fix is to never ask for the mark
at all.

**The real diamond-D goes on in post**, composited from `assets/dp-logo.png`
where it is crisp, correctly coloured, and actually theirs. The gold cape is
doing the brand-identity work in-frame; it does not need help.
