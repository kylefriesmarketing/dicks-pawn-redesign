import fs from 'fs';
const all = [];
for (let p = 1; p <= 7; p++) JSON.parse(fs.readFileSync(`prod${p}.json`,'utf8')).products.forEach(x=>all.push(x));

const JEW = new Set(['jewelry','gr','gp','gb','ge','gn','ap','an','ar','ab','ae','fw','sh','fh','watch','watches']);
function cat(p) {
  const tags = (p.tags||[]).map(t=>t.toLowerCase());
  const title = p.title.toLowerCase();
  const has = (...ws) => tags.some(t => ws.some(w => t === w || t.startsWith(w)));
  if (has('video games','playstation','nintendo','xbox','retrog','sega') ) return 'games';
  if (has('music','guitar','amp','dj','drum','mgear','keyboard')) return 'music';
  if (has('tools','drill','saw','nail','hw','ot','lg') && !tags.includes('jewelry')) return 'tools';
  if (has('sporting goods','golf','fishing','bike','surf')) return 'sport';
  if (has('shoes','sneaker','jordan','nike')) return 'shoes';
  if (has('handbag','purse','wallet','sunglasses','designer') || /louis vuitton|gucci|dior|chanel|prada|versace|fendi|coach /.test(title)) return 'designer';
  if (has('electronics','car audio','car','speaker','headphone','tv','camera','computer','tablet')) return 'elec';
  if (tags.some(t=>JEW.has(t))) return 'jewelry';
  if (/ring|necklace|bracelet|pendant|earring|chain|diamond|gold|sterling|silver|watch/.test(title)) return 'jewelry';
  return 'other';
}
function sized(src, s) {
  if (!src) return '';
  return src.replace(/(\.(jpg|jpeg|png|webp|gif))(\?|$)/i, `_${s}x$1$3`);
}
const out = [];
for (const p of all) {
  const v = p.variants && p.variants[0];
  if (!v) continue;
  const img = p.images && p.images[0] && p.images[0].src;
  if (!img) continue;
  const price = parseFloat(v.price);
  if (!price || price <= 0) continue;
  const rec = {
    t: p.title.slice(0, 110),
    p: price,
    i: sized(img, 480),
    h: p.handle,
    a: v.available ? 1 : 0,
    c: cat(p),
    d: Date.parse(p.created_at) || 0
  };
  const cp = parseFloat(v.compare_at_price);
  if (cp && cp > price) rec.cp = cp;
  out.push(rec);
}
out.sort((a,b) => b.d - a.d);
const counts = {};
for (const r of out) counts[r.c] = (counts[r.c]||0)+1;
console.log('kept', out.length, JSON.stringify(counts));
fs.writeFileSync('products.js', '// Live catalog snapshot from dickspawn.com (Shopify products.json), generated ' + new Date().toISOString().slice(0,10) + '\nconst CATALOG = ' + JSON.stringify(out) + ';\n');
console.log('bytes', fs.statSync('products.js').size);
