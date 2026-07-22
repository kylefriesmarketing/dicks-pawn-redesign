/* Build the site catalog from Dick's Pawn's live Shopify feed.
 *
 * Usage:
 *   1. curl "https://dickspawn.com/products.json?limit=250&page=N" -o prodN.json   (N = 1..7)
 *   2. node gen-products.mjs
 *
 * Emits two files, split so the shop grid loads fast and detail is fetched on demand:
 *   js/products.js  — lean list used to render the grid
 *   js/details.json — gallery images + descriptions, lazily fetched by the quick-view modal
 */
import fs from 'fs';

const all = [];
for (let p = 1; p <= 7; p++) {
  const f = `prod${p}.json`;
  if (!fs.existsSync(f)) continue;
  JSON.parse(fs.readFileSync(f, 'utf8')).products.forEach(x => all.push(x));
}
if (!all.length) { console.error('No prodN.json files found — fetch them first (see header).'); process.exit(1); }

/* --- Dick's Pawn's internal tag taxonomy, decoded from their live catalog ---------
 * Their staff tag by short codes. Getting these right matters: several were being
 * read as the wrong words, which put Louis Vuitton bags under "Tools" (HW read as
 * Hardware instead of Handbags & Wallets) and BOSE headphones under "Jewelry".
 *
 *   G_ = gold jewelry      GR ring  GP pendant  GB bracelet  GE earring  GN necklace
 *   A_ = sterling silver    AR ring  AP pendant  AB bracelet  AE earring  AN necklace
 *   FW = fine watches & fashion accessories (watches, sunglasses, keychains)
 *   HW = handbags & wallets            SH = speakers & headphones
 *   FH = fishing & outdoor             OT = other tools        LG = lawn & garden
 */
const JEWELRY_CODE = /^(g|a)(r|p|b|e|n)$/;           // GR, AP, GB, AE, AN …
const SUB_BY_CODE  = { r: 'ring', p: 'pendant', b: 'bracelet', e: 'earring', n: 'necklace' };

/* Luxury houses — these win over a generic tag. */
const LUXURY = /\b(louis vuitton|gucci|dior|chanel|prada|versace|fendi|balenciaga|givenchy|burberry|hermes|hermès|manolo blahnik|dolce\s*&?\s*gabbana|jimmy choo|valentino|saint laurent|ysl|bottega|brahmin|coach|michael kors|kate spade)\b/i;
/* Signed / authenticated sports memorabilia.
   Suffixes matter: a trailing \b would miss "Autographed".
   "Signature" is deliberately NOT here — it's a product-line word in music gear
   (Signature Series pedals, guitars) and produced false memorabilia matches. */
const MEMORABILIA = /\b(signed|autograph\w*|authenticated|certificate of authenticity|coa)\b/i;

function category(p) {
  const tags = (p.tags || []).map(t => t.toLowerCase());
  const title = p.title.toLowerCase();
  const has = (...ws) => tags.some(t => ws.some(w => t === w || t.startsWith(w)));
  const code = c => tags.includes(c);

  // 1. Their own jewelry codes are authoritative — check before anything else.
  if (tags.some(t => JEWELRY_CODE.test(t))) return 'jewelry';

  // 2. Unambiguous single-purpose codes.
  if (code('hw')) return 'designer';                       // handbags & wallets
  if (code('sh')) return 'elec';                           // speakers & headphones
  if (code('fh')) return 'sport';                          // fishing & outdoor
  if (code('fw')) {                                        // watches / sunglasses / accessories
    return /glass|sunglass|shade/.test(title) ? 'designer' : 'jewelry';
  }

  // 3. Brand and content signals.
  if (LUXURY.test(p.title)) return 'designer';
  if (MEMORABILIA.test(p.title)) return 'collect';

  // 4. Department tags.
  if (has('video games','playstation','nintendo','xbox','retrog','sega')) return 'games';
  if (has('music','guitar','amp','dj','drum','mgear','keyboard')) return 'music';
  if (has('tools','drill','saw','nail','ot','lg')) return 'tools';
  if (has('sporting goods','golf','fishing','bike','surf')) return 'sport';
  if (has('shoes','sneaker','jordan','nike','adidas')) return 'shoes';
  if (has('handbag','purse','wallet','sunglasses','designer')) return 'designer';
  if (has('cards','collectible','coin','bullion')) return 'collect';
  if (has('electronics','car audio','car','speaker','headphone','tv','camera','computer','tablet')) return 'elec';
  if (has('jewelry')) return 'jewelry';

  // 5. Last resort — read the title.
  if (/ring|necklace|bracelet|pendant|earring|chain|diamond|gold|sterling|silver|watch/.test(title)) return 'jewelry';
  return 'other';
}

