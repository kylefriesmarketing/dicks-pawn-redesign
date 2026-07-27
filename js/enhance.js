/* Progressive visual enhancements. Everything here is additive — with JS off,
   or reduced motion on, the page is fully readable and nothing is hidden. */
(function () {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- hero: real inventory instead of a decorative badge ---- */
  function heroDeals() {
    const el = document.getElementById('hero-deals');
    if (!el || typeof CATALOG === 'undefined') return;
    const money = n => '$' + n.toLocaleString('en-US', { maximumFractionDigits: 0 });
    // Two cards only. Three fitted the box but buried each other's prices, and
    // an illegible price defeats the point of showing real stock.
    const wanted = ['jewelry', 'games'];
    const picks = [];
    for (const c of wanted) {
      const hit = CATALOG.find(p => p.a && p.c === c && p.p >= 120 && !picks.includes(p));
      if (hit) picks.push(hit);
    }
    while (picks.length < 2) {
      const f = CATALOG.find(p => p.a && p.p >= 120 && !picks.includes(p));
      if (!f) break;
      picks.push(f);
    }
    el.innerHTML = picks.map(p =>
      '<a class="hero-deal" href="p/' + encodeURIComponent(p.h) + '.html">'
      // Above the fold — eager, or the cards render as empty boxes on load.
      + '<div class="hd-img"><img src="' + p.i + '" alt=""></div>'
      + '<div class="hd-body"><div class="hd-title">' + p.t.replace(/[<>&"]/g, '') + '</div>'
      + '<div class="hd-price">' + money(p.p) + '</div></div></a>').join('');
    // Opt into the entry animation only now that the cards exist and JS is
    // demonstrably running. The CSS keeps them visible without this class.
    if (!reduced) {
      el.classList.add('is-anim');
      // The animation uses `backwards` fill, which holds the from-state (opacity 0)
      // until it starts. Strip the class once it has had time to finish so the
      // resting state is plain CSS — the cards can never be left invisible by an
      // animation that was throttled or never ran.
      setTimeout(() => el.classList.remove('is-anim'), 1400);
    }
  }

  /* ---- scroll reveal ---- */
  function reveals() {
    if (reduced || !('IntersectionObserver' in window)) return;
    const targets = document.querySelectorAll(
      '.actions-grid, .cat-grid, .steps-grid, .p-grid, .why .wrap > *, .brands-grid, .rev-grid, .loc-grid, .svc, .band-stats, .faq, .form-card');
    if (!targets.length) return;
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.04 });
    targets.forEach((t, i) => {
      t.classList.add('reveal');
      t.style.transitionDelay = Math.min(i, 3) * 60 + 'ms';
      io.observe(t);
    });

    /* Watchdog. .reveal starts at opacity 0, so anything the observer fails to
       report — a document that never composites, a hidden tab restored oddly,
       a browser quirk — would be stranded invisible. Content must never depend
       on an effect firing, so force everything visible shortly after load. */
    const failSafe = () => targets.forEach(t => t.classList.add('in'));
    setTimeout(failSafe, 2500);
    addEventListener('pageshow', failSafe);
    document.addEventListener('visibilitychange', () => { if (!document.hidden) setTimeout(failSafe, 400); });
  }

  /* ---- header condenses once you scroll past the hero ---- */
  function header() {
    const h = document.querySelector('header.site');
    if (!h) return;
    let last = null;
    const on = () => {
      const s = window.scrollY > 24;
      if (s !== last) { h.classList.toggle('is-stuck', s); last = s; }
    };
    on();
    addEventListener('scroll', on, { passive: true });
  }

  function init() { heroDeals(); reveals(); header(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
