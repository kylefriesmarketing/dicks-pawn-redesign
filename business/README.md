# Business documents

## `dicks-pawn-proposal-and-agreement.pdf`

Two pages, for Jill at Dick's Pawn Superstore.

- **Page 1 — proposal.** What she gets, what it costs, and the no-lock-in promise.
- **Page 2 — agreement.** Eight plain-language clauses and the signature block.

$5,000 per month, month-to-month, cancel any time by email. No minimum term,
no notice period, no cancellation fee.

**Fully hands-off.** We write, produce *and post* to her channels. She approves
nothing — no drafts, no emails, no uploading. That is the product, not a
side effect: she asked to pay and not think about it again.

### The facts list is what makes the autonomy safe

Clause 4 gives up the approval gate and replaces it with a one-time
confirmation: a short list of facts we are allowed to state on camera, signed
off once at the start, and nothing goes on screen that is not on it.

That list already exists — it is the claim allowlist in
`content/video-series-bible.md`. Get it confirmed by someone at Dick's before
the first video goes up, because with no per-video approval it is the only
thing standing between an unverified claim and a published video about a
regulated business. Clause 4 also gives her a same-day takedown on request,
which is the release valve for anything the list did not anticipate.

### Before sending — two placeholders to fill

Page 1 ends with **[ your phone ]** and **[ your email ]**. Set them in
`make-proposal.py` and rebuild, or fill them in a PDF editor.

There is deliberately no website on the letterhead. `kylefriesmarketing.com`
was inferred from the GitHub handle and never verified, and a made-up address
on a contract is worse than none.

### Also needs sorting before the first invoice

Clause 1 promises posting and clause 6 asks for account access. Decide how the
logins are actually handled — ideally a delegated business account rather than
her personal passwords — and make sure clause 7's "handed back when we stop"
is something you can actually do.

### Rebuilding

```bash
pip install reportlab
python3 business/make-proposal.py
```

It writes straight over the PDF. Everything is in one file: the clause text is
the `CL` list, the price appears in three places (the opening line, "What it
costs", and clause 2), and the date is generated at build time.

### Why it is exactly two pages

Both pages are near-full: 0.30in of slack on page 1 and 0.05in on page 2.
Adding a sentence anywhere will push the signature block onto a third page on
its own, which looks like an afterthought. If you add something, cut something,
and re-check the page count before sending.

Two traps, both already paid for:

- Reportlab over-estimates the height of a table whose cells contain lists of
  flowables, which is enough on its own to bump the signature block to a new
  page. It is built as a plain grid with explicit `rowHeights` for that reason —
  don't refactor it back into nested flowables.
- The source contains literal em dashes. Patching it with `—` in a match
  pattern silently matches nothing and the edit disappears without an error.
  Assert on every replacement.

### Not legal advice

This is a plain-language business agreement, not a lawyer-drafted contract. At
$60k a year it is worth an attorney's eye before it becomes the template for
other clients — particularly clause 4 (publishing without client review),
clause 5 (IP transfer) and clause 8 (governing law).
