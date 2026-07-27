/* Replace emoji UI iconography with inline SVG across the static pages.
 *
 * Inlined at build time rather than swapped by JS at runtime so the icons are
 * present in the served HTML — no flash of missing glyphs, no JS dependency,
 * and crawlers/readers see the same markup users do.
 *
 * Idempotent: pages already converted are skipped.
 *
 *   node tools-icons.mjs
 */
import fs from 'fs';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { icon } = require('./js/icons.js');

const VS = '\\uFE0F?';          // emoji variation selector, often invisible in source
const stars = n => Array.from({ length: n }, () => icon('star')).join('');

/* Ordered: earlier rules win, so longer/context-specific patterns come first. */
const RULES = [
  // --- top bar -------------------------------------------------------------
  [new RegExp(`<span class="star">★</span>`, 'g'),               () => icon('star', 'ic-star')],
  [new RegExp(`📍${VS} <b>5 Locations</b>`, 'g'),                 () => icon('pin') + ' <b>5 Locations</b>'],
  [new RegExp(`🕘${VS} Mon–Sat 9am–6pm`, 'g'),                    () => icon('clock') + ' Mon–Sat 9am–6pm'],
  [new RegExp(`🕘${VS} Open `, 'g'),                              () => icon('clock') + ' Open '],
  [new RegExp(`📞${VS} \\(843\\) 646-7166`, 'g'),                 () => icon('phone') + ' (843) 646-7166'],

  // --- buttons / CTAs ------------------------------------------------------
  [new RegExp(`🛍${VS} Shop`, 'g'),                               () => icon('bag') + ' Shop'],
  [new RegExp(`🛍${VS} Preview`, 'g'),                            () => icon('bag') + ' Preview'],
  [new RegExp(`💰${VS} `, 'g'),                                   () => icon('cash') + ' '],
  [new RegExp(`📞${VS} `, 'g'),                                   () => icon('phone') + ' '],
  [new RegExp(`📍${VS} `, 'g'),                                   () => icon('pin') + ' '],
  [new RegExp(`🔍${VS} `, 'g'),                                   () => icon('search', 'ic-search') + ' '],
  [new RegExp(`🏆${VS} `, 'g'),                                   () => icon('trophy') + ' '],
  [new RegExp(`🎯${VS} `, 'g'),                                   () => icon('tag') + ' '],

  // --- five-star review rows ----------------------------------------------
  [/<div class="stars">★★★★★<\/div>/g,                            () => `<div class="stars">${stars(5)}</div>`],
  [/<div class="stars">★★★★★<\/div>/g,                            () => `<div class="stars">${stars(5)}</div>`],

  // --- inline ticks --------------------------------------------------------
  [/<span class="tick">✔<\/span>/g,                               () => `<span class="tick">${icon('check')}</span>`],
  [/✔ /g,                                                         () => icon('check', 'ic-tick') + ' '],

  // --- "why us" list dots --------------------------------------------------
  [new RegExp(`<div class="dot">💎${VS}</div>`, 'g'),             () => `<div class="dot">${icon('gem')}</div>`],
  [new RegExp(`<div class="dot">🛡${VS}</div>`, 'g'),             () => `<div class="dot">${icon('shield')}</div>`],
  [new RegExp(`<div class="dot">📦${VS}</div>`, 'g'),             () => `<div class="dot">${icon('box')}</div>`],
  [new RegExp(`<div class="dot">🪙${VS}</div>`, 'g'),             () => `<div class="dot">${icon('coin')}</div>`],

  // --- about page credential blocks ---------------------------------------
  [new RegExp(`<div class="step-num">🛡${VS}</div>`, 'g'),        () => `<div class="step-num is-ic">${icon('shield')}</div>`],
  [new RegExp(`<div class="step-num">🤝${VS}</div>`, 'g'),        () => `<div class="step-num is-ic">${icon('users')}</div>`],
  [new RegExp(`<div class="step-num">⚖${VS}</div>`, 'g'),         () => `<div class="step-num is-ic">${icon('scale')}</div>`],
  [new RegExp(`<div class="step-num">💰${VS}</div>`, 'g'),        () => `<div class="step-num is-ic">${icon('cash')}</div>`],
  [new RegExp(`<div class="step-num">💎${VS}</div>`, 'g'),        () => `<div class="step-num is-ic">${icon('gem')}</div>`],
  [new RegExp(`<div class="step-num">🛍${VS}</div>`, 'g'),        () => `<div class="step-num is-ic">${icon('bag')}</div>`],

  // --- location cards ------------------------------------------------------
  [new RegExp(`<div class="pin">📍${VS}</div>`, 'g'),             () => `<div class="pin">${icon('pin')}</div>`],
  [new RegExp(`<div class="pin"([^>]*)>💬${VS}</div>`, 'g'),      (_, a) => `<div class="pin"${a}>${icon('chat')}</div>`],
  [new RegExp(`<h3>📍${VS} `, 'g'),                               () => `<h3><span class="h-ic">${icon('pin')}</span> `],

  // --- category tiles: the real product photo behind these IS the icon now,
  //     so the emoji badge is redundant clutter. Drop it. --------------------
  [/<span class="cat-emoji">[^<]*<\/span>/g,                       () => ''],
];

const FILES = ['index.html', 'shop.html', 'sell.html', 'services.html', 'about.html', 'locations.html'];

let changed = 0;
for (const f of FILES) {
  if (!fs.existsSync(f)) continue;
  let h = fs.readFileSync(f, 'utf8');
  const before = h;
  for (const [re, fn] of RULES) h = h.replace(re, fn);

  // Load the icon helper for anything rendered client-side.
  if (!h.includes('js/icons.js')) {
    h = h.replace(/<script src="js\/shop\.js"><\/script>/, '<script src="js/icons.js"></script>\n<script src="js/shop.js"></script>');
  }
  if (h !== before) { fs.writeFileSync(f, h); changed++; console.log('  icons ->', f); }
}

/* Report anything still using emoji as chrome, so nothing silently survives. */
const EMOJI = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}]/gu;
let leftover = 0;
for (const f of FILES) {
  if (!fs.existsSync(f)) continue;
  const body = fs.readFileSync(f, 'utf8');
  const hits = body.match(EMOJI) || [];
  if (hits.length) { console.log(`  ${f}: ${hits.length} emoji remain -> ${[...new Set(hits)].join(' ')}`); leftover += hits.length; }
}
console.log(`\n${changed} files converted; ${leftover} emoji glyphs remain (decorative/body copy).`);
