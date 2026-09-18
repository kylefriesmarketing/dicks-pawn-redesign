# Character prompt — Super Dick (the locked host)

Model `soul_2` · `3:4` · `2k`, then the real logo composited on in post.
One asset, reused across the entire series.

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

## The logo problem — and how it was actually solved

The obvious move is to prompt the Dick's Pawn diamond onto his chest. **It does
not work.** Four separate attempts, all failed the same way:

| Chest instruction | Result |
|---|---|
| "small embroidered diamond crest badge" | Diamond rendered, filled with gibberish letters |
| "solid flat diamond patch, no lettering, no interior detail" | Bigger blue sticker, still gibberish |
| "plain navy, NO patch, NO badge" | Clean, but no mark at all |
| "diamond shield emblem, deep blue, white and red border" | Rendered as a Superman-style shield, not their diamond |

Image models hallucinate lettering into any branded shape, and negating it
("no text") makes it worse, because the model attends to the noun and drops the
negation.

**The fix is compositing, not prompting.** Generate a completely plain polo,
then composite `assets/dp-logo.png` — the real file — onto the chest:

```bash
convert assets/dp-logo.png -resize 150x150 lg.png
composite -geometry +455+1155 lg.png host.png super-dick-host.png
```

150px at 1536×2048, left chest. Larger crowds the cape; smaller stops reading
once there is motion. The result is the genuine mark, pixel-exact, instead of an
AI approximation of it.

**What this does and does not buy you.** The character reference now carries the
real logo, so every board and clip generated from it renders a far closer
likeness than a described one. But Seedance still *repaints* it each frame — the
video will show a good approximation, not a pixel-perfect logo. For a mark that
is genuinely exact on screen, the persistent corner logo burned in post is the
one to trust, and that one already is exact.

## Wardrobe: why cotton, and why gold

Two realism findings worth not relearning:

**The garment decides the realism.** A spandex superhero suit renders as CGI
almost regardless of prompt — smooth synthetic fabric has no weave, no wrinkle
behaviour and no matte falloff, so the model has nothing to render honestly and
defaults to flat saturated colour. A cotton pique polo forces visible knit,
creasing at the sleeve hems, and rumpling at the shoulders. Every photoreal
version in this series is cotton; every plastic-looking one is spandex.

**No head covering.** A cowl prompted plainly renders as a swim cap; prompted
with structure it renders as a balaclava with eye holes. Beyond looking wrong, a
masked figure in a video whose first line is "it's all stolen" is the worst
available optic. Bare head, own hair — which also keeps the whole face readable
for lip-sync.

The cape is gold, not red: it ties to Dick's Bullion, catches the shop light, and
leaves red free to mean only the on-screen numbers and CTAs.

## Set: white slatwall, not pine

An early read of the store photos made knotty pine the dominant wall and
produced rooms that did not look like the shop. The real ratio is the reverse:

- **White horizontal-grooved slatwall is most of the wall**, densely hung with
  merchandise
- **Knotty pine is accent columns and trim** between the slatwall panels
- Drop ceiling of acoustic tiles with recessed fluorescent panels **and** black
  track-lighting rails
- Warm medium-brown wood-look plank laminate floor
- Counters: grey speckled laminate tops, wood-panelled fronts, navy blue trim
- Glass cases lit and packed with gold chains

And the store is **busy**. Sparse, tidy renders read as a showroom; the real
place is stocked wall to wall. Say "cluttered, well-stocked, lived-in — a
working shop, not a showroom" and it lands.
