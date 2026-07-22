/* Generate a static page per product, the 5 location landing pages, and sitemap.xml.
 *
 * Static (not client-rendered) on purpose: these pages exist to be indexed, and
 * a crawler should get complete HTML with Product schema on first byte.
 *
 * Run after gen-products.mjs:
 *   node gen-pages.mjs
 */
import fs from 'fs';

const BASE = 'https://kylefriesmarketing.github.io/dicks-pawn-redesign/';
const PHONE_MAIN = '8436467166';

const src = fs.readFileSync('js/products.js', 'utf8');
const CATALOG = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
const DETAILS = JSON.parse(fs.readFileSync('js/details.json', 'utf8'));

const CATS = {
  jewelry: 'Jewelry & Gold', elec: 'Electronics', games: 'Video Games',
  music: 'Musical Instruments', tools: 'Tools & Hardware', sport: 'Sporting Goods & Golf',
  designer: 'Designer & Handbags', shoes: 'Sneakers', collect: 'Collectibles', other: 'More Finds'
};

const STORES = [
  { slug: 'north-myrtle-beach', name: "Dick's Pawn Superstore North", city: 'North Myrtle Beach',
    street: '860 Highway 17 S', zip: '29582', phone: '8436467166',
    blurb: 'Our North Myrtle Beach store sits right on Highway 17 South, serving Little River, Cherry Grove, Ocean Drive and the north end of the Grand Strand.',
    nearby: ['Little River', 'Cherry Grove', 'Ocean Drive', 'Atlantic Beach', 'Calabash'] },
  { slug: 'myrtle-beach', name: "Dick's Pawn Superstore East", city: 'Myrtle Beach',
    street: '1852 Mr. Joe White Avenue', zip: '29577', phone: '8436467166',
    blurb: 'Our Mr. Joe White Avenue store is minutes from the Boardwalk and downtown Myrtle Beach — the closest Dick\'s to the oceanfront hotels and Broadway at the Beach.',
    nearby: ['Downtown Myrtle Beach', 'The Boardwalk', 'Broadway at the Beach', 'Market Common', 'Withers Swash'] },
  { slug: 'carolina-forest', name: "Dick's Pawn Superstore West", city: 'Myrtle Beach (Carolina Forest)',
    street: '4765 Hwy 501', zip: '29579', phone: '8436467143',
    blurb: 'Our Highway 501 store serves Carolina Forest, Forestbrook and everyone heading in from Conway — easy parking and a big floor.',
    nearby: ['Carolina Forest', 'Forestbrook', 'Socastee', 'River Oaks', 'Waterway Hills'] },
  { slug: 'surfside-beach', name: "Dick's Pawn Superstore South", city: 'Surfside Beach',
    street: '1155 Dick Pond Rd', zip: '29575', phone: '8436467166',
    blurb: 'Where it all started. Our Dick Pond Road store on Highway 544 has served Surfside Beach, Garden City and Murrells Inlet since 1987.',
    nearby: ['Garden City', 'Murrells Inlet', 'Socastee', 'Litchfield', 'Pawleys Island'] },
  { slug: 'conway', name: "Dick's Pawn Superstore Conway", city: 'Conway',
    street: '2564 Main St', zip: '29526', phone: '8436467166',
    blurb: 'Our Main Street store serves Conway, Aynor and inland Horry County — the same fair deals, a little further from the sand.',
    nearby: ['Aynor', 'Loris', 'Bucksport', 'Homewood', 'Horry County'] }
];

const esc = s => String(s == null ? '' : s)
  .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
const money = n => '$' + n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

