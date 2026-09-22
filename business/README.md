# Business documents

## `dicks-pawn-proposal-and-agreement.pdf`

Three pages, for Jill at Dick's Pawn Superstore.

- **Page 1 — proposal.** Two plans side by side, where the money goes, and what
  is and is not being promised.
- **Pages 2–3 — agreement.** Nine plain-language clauses, a plan tick-box and
  the signature block.

### Four a month is a floor, not the offer

Two things the proposal has to carry, because without them $5,000 for four
videos looks like bad arithmetic:

- **The videos are not the whole job.** They are posted and managed across
  Instagram, Facebook and TikTok, and performance feeds back into what gets
  made next. That is in clause 1 as a deliverable and in the "More than four
  videos" section on page 1.
- **Four a month is a starting point.** The goal is two, three, even four a
  week once the pipeline is running.

**The ramp is written as intent, never as a commitment.** Page 1 says "the
goal is"; clause 1 says any higher number, and any price change with it, gets
agreed in writing first, and that "neither of us owes the other a higher number
until then." That sentence is the whole point — it lets Kyle sell the ambition
without her being able to hold him to four a week later. Do not soften it into
a promise.

### The plan table shows differences only

Rows are Price, Best for, How it is made, On camera, Your time. Nothing that is
true of both plans belongs in it — SEO, posting and the four-a-month target are
all stated in the lead sentence directly above, and an "Also included" row
repeating them was removed.

**Describe the tiers by purpose, never by quality.** An earlier draft said
"professionally shot" and "professional talent" in the $10,000 column and
"quick in-store filming" with "your staff" in the $5,000 one. That does not
anchor — it tells a cautious owner the thing she can afford is the lesser
version, and she stops reading the table as a choice. Both columns now describe
method and fit, and the judgement words are gone.

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

### Where the money goes

Page 1 lists what the fee covers — filmer and producer, a dedicated editor, the
AI production platform and its render time, editing and design software,
scheduling and analytics tools, the SEO work, posting and tracking — and says a
good share is spent before anything reaches her channels.

**No figure is attached to any line, deliberately.** An earlier draft named
$2,000 as the editor's share. Publishing one input cost invites the arithmetic
("so what is the other $3,000 for?") and anchors the conversation to costs
rather than the result. Listing the inputs without pricing them makes the same
point — real money goes out — without handing over a number to negotiate
against. Do not put figures back on individual lines.

The wording is "a good share," not "all" or "most," because only the first is
verifiable.

### What clause 9 can and cannot do

Clause 9 makes payments non-refundable, rules out credits, part-refunds,
discounts and make-good work, caps total liability at the fees paid for the
month in question, and excludes indirect losses. The key sentence is that the
fee **reserves capacity in the schedule and is earned when the month begins** —
that is what makes non-refundability defensible, because the thing being bought
is availability rather than a fixed number of items.

Four further bars were added because they block the routes money actually
leaves by, which a lawsuit rarely is:

- **Notice and cure.** She must raise a problem in writing and allow 15 days to
  fix it before any claim. Most disputes die here, which is the point.
- **No chargebacks.** She agrees not to dispute or charge back a payment with
  her bank or card issuer. A chargeback is far more likely than litigation over
  a sum this size, and is the one route a no-refund clause alone does not touch.
- **Six-month claims window** from the month a claim relates to.
- **Acknowledgement and severability** in clause 10 — she confirms she read it
  and relies on nothing outside it, and a court striking one clause leaves the
  rest standing.

**It does not cover doing nothing at all.** A no-refund clause protects against
a client being unhappy with work that was delivered. Courts generally treat
total non-performance as a failure of consideration and will not enforce
"non-refundable" over the top of it, whatever the contract says. The practical
protection against that scenario is clause 3's commitment to say so before the
month ends and let her decide whether to continue — which is exactly why that
sentence should not be cut.

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

---

## `dicks-pawn-per-video-proposal.pdf`

Three pages, same client, a different shape of deal: **$300 a finished video,
minimum order of ten, production only.** Built by
`make-per-video-proposal.py`. It stands alone — it is not a third tier bolted
onto the monthly proposal, and the two are meant to be sent separately.

- **Page 1 — proposal.** The price band, what $300 buys, what it explicitly
  does not, and the deposit promise.
- **Pages 2–3 — agreement.** Ten clauses, an order line to fill in, signatures.

### Why the terms are the opposite of the monthly agreement's

The monthly agreement says payments are never refundable, because the fee
reserves capacity rather than buying a fixed number of items. This one says the
deposit balance comes straight back, because here the count *is* the deal.

That is not an inconsistency to tidy up. They are different products and the
protection has to sit in a different place:

| | Monthly | Per video |
|---|---|---|
| What is sold | Capacity for a month | A fixed number of videos |
| Deliverable count | Explicitly not guaranteed (clause 3) | Explicitly guaranteed (clause 6) |
| Refunds | None, ever | Undelivered balance returned in 14 days |
| Where the risk sits | Volume disputes | Scope disputes |

**This structure removes the non-performance exposure entirely.** Under the
monthly agreement, a month where nothing ships is money held for no work, and
no clause survives that. Here, money is only earned per delivered file, so the
scenario cannot arise. It is the stronger position of the two, by a distance.

### The three clauses doing the real work

Per-unit pricing lives or dies on definitions, so:

- **Clause 1 defines a video** — up to 60 seconds, vertical, captioned, idea
  through graphics, delivered as an MP4. Without a ceiling, $300 buys a
  three-minute documentary.
- **Clause 4 caps revisions at one round**, and draws the line: changes to
  script, captions, graphics, music, pace and cut are free; *starting again* —
  new topic, new script, re-generated footage — is a new video at $300. Without
  that sentence, one dissatisfied client makes $300 unbounded.
- **Clause 5 puts a date on delivery** (21 days for the first ten) and gives
  her a clean exit if it slips by 14 days. Open-ended delivery is what turns a
  per-unit deal sour.

### Numbers to re-check before this goes out

Both are placeholders set to sensible defaults, not measured facts:

- **21 days for the first ten.** Set from the EP01 build, which took one
  episode. Ten is not ten times one, but it is not one either — confirm against
  real throughput before signing anything.
- **Blocks of ten above the minimum.** Keeps ordering tidy; nothing depends on it.

Also worth pricing properly: at ten videos the order is $3,000, against $5,000
a month for four plus posting, SEO and analytics. Per video that is $300
against roughly $1,250. Whether that clears cost depends on the editor
arrangement and the per-episode render spend, neither of which is recorded
here.

### Chrome is duplicated on purpose

`make-per-video-proposal.py` carries its own copy of the fonts, letterhead,
styles and the `box`/`rule`/`bullets` helpers rather than importing them from
`make-proposal.py`. Importing would re-run and re-date that document, which is
already with the client.

**If a third document appears, extract `business/letterhead.py` first.** Two
copies is tolerable; three is a drift problem.

### Layout traps, again

Both documents hit the same two:

- Page 1 overflowed by exactly one line on the first build and pushed a
  near-empty page 2 into the file. Always check the page count after editing
  page 1 — a 4-page file where 3 was intended is the tell.
- **Last-ink measurement reads the footer, not the body.** Any script checking
  free space has to exclude the bottom ~0.55in or every page reports the same
  number. The check in this repo's verification pass does.
