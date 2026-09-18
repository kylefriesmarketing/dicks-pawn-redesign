# Business documents

## `dicks-pawn-proposal-and-agreement.pdf`

Three pages, for Jill at Dick's Pawn Superstore.

- **Page 1 — proposal.** Two plans side by side, where the money goes, and what
  is and is not being promised.
- **Pages 2–3 — agreement.** Nine plain-language clauses, a plan tick-box and
  the signature block.

### Two plans

| | Standard | Full production |
|---|---|---|
| Price | $5,000 / month | $10,000 / month |
| How | AI host pieces + quick in-store filming | Professionally shot, full crew |
| On camera | Her staff | Professional talent |
| Her time | ~half a day a month | None |

Both are month-to-month, cancel any time by email, and both include SEO and
posting to her channels.

### The two things this document is careful about

**Nothing is guaranteed — not results, and not the deliverables.** Clause 3
covers both, and page 1 says the same in Kyle's voice. Results are an informed
expectation from research, past work and experience. The count is a target:
four a month, depending on the time and resources available that month,
including her staff, a location to film in and account access.

That leaves the document with no hard promise about output, which is a real
cost — so the one commitment that remains is a communication one: **we tell you
before the month ends, not after**. Without that line the whole page reads as
"we promise nothing." Do not delete it while trimming for space.

**There is no money remedy anywhere in this document, by design.** Clause 3
states that payments are not refundable and that no credits or make-good work
are issued for a short month; the client's sole remedy is to stop, which
clause 4 lets her do any time. Two earlier lines created payment consequences
and were removed: "you are not invoiced for a month whose work is not
delivered", and clause 4's "hand over everything you have paid for" (which
implied entitlement to a count) — now "everything we have made for you".

If you edit this file, do not reintroduce any phrasing that ties payment to
delivery. That was a deliberate client decision, not an oversight.

The one specific operational promise left is clause 5's same-day takedown. It
is not a payment trigger, and it is doing real work for trust — but it is a
commitment, so it is there on purpose.

"Four a month" is written as a *target* in all four places it appears — the
opening line, the plan table, clause 1 and clause 3. If you change one, change
all four.

**Her staff are on camera, which is not free for her.** The earlier draft
promised "nothing for you to do." That cannot survive a shoot, so clause 6
names the cost honestly — about half a day a month, at a time she picks, worked
around opening hours — and adds the escape hatch: a month she cannot spare the
time still gets its videos, made without filming, at the same price. The AI
pipeline is what makes that promise keepable.

Approvals are still gone. Clause 5 keeps the one-time facts list that makes
publishing without review safe; that list is the claim allowlist already in
`content/video-series-bible.md`. Get it confirmed before the first video goes
up.

### The $2,000 editor line

Page 1 states that $2,000 of the $5,000 goes to the editor. This was a
deliberate client decision, made after the trade-off was raised: it shows the
money going into real production, at the cost of anchoring the conversation to
input costs rather than results. The surrounding sentence is written to frame
the remainder as covered work — AI production, SEO, posting, tools — rather
than margin.

### Before sending

- **No website, on purpose.** Kyle Fries Marketing does not have one. The
  letterhead carries the email and phone and nothing else. Do not add a domain
  here — an address that does not resolve is worse on a contract than none, and
  `kylefriesmarketing.com` in particular was only ever an inference from the
  GitHub handle.

  The one "website" in the document is in clause 1: the SEO work covers *Dick's
  Pawn's* site. That is correct and stays.
- **Sort out account access.** Clause 1 promises posting and clause 6 asks for
  logins. Use delegated business accounts, not her personal passwords, so
  clause 9's "handed back when we stop" is something you can actually do.

### Rebuilding

```bash
pip install reportlab
python3 business/make-proposal.py
```

Everything is in one file: the plan table is `ROWS`, the clause text is `CL`,
and the date is generated at build time.

### Layout notes, all of them paid for the hard way

Page slack: 0.10in on page 1, 2.26in on page 2, 5.87in on page 3. Re-check the
page count after any edit.

- **The clause break after clause 6 is deliberate.** Left to flow, all nine
  clauses land on page 2 and the signature block is stranded alone on page 3.
- **Reportlab over-estimates a table whose cells hold lists of flowables**,
  which alone is enough to bump the signature block to a new page. It is a
  plain grid with explicit `rowHeights` for that reason — don't refactor it
  back into nested flowables.
- **Table padding is expensive.** The plan table's vertical padding was costing
  1.36in at 7pt; it is 5pt now.
- **The source contains literal em dashes.** Patching it with `—` in a
  match pattern silently matches nothing and the edit vanishes with no error.
  Assert on every replacement.

### Not legal advice

This is a plain-language business agreement, not a lawyer-drafted contract. At
$60k–$120k a year it is worth an attorney's eye before it becomes the template
for other clients — particularly clause 3 (the guarantee wording), clause 5
(publishing without client review), clause 7 (IP transfer) and clause 9
(governing law).
