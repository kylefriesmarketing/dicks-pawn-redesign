/* Dick's Pawn — catalog browser. CATALOG comes from js/products.js */
(function () {
  const CATS = {
    all:      'All Items',
    jewelry:  'Jewelry & Gold',
    elec:     'Electronics',
    games:    'Video Games',
    music:    'Musical Instruments',
    tools:    'Tools & Hardware',
    sport:    'Sporting Goods & Golf',
    shoes:    'Sneakers',
    designer: 'Designer & Handbags',
    other:    'More Finds'
  };
  const NEW_DAYS = 21 * 86400000; // "New" badge window
  const BATCH = 48;
  const fmt = n => '$' + n.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  function cardHTML(p) {
    const isNew = Date.now() - p.d < NEW_DAYS;
    const badge = !p.a ? '<span class="p-badge sold">Sold Out</span>'
      : p.cp ? '<span class="p-badge deal">Deal</span>'
      : isNew ? '<span class="p-badge new">New</span>' : '';
    const was = p.cp ? '<s>' + fmt(p.cp) + '</s>' : '';
    return '<div class="p-card' + (p.a ? '' : ' is-sold') + '">'
      + '<div class="p-img">' + badge + '<img loading="lazy" src="' + p.i + '" alt="' + p.t.replace(/"/g, '&quot;') + '"></div>'
      + '<div class="p-body">'
      + '<div class="p-title">' + p.t + '</div>'
      + '<div class="p-price">' + fmt(p.p) + was + '</div>'
      + '<a class="p-cta" href="https://dickspawn.com/products/' + p.h + '" target="_blank" rel="noopener">'
      + (p.a ? 'View Item <span class="arrow">→</span>' : 'Sold Out') + '</a>'
      + '</div></div>';
  }

  /* Render a fixed strip of products into a container (used on the homepage). */
  window.renderStrip = function (elId, opts) {
    const el = document.getElementById(elId);
    if (!el || typeof CATALOG === 'undefined') return;
    let items = CATALOG.filter(p => p.a);
    if (opts && opts.cat) items = items.filter(p => p.c === opts.cat);
    if (opts && opts.deals) items = items.filter(p => p.cp);
    items = items.slice(0, (opts && opts.n) || 8);
    el.innerHTML = items.map(cardHTML).join('');
  };

  /* Render a mixed spread — n items from each named category. */
  window.renderMix = function (elId, cats, perCat) {
    const el = document.getElementById(elId);
    if (!el || typeof CATALOG === 'undefined') return;
    let picks = [];
    cats.forEach(c => {
      picks = picks.concat(CATALOG.filter(p => p.a && p.c === c).slice(0, perCat || 2));
    });
    el.innerHTML = picks.map(cardHTML).join('');
  };

  /* Full shop page */
  window.initShop = function () {
    const grid = document.getElementById('p-grid');
    if (!grid) return;
    const state = { cat: 'all', q: '', sort: 'new', stock: true, shown: BATCH };
    const params = new URLSearchParams(location.search);
    if (params.get('cat') && CATS[params.get('cat')]) state.cat = params.get('cat');
    if (params.get('q')) state.q = params.get('q');

    // Build pills with counts
    const counts = { all: CATALOG.length };
    CATALOG.forEach(p => counts[p.c] = (counts[p.c] || 0) + 1);
    const pills = document.getElementById('pills');
    pills.innerHTML = Object.keys(CATS)
      .filter(k => k === 'all' || counts[k])
      .map(k => '<button class="pill" data-cat="' + k + '">' + CATS[k] + ' <small>' + (counts[k] || 0) + '</small></button>')
      .join('');
    pills.addEventListener('click', e => {
      const b = e.target.closest('.pill');
      if (!b) return;
      state.cat = b.dataset.cat; state.shown = BATCH;
      history.replaceState(null, '', state.cat === 'all' ? location.pathname : '?cat=' + state.cat);
      render();
    });

    const q = document.getElementById('q');
    q.value = state.q;
    q.addEventListener('input', () => { state.q = q.value; state.shown = BATCH; render(); });
    const sort = document.getElementById('sort');
    sort.addEventListener('change', () => { state.sort = sort.value; render(); });
    const stock = document.getElementById('stock');
    stock.checked = state.stock;
    stock.addEventListener('change', () => { state.stock = stock.checked; state.shown = BATCH; render(); });
    document.getElementById('load-more').addEventListener('click', () => { state.shown += BATCH; render(); });

    function filtered() {
      const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
      let items = CATALOG.filter(p =>
        (state.cat === 'all' || p.c === state.cat) &&
        (!state.stock || p.a) &&
        (!terms.length || terms.every(t => p.t.toLowerCase().includes(t)))
      );
      if (state.sort === 'lo') items = items.slice().sort((a, b) => a.p - b.p);
      else if (state.sort === 'hi') items = items.slice().sort((a, b) => b.p - a.p);
      // 'new' keeps catalog order (already newest-first)
      return items;
    }

    function render() {
      document.querySelectorAll('#pills .pill').forEach(b => b.classList.toggle('on', b.dataset.cat === state.cat));
      const items = filtered();
      const slice = items.slice(0, state.shown);
      grid.innerHTML = slice.length ? slice.map(cardHTML).join('')
        : '<div class="empty-msg" style="grid-column:1/-1">No items match — try a different search, or call us at (843) 646-7166. New items arrive daily!</div>';
      document.getElementById('p-count').textContent =
        'Showing ' + slice.length + ' of ' + items.length + ' items' +
        (state.cat !== 'all' ? ' in ' + CATS[state.cat] : '') +
        ' — snapshot of our live inventory; visit dickspawn.com or stop in for today’s floor.';
      document.getElementById('load-wrap').style.display = state.shown < items.length ? '' : 'none';
    }
    render();
  };
})();
