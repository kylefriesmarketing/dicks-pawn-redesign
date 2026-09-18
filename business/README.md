# Business documents

## `dicks-pawn-proposal-and-agreement.pdf`

Two pages, for Jill at Dick's Pawn Superstore.

- **Page 1 — proposal.** What she gets, what it costs, and the no-lock-in promise.
- **Page 2 — agreement.** Eight plain-language clauses and the signature block.

$5,000 per month, month-to-month, cancel any time by email. No minimum term,
no notice period, no cancellation fee.

### Before sending — two placeholders to fill

Page 1 ends with **[ your phone ]** and **[ your email ]**. Set them in
`make-proposal.py` and rebuild, or fill them in a PDF editor.

There is deliberately no website on the letterhead. `kylefriesmarketing.com`
was inferred from the GitHub handle and never verified, and a made-up address
on a contract is worse than none.

### Rebuilding

```bash
pip install reportlab
python3 business/make-proposal.py
```

It writes straight over the PDF. Everything is in one file: the clause text is
the `CL` list, the price appears in three places (the opening line, "What it
costs", and clause 2), and the date is generated at build time.

### Why it is exactly two pages

Both pages are near-full: 0.95in of slack on page 1 and 0.61in on page 2.
Adding a couple of sentences anywhere will push the signature block onto a
third page on its own, which looks like an afterthought. If you add something,
cut something, or re-check the page count before sending.

Reportlab over-estimates the height of a table whose cells contain lists of
flowables, which is enough on its own to bump the signature block to a new
page. It is built as a plain grid with explicit `rowHeights` for that reason —
don't refactor it back into nested flowables.

### Not legal advice

This is a plain-language business agreement, not a lawyer-drafted contract. At
$60k a year it is worth an attorney's eye before it becomes the template for
other clients, particularly clause 8 (governing law) and clause 5 (IP transfer).
