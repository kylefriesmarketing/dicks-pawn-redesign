/* Dick's Pawn — icon set.
 *
 * Emoji were doing the icon work across the site, which renders differently on
 * every OS (Windows/Mac/Android all ship different art) and reads as low-effort
 * on a business site. These are drawn on a single 24x24 grid with a 1.85 stroke
 * so they sit together as one family and inherit currentColor.
 *
 * Consumed two ways:
 *   - build time: tools-icons.mjs inlines them into static HTML (no JS needed
 *     to render, no flash of missing icons)
 *   - run time:   shop.js calls icon() for cards it renders itself
 */
(function (root) {
  const P = {
    phone:   '<path d="M6.6 3h2.9l1.5 3.9-2 1.4a12.2 12.2 0 0 0 5.7 5.7l1.4-2 3.9 1.5v2.9a2 2 0 0 1-2.2 2A16.4 16.4 0 0 1 4.6 5.2 2 2 0 0 1 6.6 3z"/>',
    pin:     '<path d="M12 21.2s6.8-5.6 6.8-10.8a6.8 6.8 0 1 0-13.6 0c0 5.2 6.8 10.8 6.8 10.8z"/><circle cx="12" cy="10.2" r="2.5"/>',
    clock:   '<circle cx="12" cy="12" r="8.8"/><path d="M12 6.9v5.4l3.4 2"/>',
    check:   '<path d="m4.8 12.6 4.8 4.8L19.2 6.9"/>',
    cash:    '<rect x="2.6" y="6" width="18.8" height="12" rx="2.2"/><circle cx="12" cy="12" r="2.6"/><path d="M6.2 10.1h.02M17.8 13.9h.02"/>',
    bag:     '<path d="M5.6 7.8h12.8l1 12.4H4.6z"/><path d="M9 7.8V5.9a3 3 0 0 1 6 0v1.9"/>',
    search:  '<circle cx="10.9" cy="10.9" r="6.6"/><path d="m15.8 15.8 4.5 4.5"/>',
    chat:    '<path d="M20.2 14.9a2 2 0 0 1-2 2H8.4L4 20.4V5.9a2 2 0 0 1 2-2h12.2a2 2 0 0 1 2 2z"/>',
    trophy:  '<path d="M8.2 3.6h7.6v5.2a3.8 3.8 0 0 1-7.6 0z"/><path d="M8.2 5.4H5.6a2.4 2.4 0 0 0 2.6 4.4M15.8 5.4h2.6a2.4 2.4 0 0 1-2.6 4.4"/><path d="M12 12.6v3.8M8.9 20.4h6.2"/>',
    gem:     '<path d="M6 3.4h12l3.7 5.7L12 20.6 2.3 9.1z"/><path d="M2.3 9.1h19.4"/><path d="m9 3.4 3 5.7 3-5.7"/>',
    shield:  '<path d="M12 3.2 5.2 6v5.8c0 4.4 2.9 7.6 6.8 8.9 3.9-1.3 6.8-4.5 6.8-8.9V6z"/><path d="m9.2 11.8 2 2 3.6-3.9"/>',
    box:     '<path d="M3.6 7.6 12 3.2l8.4 4.4v8.8L12 20.8l-8.4-4.4z"/><path d="m3.6 7.6 8.4 4.4 8.4-4.4M12 12v8.8"/>',
    coin:    '<circle cx="12" cy="12" r="8.8"/><path d="M12 6.9v10.2M9.6 9.6c0-1 1.1-1.8 2.4-1.8s2.4.8 2.4 1.8c0 2.6-4.8 1.6-4.8 4.4 0 1 1.1 1.8 2.4 1.8s2.4-.8 2.4-1.8"/>',
    users:   '<circle cx="9.2" cy="8" r="3.2"/><path d="M3.4 20a5.8 5.8 0 0 1 11.6 0"/><path d="M16.2 5.2a3.2 3.2 0 0 1 0 5.9M17.9 20a5.9 5.9 0 0 0-2.4-4.7"/>',
    scale:   '<path d="M12 4.2v15.6M7.6 19.8h8.8M12 6.9 5.4 8.8l-2.6 5.2a3.5 3.5 0 0 0 6.9 0L7.1 8.8M12 6.9l6.6 1.9 2.6 5.2a3.5 3.5 0 0 1-6.9 0l2.6-5.2"/>',
    tag:     '<path d="M11 3.4H3.4V11l9.8 9.8 7.6-7.6z"/><circle cx="7.4" cy="7.4" r="1.5"/>',
    truck:   '<path d="M2.8 6.4h10.4v9.4H2.8z"/><path d="M13.2 9.6h3.6l3.4 3.2v3h-7z"/><circle cx="6.6" cy="18" r="1.9"/><circle cx="17" cy="18" r="1.9"/>',
    sparkle: '<path d="m12 3 1.9 5.4L19.3 10l-5.4 1.9L12 17.3l-1.9-5.4L4.7 10l5.4-1.6z"/><path d="M18.6 15.4l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/>'
  };

  /* Filled marks read better than outlines at small sizes. */
  const FILLED = {
    star: '<path d="m12 2.4 2.94 6.1 6.66.94-4.8 4.7 1.14 6.66L12 17.7l-5.94 3.1 1.14-6.66-4.8-4.7 6.66-.94z"/>'
  };

  function icon(name, cls) {
    const filled = FILLED[name];
    const body = filled || P[name];
    if (!body) return '';
    return '<svg class="ic' + (cls ? ' ' + cls : '') + '" viewBox="0 0 24 24" aria-hidden="true" focusable="false"'
      + (filled ? ' fill="currentColor" stroke="none"' : '') + '>' + body + '</svg>';
  }

  const api = { icon, PATHS: P, FILLED };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.DPIcons = api;
  root.icon = icon;
})(typeof globalThis !== 'undefined' ? globalThis : this);
