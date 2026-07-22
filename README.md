# Dick's Pawn Superstore — Website Redesign

A clean, conversion-focused redesign concept for [dickspawn.com](https://dickspawn.com).
Static HTML/CSS/JS — no build step, no dependencies.

**Live preview:** https://kylefriesmarketing.github.io/dicks-pawn-redesign/

---

## Pages

| File | Purpose |
|---|---|
| `index.html` | Homepage — hero, 4 action cards, live product strips, categories, 3-step sell funnel, why-us, sister brands, reviews, locations, final CTA |
| `shop.html` | Full catalog browser — search, 9 category filters, price sorting, in-stock toggle, paged loading |
| `sell.html` | Sell & Pawn — 3-step explainer, what-we-take grid, quote form, pawn FAQ |
| `services.html` | Jewelry repair, layaway/warranty, gold buying, Dick's Bullion, Dick's Title Loans |
| `about.html` | Company story (est. 1987, Surfside Beach), stats, credentials |
| `locations.html` | All 5 stores with embedded Google Maps, directions, click-to-call |

## Structure

```
assets/style.css      all styling (one file, CSS custom properties for theming)
assets/dp-logo.png    the real Dick's Pawn diamond logo (also the favicon)
js/products.js        catalog snapshot — 1,565 real products (453KB / 111KB gzipped)
js/details.json       galleries + descriptions, fetched only on first quick-view
js/shop.js            grid rendering, search, filters, sort, quick-view modal
gen-products.mjs      rebuilds both data files from their Shopify feed
serve.mjs             local dev server (node serve.mjs → localhost:8489)
```

## Features

- **Quick View** — click any product for a modal with the full photo gallery
  (up to 5 images), the real product description, SKU, and Buy / Call-to-Hold CTAs.
  Detail data is lazily fetched so the grid stays fast. Closes on Esc, backdrop
  click, or the X; restores focus and scroll.
- **Category + subcategory filters** — jewelry is ~64% of the catalog, so it
  subdivides into Rings / Necklaces / Pendants / Bracelets / Earrings / Watches.
- **Deep links** — `shop.html?cat=jewelry&sub=ring`, shareable and back-button safe.
- **Live search** across every title, price sorting, in-stock toggle.
- **Real product photography** on the homepage category tiles, pulled from the
  catalog at runtime — no stock photos, no generated art.
- **SEO** — `PawnShop` structured data for all 5 locations with hours and phone
  numbers, canonical URLs, Open Graph + Twitter cards on every page.
- **Accessibility** — skip links, `<main>` landmarks, `aria-pressed` filter state,
  live-region result counts, visible focus rings, labelled search.

## Brand

Pulled from the live site so it feels like *them*, not a generic template:

- **Navy** `#133564` — their existing button color, the logo shield
- **Red** `#d63031` — the logo's accent, used here for all primary CTAs
- **Gold** `#c9a24b` — Dick's Bullion
- **Jost** — the typeface their current site already uses

## The product catalog

`js/products.js` is a snapshot of **1,565 real, live items** pulled from their Shopify
storefront (`dickspawn.com/products.json`) — real titles, real prices, real photos
(served from Shopify's CDN), real product links.

Category breakdown (in stock): Jewelry & Gold 991 · Musical Instruments 131 ·
Video Games 101 · Tools 90 · Sporting Goods & Golf 74 · Designer & Handbags 57 ·
Electronics 50 · Sneakers 17 · Collectibles 6 · More Finds 10

### Their tag taxonomy (worth knowing before you touch `gen-products.mjs`)

Dick's staff tag products with short codes, and several are easy to misread —
getting them wrong silently files products under the wrong department:

| Code | Means | Not |
|---|---|---|
| `HW` | **H**andbags & **W**allets | ~~Hardware~~ |
| `SH` | **S**peakers & **H**eadphones | ~~Shoes~~ |
| `FH` | **F**ishing & outdoor | ~~Fine goods~~ |
| `FW` | Fine **W**atches & fashion accessories | ~~Footwear~~ |
| `OT` / `LG` | Other Tools / Lawn & Garden | |
| `G_` / `A_` | Gold / sterling silver jewelry, 2nd letter = **R**ing, **P**endant, **B**racelet, **E**arring, **N**ecklace | |

Reading `HW` as "hardware" put Louis Vuitton bags under Tools; reading `SH` as a
jewelry code put BOSE headphones under Jewelry. Both are fixed — see the comments
in `gen-products.mjs`.

**To refresh the catalog**, re-run the generator (see git history for `gen-products.mjs`),
or — better for production — swap `js/products.js` for a live fetch of
`https://dickspawn.com/products.json`, since this is a static snapshot that will drift
as inventory turns over.

## Before this goes live — action items

1. **Replace the 3 testimonial quotes** on `index.html`. They're clearly labeled
   *"Sample Review — replace with a real featured review."* The 4.9★ / 2,000+ figures
   are real and verified from their Google listing.
2. **Confirm store hours.** Mon–Sat 9am–6pm, closed Sunday, sourced from Yelp listings —
   worth verifying per location, since one store may differ.
3. **Wire up the quote form.** `sell.html`'s form currently opens the user's mail client
   (`mailto:`). For production, point it at a real form handler so submissions are tracked.
4. **Add real store photography.** The category tiles use gradient + emoji placeholders;
   real storefront and interior shots would lift the whole design.
5. **Product links** currently deep-link to the existing dickspawn.com Shopify product
   pages — so "View Item" always lands on a working, purchasable page.

## Notes

- Fully responsive; sticky Call / Get Cash bar appears on mobile.
- Every section ends in a call to action. ~29 CTAs on the homepage alone.
- Catalog is 440KB raw / **111KB gzipped**, loaded once and filtered client-side —
  so searching and filtering are instant with no server round-trips.