/* Sub-buckets so the ~1,000-item jewelry category stays browsable.
   Prefers their tag code; falls back to the title. */
function subcategory(cat, p) {
  if (cat !== 'jewelry') return '';
  const coded = (p.tags || []).map(t => t.toLowerCase()).find(t => JEWELRY_CODE.test(t));
  if (coded) return SUB_BY_CODE[coded[1]];
  const t = p.title.toLowerCase();
  if (/watch/.test(t)) return 'watch';
  if (/\brings?\b/.test(t)) return 'ring';
  if (/earring|stud/.test(t)) return 'earring';
  if (/bracelet|bangle|cuff/.test(t)) return 'bracelet';
  if (/necklace|chain|choker/.test(t)) return 'necklace';
  if (/pendant|charm|locket/.test(t)) return 'pendant';
  return 'other';
}

/* Shopify supports inline resize via a _WxH suffix before the extension. */
const sized = (src, w) => src ? src.replace(/(\.(jpg|jpeg|png|webp|gif))(\?|$)/i, `_${w}x$1$3`) : '';

const clean = html => (html || '')
  .replace(/<[^>]*>/g, ' ')
  .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&quot;/g, '"')
  .replace(/&#39;|&rsquo;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>')
  .replace(/\s+/g, ' ').trim();

/* Trim to a sentence if one ends near the limit, otherwise to a whole word —
   never mid-word, which reads like the page broke. */
function trim(text, max) {
  if (text.length <= max) return text;
  const cut = text.slice(0, max);
  const sentence = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('! '), cut.lastIndexOf('? '));
  if (sentence > max * 0.6) return cut.slice(0, sentence + 1);
  const word = cut.lastIndexOf(' ');
  return (word > 0 ? cut.slice(0, word) : cut).replace(/[,;:]$/, '') + '…';
}

const list = [];
const details = {};

for (const p of all) {
  const v = p.variants && p.variants[0];
  const img = p.images && p.images[0] && p.images[0].src;
  const price = v ? parseFloat(v.price) : NaN;
  if (!v || !img || !(price > 0) || !p.handle) continue;

  const cat = category(p);
  const rec = {
    t: p.title.slice(0, 140),
    p: price,
    i: sized(img, 480),
    h: p.handle,
    a: v.available ? 1 : 0,
    c: cat,
    d: Date.parse(p.created_at) || 0
  };
  const sub = subcategory(cat, p);
  if (sub) rec.s = sub;
  const cp = parseFloat(v.compare_at_price);
  if (cp && cp > price) rec.cp = cp;
  list.push(rec);

  // Detail payload — gallery + description, fetched only when a quick-view opens.
  details[p.handle] = {
    g: (p.images || []).slice(0, 5).map(im => sized(im.src, 800)),
    b: trim(clean(p.body_html), 600),
    v: p.vendor || '',
    sku: v.sku || ''
  };
}

list.sort((a, b) => b.d - a.d);

fs.mkdirSync('js', { recursive: true });
fs.writeFileSync('js/products.js',
  `// Catalog snapshot from dickspawn.com (Shopify products.json) — generated ${new Date().toISOString().slice(0, 10)}\n` +
  `// Regenerate with: node gen-products.mjs   (see file header for the fetch step)\n` +
  `const CATALOG = ${JSON.stringify(list)};\n`);
fs.writeFileSync('js/details.json', JSON.stringify(details));

const counts = {};
list.forEach(r => counts[r.c] = (counts[r.c] || 0) + 1);
const subs = {};
list.filter(r => r.s).forEach(r => subs[r.s] = (subs[r.s] || 0) + 1);
console.log('products:', list.length, '| in stock:', list.filter(r => r.a).length);
console.log('categories:', counts);
console.log('jewelry subcategories:', subs);
console.log('products.js', (fs.statSync('js/products.js').size / 1024).toFixed(0) + 'KB',
            '| details.json', (fs.statSync('js/details.json').size / 1024).toFixed(0) + 'KB');
