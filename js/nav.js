/* Mobile navigation.
   The desktop <nav class="main"> is hidden under 980px, so phones had no way to
   reach Shop / Sell / Locations. This builds a slide-in panel from that same nav
   at runtime — one source of truth, so every page stays in sync automatically. */
(function () {
  function build() {
    const header = document.querySelector('header.site .wrap');
    const nav = document.querySelector('nav.main');
    if (!header || !nav || document.querySelector('.nav-toggle')) return;

    const toggle = document.createElement('button');
    toggle.className = 'nav-toggle';
    toggle.type = 'button';
    toggle.setAttribute('aria-label', 'Open menu');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', 'nav-panel');
    toggle.innerHTML = '<span></span><span></span><span></span>';

    const backdrop = document.createElement('div');
    backdrop.className = 'nav-back';

    const panel = document.createElement('div');
    panel.className = 'nav-panel';
    panel.id = 'nav-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-modal', 'true');
    panel.setAttribute('aria-label', 'Site menu');

    const links = [...nav.querySelectorAll('a')]
      .map(a => '<a href="' + a.getAttribute('href') + '"'
        + (a.classList.contains('active') ? ' class="on" aria-current="page"' : '') + '>'
        + a.innerHTML + '</a>').join('');

    /* Generated pages live one level down (/p/, /locations/), so a hardcoded
       "sell.html" would 404 there. Derive the prefix from the page's own nav
       link instead of assuming we're at the root. */
    const home = nav.querySelector('a[href$="index.html"]');
    const prefix = home ? home.getAttribute('href').replace(/index\.html$/, '') : '';

    panel.innerHTML =
      '<div class="nav-panel-head">'
      + '<span class="nav-panel-title">Menu</span>'
      + '<button class="nav-close" type="button" aria-label="Close menu">&times;</button>'
      + '</div>'
      + '<nav class="nav-links">' + links + '</nav>'
      + '<div class="nav-panel-foot">'
      + '<a class="btn btn-red" href="' + prefix + 'sell.html">💰 Get Cash Today</a>'
      + '<a class="btn btn-outline" href="tel:8436467166">📞 (843) 646-7166</a>'
      + '<p class="nav-hours">Open Mon–Sat 9am–6pm · 5 Grand Strand locations</p>'
      + '</div>';

    header.appendChild(toggle);
    document.body.appendChild(backdrop);
    document.body.appendChild(panel);

    let lastFocus = null;

    function open() {
      lastFocus = document.activeElement;
      panel.classList.add('open');
      backdrop.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      panel.querySelector('.nav-close').focus();
      document.addEventListener('keydown', onKey);
    }
    function close() {
      panel.classList.remove('open');
      backdrop.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      document.removeEventListener('keydown', onKey);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    function onKey(e) {
      if (e.key === 'Escape') { close(); return; }
      if (e.key !== 'Tab') return;
      // Keep focus inside the panel while it is open.
      const f = panel.querySelectorAll('a[href], button');
      if (!f.length) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }

    toggle.addEventListener('click', open);
    backdrop.addEventListener('click', close);
    panel.querySelector('.nav-close').addEventListener('click', close);
    panel.querySelectorAll('.nav-links a').forEach(a => a.addEventListener('click', close));
    // If the viewport grows back to desktop, drop the panel state.
    window.addEventListener('resize', () => { if (window.innerWidth > 980 && panel.classList.contains('open')) close(); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
