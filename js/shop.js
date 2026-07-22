/* Dick's Pawn — catalog browser + quick view.
   CATALOG comes from js/products.js; richer per-product detail (gallery,
   description) lives in js/details.json and is fetched only when a quick
   view is first opened, so the grid stays fast. */
(function () {
  const CATS = {
    all:      'All Items',
    jewelry:  'Jewelry & Gold',
    elec:     'Electronics',
    games:    'Video Games',
    music:    'Musical Instruments',
    tools:    'Tools & Hardware',
    sport:    'Sporting Goods & Golf',
    designer: 'Designer & Handbags',
    shoes:    'Sneakers',
    collect:  'Collectibles',
    other:    'More Finds'
  };
  const SUBS = {
    ring: 'Rings', necklace: 'Necklaces', pendant: 'Pendants & Charms',
    bracelet: 'Bracelets', earring: 'Earrings', watch: 'Watches', other: 'Other'
  };
  const NEW_DAYS = 21 * 86400000;
  const BATCH = 48;
  const PRODUCT_URL = 'https://dickspawn.com/products/';   // their live Shopify checkout
  const PAGE_URL = 'p/';                                    // our own indexable product page

  const fmt = n => '$' + n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  /* ---------- product card ---------- */
  function cardHTML(p, i) {
    const isNew = Date.now() - p.d < NEW_DAYS;
    const badge = !p.a ? '<span class="p-badge sold">Sold Out</span>'
      : p.cp ? '<span class="p-badge deal">Deal</span>'
      : isNew ? '<span class="p-badge new">New</span>' : '';
    const was = p.cp ? '<s>' + fmt(p.cp) + '</s>' : '';
    // The title is a real link to the product's own page — that's what makes the
    // 1,565 generated pages crawlable, and lets people open items in a new tab.
    const href = PAGE_URL + encodeURIComponent(p.h) + '.html';
    return '<div class="p-card' + (p.a ? '' : ' is-sold') + '" data-h="' + esc(p.h) + '">'
      + '<a class="p-img" href="' + href + '">' + badge
      + '<img loading="lazy" src="' + esc(p.i) + '" alt="' + esc(p.t) + '"></a>'
      + '<div class="p-body">'
      + '<a class="p-title" href="' + href + '">' + esc(p.t) + '</a>'
      + '<div class="p-price">' + fmt(p.p) + was + '</div>'
      + '<button class="p-cta" type="button" data-qv="' + esc(p.h) + '">'
      + (p.a ? 'Quick View <span class="arrow">→</span>' : 'Sold Out') + '</button>'
      + '</div></div>';
  }

  const byHandle = {};
  function indexCatalog() {
    if (typeof CATALOG === 'undefined') return;
    CATALOG.forEach(p => byHandle[p.h] = p);
  }

  /* ---------- quick view ---------- */
  let detailCache = null, detailPromise = null, lastFocus = null;

  function loadDetails() {
    if (detailCache) return Promise.resolve(detailCache);
    if (!detailPromise) {
      detailPromise = fetch('js/details.json')
        .then(r => r.ok ? r.json() : {})
        .then(d => (detailCache = d))
        .catch(() => (detailCache = {}));
    }
    return detailPromise;
  }

  function ensureModal() {
    let back = document.getElementById('qv-back');
    if (back) return back;
    back = document.createElement('div');
    back.id = 'qv-back';
    back.className = 'qv-back';
    back.innerHTML = '<div class="qv" role="dialog" aria-modal="true" aria-labelledby="qv-title"></div>';
    document.body.appendChild(back);
    back.addEventListener('click', e => { if (e.target === back) closeQV(); });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && back.classList.contains('open')) closeQV();
    });
    return back;
  }

  function closeQV() {
    const back = document.getElementById('qv-back');
    if (!back) return;
    back.classList.remove('open');
    document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function openQV(handle) {
    const p = byHandle[handle];
    if (!p) return;
    lastFocus = document.activeElement;
    const back = ensureModal();
    const box = back.querySelector('.qv');
    const was = p.cp ? '<s>' + fmt(p.cp) + '</s>' : '';

    // Render immediately from the grid data, then fill in gallery/description.
    box.innerHTML =
      '<div class="qv-media">'
      + '<div class="qv-main"><img id="qv-main-img" src="' + esc(p.i) + '" alt="' + esc(p.t) + '"></div>'
      + '<div class="qv-thumbs" id="qv-thumbs"></div>'
      + '</div>'
      + '<div class="qv-body">'
      + '<button class="qv-close" type="button" aria-label="Close quick view">&times;</button>'
      + '<span class="qv-cat">' + esc(CATS[p.c] || 'Item') + '</span>'
      + '<h3 id="qv-title">' + esc(p.t) + '</h3>'
      + '<div class="qv-price">' + fmt(p.p) + was + '</div>'
      + '<span class="qv-stock ' + (p.a ? 'in' : 'out') + '">' + (p.a ? '✔ In stock now' : 'Sold out') + '</span>'
      + '<p class="qv-desc" id="qv-desc">Loading details…</p>'
      + '<div class="qv-meta" id="qv-meta"></div>'
      + '<div class="qv-ctas">'
      + (p.a
          ? '<a class="btn btn-red" href="' + PRODUCT_URL + esc(p.h) + '" target="_blank" rel="noopener">Buy Online <span class="arrow">→</span></a>'
            + '<a class="btn btn-outline" href="tel:8436467166">📞 Call to Hold</a>'
          : '<a class="btn btn-outline" href="tel:8436467166">📞 Ask About Similar</a>')
      + '</div>'
      + '<a class="qv-full" href="' + PAGE_URL + encodeURIComponent(p.h) + '.html">See full details &amp; similar items <span class="arrow">→</span></a>'
      + '</div>';

    box.querySelector('.qv-close').addEventListener('click', closeQV);
    back.classList.add('open');
    document.body.style.overflow = 'hidden';
    box.querySelector('.qv-close').focus();

    loadDetails().then(all => {
      if (!back.classList.contains('open')) return;
      const d = all[handle];
      const desc = document.getElementById('qv-desc');
      if (!desc) return;
      desc.textContent = (d && d.b) ? d.b : 'Visit us in store or online for full details on this item.';
      const meta = document.getElementById('qv-meta');
      if (meta && d) {
        const bits = [];
        if (d.v) bits.push('Sold by ' + d.v);
        if (d.sku) bits.push('SKU ' + d.sku);
        meta.textContent = bits.join(' · ');
      }
      const thumbs = document.getElementById('qv-thumbs');
      const gallery = (d && d.g && d.g.length > 1) ? d.g : null;
      if (thumbs && gallery) {
        thumbs.innerHTML = gallery.map((src, i) =>
          '<button class="qv-thumb' + (i === 0 ? ' on' : '') + '" type="button" data-src="' + esc(src) + '" aria-label="View image ' + (i + 1) + '">'
          + '<img loading="lazy" src="' + esc(src) + '" alt=""></button>').join('');
        const main = document.getElementById('qv-main-img');
        if (main && gallery[0]) main.src = gallery[0];
        thumbs.addEventListener('click', e => {
          const b = e.target.closest('.qv-thumb');
          if (!b) return;
          document.getElementById('qv-main-img').src = b.dataset.src;
          thumbs.querySelectorAll('.qv-thumb').forEach(t => t.classList.toggle('on', t === b));
        });
      }
    });
  }

  /* Delegated so it covers every grid on the page, including lazily rendered ones.
     Only the Quick View button opens the modal — the image and title are real
     links to the product page, so normal click / middle-click / open-in-new-tab
     all behave the way people expect. */
  document.addEventListener('click', e => {
    const btn = e.target.closest('[data-qv]');
    if (btn) { e.preventDefault(); openQV(btn.dataset.qv); }
  });

  /* ---------- homepage strips ---------- */
  window.renderStrip = function (elId, opts) {
    const el = document.getElementById(elId);
    if (!el || typeof CATALOG === 'undefined') return;
    indexCatalog();
    let items = CATALOG.filter(p => p.a);
    if (opts && opts.cat) items = items.filter(p => p.c === opts.cat);
    if (opts && opts.deals) items = items.filter(p => p.cp);
    el.innerHTML = items.slice(0, (opts && opts.n) || 8).map(cardHTML).join('');
  };

  window.renderMix = function (elId, cats, perCat) {
    const el = document.getElementById(elId);
    if (!el || typeof CATALOG === 'undefined') return;
    indexCatalog();
    let picks = [];
    cats.forEach(c => { picks = picks.concat(CATALOG.filter(p => p.a && p.c === c).slice(0, perCat || 2)); });
    el.innerHTML = picks.map(cardHTML).join('');
  };

  /* Paint each category tile with a real product photo from that category. */
  window.paintCategoryTiles = function () {
    if (typeof CATALOG === 'undefined') return;
    document.querySelectorAll('.cat-card[data-cat]').forEach(tile => {
      const cat = tile.dataset.cat;
      const sub = tile.dataset.sub;
      const hit = CATALOG.find(p => p.a && p.c === cat && (!sub || p.s === sub));
      if (hit) tile.style.backgroundImage = 'url("' + hit.i + '")';
    });
  };

  /* ---------- full shop page ---------- */
  window.initShop = function () {
    const grid = document.getElementById('p-grid');
    if (!grid || typeof CATALOG === 'undefined') return;
    indexCatalog();

    const state = { cat: 'all', sub: '', q: '', sort: 'new', stock: true, shown: BATCH };
    const params = new URLSearchParams(location.search);
    if (params.get('cat') && CATS[params.get('cat')]) state.cat = params.get('cat');
    if (params.get('sub') && SUBS[params.get('sub')]) state.sub = params.get('sub');
    if (params.get('q')) state.q = params.get('q');

    const pills = document.getElementById('pills');
    const subpills = document.getElementById('subpills');
    const q = document.getElementById('q');
    const sort = document.getElementById('sort');
    const stock = document.getElementById('stock');

    /* Counts must reflect the in-stock toggle, or the pill promises more than the grid shows. */
    function pool() { return state.stock ? CATALOG.filter(p => p.a) : CATALOG; }

    function buildPills() {
      const src = pool();
      const counts = { all: src.length };
      src.forEach(p => counts[p.c] = (counts[p.c] || 0) + 1);
      pills.innerHTML = Object.keys(CATS)
        .filter(k => k === 'all' || counts[k])
        .map(k => '<button class="pill' + (k === state.cat ? ' on' : '') + '" type="button" data-cat="' + k + '"'
          + ' aria-pressed="' + (k === state.cat) + '">' + CATS[k] + ' <small>' + (counts[k] || 0) + '</small></button>')
        .join('');
    }

    function buildSubpills() {
      const src = pool().filter(p => p.c === state.cat);
      const counts = {};
      src.forEach(p => { if (p.s) counts[p.s] = (counts[p.s] || 0) + 1; });
      const keys = Object.keys(SUBS).filter(k => counts[k]);
      if (state.cat === 'all' || keys.length < 2) { subpills.innerHTML = ''; return; }
      subpills.innerHTML = '<button class="subpill' + (state.sub ? '' : ' on') + '" type="button" data-sub="">All ' + CATS[state.cat] + '</button>'
        + keys.map(k => '<button class="subpill' + (k === state.sub ? ' on' : '') + '" type="button" data-sub="' + k + '">'
          + SUBS[k] + ' <small>' + counts[k] + '</small></button>').join('');
    }

    function syncURL() {
      const qs = new URLSearchParams();
      if (state.cat !== 'all') qs.set('cat', state.cat);
      if (state.sub) qs.set('sub', state.sub);
      if (state.q) qs.set('q', state.q);
      const s = qs.toString();
      history.replaceState(null, '', s ? '?' + s : location.pathname);
    }

    pills.addEventListener('click', e => {
      const b = e.target.closest('.pill');
      if (!b) return;
      state.cat = b.dataset.cat;
      state.sub = '';
      state.shown = BATCH;
      syncURL(); render();
    });
    subpills.addEventListener('click', e => {
      const b = e.target.closest('.subpill');
      if (!b) return;
      state.sub = b.dataset.sub || '';
      state.shown = BATCH;
      syncURL(); render();
    });
    q.value = state.q;
    q.addEventListener('input', () => { state.q = q.value; state.shown = BATCH; syncURL(); render(); });
    sort.addEventListener('change', () => { state.sort = sort.value; render(); });
    stock.checked = state.stock;
    stock.addEventListener('change', () => { state.stock = stock.checked; state.shown = BATCH; render(); });
    document.getElementById('load-more').addEventListener('click', () => {
      state.shown += BATCH;
      render({ keepScroll: true });
    });

    function filtered() {
      const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
      let items = pool().filter(p =>
        (state.cat === 'all' || p.c === state.cat) &&
        (!state.sub || p.s === state.sub) &&
        (!terms.length || terms.every(t => p.t.toLowerCase().includes(t)))
      );
      if (state.sort === 'lo') items = items.slice().sort((a, b) => a.p - b.p);
      else if (state.sort === 'hi') items = items.slice().sort((a, b) => b.p - a.p);
      return items;
    }

    function render() {
      buildPills();
      buildSubpills();
      const items = filtered();
      const slice = items.slice(0, state.shown);
      grid.innerHTML = slice.length
        ? slice.map(cardHTML).join('')
        : '<div class="empty-msg" style="grid-column:1/-1">No items match — try a different search, or call us at '
          + '<a href="tel:8436467166" style="color:var(--red);font-weight:700">(843) 646-7166</a>. New items arrive daily!</div>';

      let label = 'Showing ' + slice.length + ' of ' + items.length + ' item' + (items.length === 1 ? '' : 's');
      if (state.sub) label += ' in ' + SUBS[state.sub];
      else if (state.cat !== 'all') label += ' in ' + CATS[state.cat];
      document.getElementById('p-count').innerHTML = label
        + ' <span style="opacity:.75">— a snapshot of our live inventory. New items hit the floor daily.</span>';
      document.getElementById('load-wrap').style.display = state.shown < items.length ? '' : 'none';
    }

    render();
  };
})();