/* ---------- shared chrome ---------- */
function head({ title, desc, canonical, image, depth, ld }) {
  const up = '../'.repeat(depth);
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
<link rel="icon" type="image/png" href="${up}assets/dp-logo.png">
<link rel="apple-touch-icon" href="${up}assets/dp-logo.png">
<meta name="theme-color" content="#133564">
<link rel="canonical" href="${canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Dick's Pawn Superstore">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:image" content="${image}">
<meta property="og:url" content="${canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(title)}">
<meta name="twitter:description" content="${esc(desc)}">
<meta name="twitter:image" content="${image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="${up}assets/style.css">
<script type="application/ld+json">
${JSON.stringify(ld, null, 1)}
</script>
</head>
<body>

<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <div class="wrap">
    <div class="topbar-left">
      <span><span class="star">★</span> <b>4.9</b> · 2,000+ Google Reviews</span>
      <span class="hide-m">📍 <b>5 Locations</b> on the Grand Strand</span>
      <span class="hide-m">🕘 Mon–Sat 9am–6pm</span>
    </div>
    <div class="topbar-right"><a href="tel:${PHONE_MAIN}">📞 (843) 646-7166</a></div>
  </div>
</div>

<header class="site">
  <div class="wrap">
    <a class="brand" href="${up}index.html">
      <img src="${up}assets/dp-logo.png" alt="Dick's Pawn Superstore diamond logo">
      <span class="brand-name">DICK'S PAWN<small>Superstore · Est. 1987</small></span>
    </a>
    <nav class="main">
      <a href="${up}index.html">Home</a>
      <a href="${up}shop.html">Shop</a>
      <a href="${up}sell.html">Sell &amp; Pawn</a>
      <a href="${up}services.html">Services</a>
      <a href="${up}about.html">About</a>
      <a href="${up}locations.html">Locations</a>
    </nav>
    <div class="header-cta"><a class="btn btn-red" href="${up}sell.html">Get Cash Today</a></div>
  </div>
</header>

<main id="main" tabindex="-1">`;
}

function foot(depth) {
  const up = '../'.repeat(depth);
  return `</main>

<footer>
  <div class="wrap">
    <div class="foot-main">
      <div class="foot-brand">
        <img src="${up}assets/dp-logo.png" alt="Dick's Pawn Superstore logo">
        <p>The Grand Strand's family-owned pawn superstore since 1987. Buy, sell, and pawn with people you can trust.</p>
        <div class="badges"><span class="badge">BBB A+</span><span class="badge">MB Chamber</span><span class="badge">Natl. Pawn Brokers Assoc.</span></div>
      </div>
      <div>
        <h4>Shop</h4>
        <ul>
          <li><a href="${up}shop.html">All Inventory</a></li>
          <li><a href="${up}shop.html?cat=jewelry">Jewelry &amp; Gold</a></li>
          <li><a href="${up}shop.html?cat=elec">Electronics</a></li>
          <li><a href="${up}shop.html?cat=games">Video Games</a></li>
          <li><a href="${up}shop.html?cat=music">Instruments</a></li>
        </ul>
      </div>
      <div>
        <h4>Locations</h4>
        <ul>
${STORES.map(s => `          <li><a href="${up}locations/${s.slug}.html">${esc(s.city)}</a></li>`).join('\n')}
        </ul>
      </div>
      <div class="foot-contact">
        <h4>Contact</h4>
        <ul>
          <li><b>Call us</b><a href="tel:${PHONE_MAIN}">(843) 646-7166</a></li>
          <li><b>Email</b><a href="mailto:dickspawnsuperstore@gmail.com">dickspawnsuperstore@gmail.com</a></li>
          <li><b>Hours</b>Mon–Sat 9am–6pm · Sun closed</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Dick's Pawn Superstore. All rights reserved.</span>
      <span>14-Day Returns · 100% Secure Checkout · Licensed &amp; Insured</span>
    </div>
  </div>
</footer>

<div class="mob-cta">
  <a class="btn btn-navy" href="tel:${PHONE_MAIN}">📞 Call Now</a>
  <a class="btn btn-red" href="${up}sell.html">💰 Get Cash</a>
</div>

<script src="${up}js/nav.js"></script>
</body>
</html>
`;
}

/* ---------- product pages ---------- */
function productPage(p) {
  const d = DETAILS[p.h] || {};
  const gallery = (d.g && d.g.length ? d.g : [p.i]);
  const desc = d.b || `${p.t} — in stock now at Dick's Pawn Superstore on the Grand Strand.`;
  const metaDesc = `${p.t} — ${money(p.p)} at Dick's Pawn Superstore, Myrtle Beach SC. ${p.a ? 'In stock now.' : 'Recently sold.'} 5 locations, 14-day returns.`;
  const canonical = `${BASE}p/${p.h}.html`;

  const ld = {
    '@context': 'https://schema.org', '@type': 'Product',
    name: p.t, image: gallery, description: desc,
    sku: d.sku || undefined,
    brand: { '@type': 'Brand', name: (d.v && !/^Dick's/i.test(d.v)) ? d.v : "Dick's Pawn Superstore" },
    category: CATS[p.c] || 'Pre-owned',
    offers: {
      '@type': 'Offer', url: canonical, priceCurrency: 'USD', price: p.p.toFixed(2),
      itemCondition: 'https://schema.org/UsedCondition',
      availability: p.a ? 'https://schema.org/InStock' : 'https://schema.org/SoldOut',
      seller: { '@type': 'Organization', name: "Dick's Pawn Superstore" }
    }
  };

  // Related: same category, in stock, nearest in price.
  const related = CATALOG
    .filter(x => x.a && x.c === p.c && x.h !== p.h)
    .sort((a, b) => Math.abs(a.p - p.p) - Math.abs(b.p - p.p))
    .slice(0, 4);

  const thumbs = gallery.length > 1
    ? `<div class="qv-thumbs">${gallery.map((g, i) =>
        `<button class="qv-thumb${i === 0 ? ' on' : ''}" type="button" data-src="${esc(g)}" aria-label="View image ${i + 1}"><img loading="lazy" src="${esc(g)}" alt=""></button>`).join('')}</div>`
    : '';

  return head({ title: `${p.t} — ${money(p.p)} | Dick's Pawn Superstore`, desc: metaDesc,
                canonical, image: gallery[0], depth: 1, ld })
  + `
<div class="wrap">
  <div class="crumb pdp-crumb"><a href="../index.html">Home</a> / <a href="../shop.html">Shop</a> / <a href="../shop.html?cat=${p.c}">${esc(CATS[p.c] || 'Items')}</a></div>
</div>

<section class="pdp">
  <div class="wrap pdp-grid">
    <div class="pdp-media">
      <div class="qv-main"><img id="pdp-img" src="${esc(gallery[0])}" alt="${esc(p.t)}"></div>
      ${thumbs}
    </div>
    <div class="pdp-info">
      <span class="qv-cat">${esc(CATS[p.c] || 'Item')}</span>
      <h1>${esc(p.t)}</h1>
      <div class="qv-price">${money(p.p)}${p.cp ? `<s>${money(p.cp)}</s>` : ''}</div>
      <span class="qv-stock ${p.a ? 'in' : 'out'}">${p.a ? '✔ In stock now' : 'Sold out'}</span>
      <p class="qv-desc">${esc(desc)}</p>
      ${d.sku ? `<div class="qv-meta">SKU ${esc(d.sku)}${d.v ? ' · Sold by ' + esc(d.v) : ''}</div>` : ''}
      <div class="qv-ctas">
        ${p.a
          ? `<a class="btn btn-red btn-lg" href="https://dickspawn.com/products/${esc(p.h)}" target="_blank" rel="noopener">Buy Online <span class="arrow">→</span></a>
             <a class="btn btn-outline btn-lg" href="tel:${PHONE_MAIN}">📞 Call to Hold</a>`
          : `<a class="btn btn-outline btn-lg" href="tel:${PHONE_MAIN}">📞 Ask About Similar</a>
             <a class="btn btn-red btn-lg" href="../shop.html?cat=${p.c}">See What's In Stock <span class="arrow">→</span></a>`}
      </div>
      <ul class="pdp-trust">
        <li>✔ 14-day returns</li>
        <li>✔ Inspected &amp; tested in store</li>
        <li>✔ Layaway available</li>
        <li>✔ Free pickup at any of our 5 stores</li>
      </ul>
    </div>
  </div>
</section>

<section class="steps pdp-related">
  <div class="wrap">
    <div class="strip-head">
      <div>
        <span class="kicker">You Might Also Like</span>
        <h2 class="sec-title">More in ${esc(CATS[p.c] || 'the store')}</h2>
      </div>
      <a class="btn btn-navy" href="../shop.html?cat=${p.c}">Shop All <span class="arrow">→</span></a>
    </div>
    <div class="p-grid">
${related.map(r => `      <div class="p-card">
        <div class="p-img"><img loading="lazy" src="${esc(r.i)}" alt="${esc(r.t)}"></div>
        <div class="p-body">
          <div class="p-title">${esc(r.t)}</div>
          <div class="p-price">${money(r.p)}</div>
          <a class="p-cta" href="${esc(r.h)}.html">View Item <span class="arrow">→</span></a>
        </div>
      </div>`).join('\n')}
    </div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <h2>Got something to sell?</h2>
    <p>We buy items like this every day. Bring yours in for a free, no-obligation cash offer.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-navy btn-lg" href="../sell.html">💰 Get a Free Quote</a>
      <a class="btn btn-ghost btn-lg" href="../locations.html">📍 Find a Store</a>
    </div>
  </div>
</section>

<script>
(function () {
  var thumbs = document.querySelector('.qv-thumbs');
  if (!thumbs) return;
  thumbs.addEventListener('click', function (e) {
    var b = e.target.closest('.qv-thumb');
    if (!b) return;
    document.getElementById('pdp-img').src = b.dataset.src;
    thumbs.querySelectorAll('.qv-thumb').forEach(function (t) { t.classList.toggle('on', t === b); });
  });
})();
</script>
` + foot(1);
}

/* ---------- location pages ---------- */
function locationPage(s) {
  const canonical = `${BASE}locations/${s.slug}.html`;
  const mapQ = encodeURIComponent(`Dick's Pawn Superstore ${s.street} ${s.city} SC`);
  const ld = {
    '@context': 'https://schema.org', '@type': 'PawnShop',
    '@id': canonical + '#store', name: s.name, url: canonical,
    image: `${BASE}assets/og-card.jpg`, telephone: '+1' + s.phone,
    priceRange: '$'.repeat(2), email: 'dickspawnsuperstore@gmail.com',
    parentOrganization: { '@type': 'Organization', name: "Dick's Pawn Superstore", url: BASE },
    address: { '@type': 'PostalAddress', streetAddress: s.street, addressLocality: s.city.replace(/\s*\(.*\)/, ''),
               addressRegion: 'SC', postalCode: s.zip, addressCountry: 'US' },
    areaServed: s.nearby.map(n => ({ '@type': 'Place', name: n })),
    openingHoursSpecification: [{ '@type': 'OpeningHoursSpecification',
      dayOfWeek: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'], opens: '09:00', closes: '18:00' }],
    aggregateRating: { '@type': 'AggregateRating', ratingValue: '4.9', reviewCount: '2000' }
  };

  const title = `Pawn Shop in ${s.city.replace(/\s*\(.*\)/, '')}, SC | ${s.name}`;
  const desc = `${s.name} at ${s.street}, ${s.city.replace(/\s*\(.*\)/, '')} SC. Buy, sell and pawn — jewelry, electronics, tools and more. Open Mon–Sat 9–6. Call ${s.phone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3')}.`;

  return head({ title, desc, canonical, image: `${BASE}assets/og-card.jpg`, depth: 1, ld })
  + `
<div class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="../index.html">Home</a> / <a href="../locations.html">Locations</a> / ${esc(s.city)}</div>
    <h1>Pawn Shop in ${esc(s.city.replace(/\s*\(.*\)/, ''))}, SC</h1>
    <p>${esc(s.blurb)}</p>
    <div class="hero-ctas">
      <a class="btn btn-red btn-lg" href="tel:${s.phone}">📞 Call This Store</a>
      <a class="btn btn-ghost btn-lg" href="https://maps.google.com/?q=${mapQ}" target="_blank" rel="noopener">📍 Get Directions</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap loc-detail">
    <div class="loc-detail-info">
      <span class="kicker">Store Details</span>
      <h2 class="sec-title">${esc(s.name)}</h2>
      <address class="loc-address">
        ${esc(s.street)}<br>${esc(s.city.replace(/\s*\(.*\)/, ''))}, SC ${s.zip}
      </address>
      <p class="loc-line"><b>Phone</b> <a href="tel:${s.phone}">${s.phone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3')}</a></p>
      <p class="loc-line"><b>Hours</b> Monday–Saturday 9:00am–6:00pm · Closed Sunday</p>
      <p class="loc-line"><b>Email</b> <a href="mailto:dickspawnsuperstore@gmail.com">dickspawnsuperstore@gmail.com</a></p>
      <div class="loc-ctas" style="margin-top:18px">
        <a class="btn btn-navy" href="https://maps.google.com/?q=${mapQ}" target="_blank" rel="noopener">Directions</a>
        <a class="btn btn-outline" href="tel:${s.phone}">Call</a>
      </div>
      <h3 class="loc-sub">Serving</h3>
      <p class="sec-sub">${s.nearby.map(esc).join(' · ')}</p>
    </div>
    <div class="loc-detail-map">
      <iframe loading="lazy" title="Map — ${esc(s.name)}" src="https://maps.google.com/maps?q=${mapQ}&z=14&output=embed"></iframe>
    </div>
  </div>
</section>

<section class="steps">
  <div class="wrap center">
    <span class="kicker">What You Can Do Here</span>
    <h2 class="sec-title">Everything, under one roof</h2>
    <div class="steps-grid">
      <div class="step"><div class="step-num">💰</div><h3>Sell or Pawn</h3><p>Free appraisals on jewelry, electronics, tools and more. No credit check, cash on the spot.</p></div>
      <div class="step"><div class="step-num">💎</div><h3>Jewelry Repair</h3><p>An experienced jeweler is on staff here every day — many repairs done while you wait.</p></div>
      <div class="step"><div class="step-num">🛍️</div><h3>Shop the Floor</h3><p>New items arrive daily. Browse online and pick up here for free.</p></div>
    </div>
    <a class="btn btn-red btn-lg" href="../shop.html">Browse 1,500+ Items <span class="arrow">→</span></a>
  </div>
</section>

<section>
  <div class="wrap center">
    <span class="kicker">Our Other Stores</span>
    <h2 class="sec-title">Four more along the Grand Strand</h2>
    <div class="loc-grid" style="margin-top:34px">
${STORES.filter(o => o.slug !== s.slug).map(o => `      <div class="loc-card">
        <div class="pin">📍</div>
        <h3>${esc(o.city.replace(/\s*\(.*\)/, ''))}</h3>
        <address>${esc(o.street)}<br>${esc(o.city.replace(/\s*\(.*\)/, ''))}, SC ${o.zip}</address>
        <a class="tel" href="tel:${o.phone}">${o.phone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3')}</a>
        <div class="loc-ctas"><a class="btn btn-navy btn-sm" href="${o.slug}.html">Store Page</a></div>
      </div>`).join('\n')}
    </div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <h2>Stop by ${esc(s.city.replace(/\s*\(.*\)/, ''))} today</h2>
    <p>Walk-ins always welcome — no appointment needed. Open Monday through Saturday, 9am to 6pm.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-navy btn-lg" href="tel:${s.phone}">📞 Call ${s.phone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3')}</a>
      <a class="btn btn-ghost btn-lg" href="../sell.html">💰 Get a Cash Quote</a>
    </div>
  </div>
</section>
` + foot(1);
}

/* ---------- write everything ---------- */
fs.mkdirSync('p', { recursive: true });
fs.mkdirSync('locations', { recursive: true });

let n = 0;
for (const p of CATALOG) { fs.writeFileSync(`p/${p.h}.html`, productPage(p)); n++; }
for (const s of STORES) fs.writeFileSync(`locations/${s.slug}.html`, locationPage(s));

/* sitemap — static pages, all products, all stores */
const today = new Date().toISOString().slice(0, 10);
const urls = [
  { loc: BASE, pri: '1.0' },
  { loc: BASE + 'shop.html', pri: '0.9' },
  { loc: BASE + 'sell.html', pri: '0.9' },
  { loc: BASE + 'services.html', pri: '0.7' },
  { loc: BASE + 'about.html', pri: '0.6' },
  { loc: BASE + 'locations.html', pri: '0.8' },
  ...STORES.map(s => ({ loc: `${BASE}locations/${s.slug}.html`, pri: '0.8' })),
  ...CATALOG.filter(p => p.a).map(p => ({ loc: `${BASE}p/${p.h}.html`, pri: '0.6' }))
];
fs.writeFileSync('sitemap.xml',
  '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
  + urls.map(u => `<url><loc>${u.loc}</loc><lastmod>${today}</lastmod><priority>${u.pri}</priority></url>`).join('\n')
  + '\n</urlset>\n');

fs.writeFileSync('robots.txt', `User-agent: *\nAllow: /\n\nSitemap: ${BASE}sitemap.xml\n`);

console.log(`product pages: ${n}`);
console.log(`location pages: ${STORES.length}`);
console.log(`sitemap urls: ${urls.length}`);
