from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime, os

L = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("Sans",   L+"LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-B", L+"LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-I", L+"LiberationSans-Italic.ttf"))
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-B", italic="Sans-I")

INK   = colors.HexColor("#15202b")
MUTED = colors.HexColor("#5b6b7c")
ACC   = colors.HexColor("#1b4965")
RULE  = colors.HexColor("#d4dce4")
TINT  = colors.HexColor("#eef3f7")

PW, PH = LETTER
M = 0.85*inch

def S(name, **kw):
    base = dict(fontName="Sans", fontSize=10.2, leading=15.4, textColor=INK,
                spaceAfter=0, spaceBefore=0)
    base.update(kw); return ParagraphStyle(name, **base)

body      = S("body", fontSize=10, leading=14.6, spaceAfter=7)
lead      = S("lead", fontSize=11.2, leading=16.4, spaceAfter=9)
h1        = S("h1", fontName="Sans-B", fontSize=19, leading=23, textColor=INK, spaceAfter=3)
h2        = S("h2", fontName="Sans-B", fontSize=11.8, leading=15, textColor=ACC,
              spaceBefore=12, spaceAfter=5)
kicker    = S("kicker", fontName="Sans-B", fontSize=8.2, leading=11, textColor=MUTED)
sub       = S("sub", fontSize=10.2, leading=14, textColor=MUTED, spaceAfter=2)
bullet    = S("bullet", fontSize=10, leading=14.4, spaceAfter=4,
              leftIndent=15, bulletIndent=2, firstLineIndent=0)
callout   = S("callout", fontSize=10.6, leading=15.6, spaceAfter=0)
calloutH  = S("calloutH", fontName="Sans-B", fontSize=12.2, leading=16, textColor=ACC, spaceAfter=5)
clause    = S("clause", fontSize=9.5, leading=13.2, spaceAfter=4)
clauseH   = S("clauseH", fontName="Sans-B", fontSize=10.2, leading=13, textColor=INK,
              spaceBefore=5, spaceAfter=3)
sigLbl    = S("sigLbl", fontSize=8.4, leading=11, textColor=MUTED)
fine      = S("fine", fontSize=8.6, leading=12.6, textColor=MUTED)
tcell     = S("tcell", fontSize=9.2, leading=12.6)
tcellb    = S("tcellb", fontName="Sans-B", fontSize=9.2, leading=12.6)
thead     = S("thead", fontName="Sans-B", fontSize=10.4, leading=13, textColor=colors.white)
tlabel    = S("tlabel", fontName="Sans-B", fontSize=9.2, leading=12.6, textColor=MUTED)
tprice    = S("tprice", fontName="Sans-B", fontSize=13, leading=16, textColor=INK)

TODAY = datetime.date.today().strftime("%B %-d, %Y")

def header_footer(canvas, doc):
    canvas.saveState()
    # letterhead
    canvas.setFont("Sans-B", 10.6); canvas.setFillColor(INK)
    canvas.drawString(M, PH - M + 26, "KYLE FRIES MARKETING")
    canvas.setFont("Sans", 8.4); canvas.setFillColor(MUTED)
    canvas.drawRightString(PW - M, PH - M + 26,
                           "Kylefriesmarketing@gmail.com \u00b7 806-544-8098")
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.7)
    canvas.line(M, PH - M + 18, PW - M, PH - M + 18)
    # footer
    canvas.setFont("Sans", 8.2); canvas.setFillColor(MUTED)
    canvas.drawString(M, M - 34, "Dick's Pawn Superstore · Video and SEO · %s" % TODAY)
    canvas.drawRightString(PW - M, M - 34, "Page %d" % doc.page)
    canvas.restoreState()

def rule(space_before=4, space_after=10, col=RULE):
    t = Table([[""]], colWidths=[PW - 2*M], rowHeights=[0.7])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),col),
                           ("TOPPADDING",(0,0),(-1,-1),0),
                           ("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return [Spacer(1, space_before), t, Spacer(1, space_after)]

def box(flows, pad=12, bg=TINT, edge=None):
    t = Table([[flows]], colWidths=[PW - 2*M])
    st = [("BACKGROUND",(0,0),(-1,-1),bg),
          ("LEFTPADDING",(0,0),(-1,-1),pad), ("RIGHTPADDING",(0,0),(-1,-1),pad),
          ("TOPPADDING",(0,0),(-1,-1),pad),  ("BOTTOMPADDING",(0,0),(-1,-1),pad)]
    if edge: st.append(("LINEBEFORE",(0,0),(0,-1),3,edge))
    t.setStyle(TableStyle(st)); return t

def bullets(items):
    return [Paragraph(x, bullet, bulletText="•") for x in items]

story = []
A = story.append
from reportlab.platypus import PageBreak

# ---------------------------------------------------------------- PROPOSAL
A(Paragraph("PROPOSAL", kicker))
A(Spacer(1, 5))
A(Paragraph("Video and SEO for Dick's Pawn Superstore", h1))
A(Spacer(1, 3))
A(Paragraph("Prepared for Jill &nbsp;\u00b7&nbsp; %s" % TODAY, sub))
A(Spacer(1, 14))

A(Paragraph(
  "Four videos a month on your channels, the SEO work included, and none of it run "
  "by you. That is the target either way \u2014 the two plans differ on how the "
  "videos get made and how much of your time it takes.", lead))
A(Spacer(1, 10))

def cell(t, st=tcell): return Paragraph(t, st)
ROWS = [
  [cell("", tlabel), cell("Standard", thead), cell("Full production", thead)],
  [cell("Price", tlabel), cell("$5,000 / month", tprice), cell("$10,000 / month", tprice)],
  [cell("Best for", tlabel),
   cell("Staying in front of people every week, month after month.", tcellb),
   cell("A flagship piece \u2014 a launch, a new store, a campaign.", tcellb)],
  [cell("How it<br/>is made", tlabel),
   cell("AI host pieces built from your own store photos, plus in-store filming. "
        "I shoot and produce."),
   cell("Shot on location with a full crew, lighting and sound.")],
  [cell("On camera", tlabel),
   cell("You and your staff."),
   cell("Hired talent.")],
  [cell("Your time", tlabel),
   cell("About half a day a month, when it suits you."),
   cell("None.")],
]
CW = [1.15*inch, 2.75*inch, 2.75*inch]
plan = Table(ROWS, colWidths=CW, repeatRows=1)
plan.setStyle(TableStyle([
    ("BACKGROUND",(1,0),(-1,0), ACC),
    ("BACKGROUND",(0,0),(0,0), colors.white),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [colors.white, TINT]),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LEFTPADDING",(0,0),(-1,-1),9), ("RIGHTPADDING",(0,0),(-1,-1),9),
    ("TOPPADDING",(0,0),(-1,-1),5),  ("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LINEBELOW",(0,0),(-1,-2),0.5,RULE),
    ("LINEAFTER",(0,0),(-2,-1),0.5,RULE),
]))
A(plan)
A(Spacer(1, 9))
A(Paragraph(
  "The five-myths video I sent you is a Standard piece \u2014 presenter and store "
  "AI-generated from your own photos, which is what makes four a month possible at "
  "this price.", body))
A(Spacer(1, 4))

A(KeepTogether([
  Paragraph("Where the $5,000 goes", h2),
  Paragraph(
    "I film and produce. A dedicated editor on my team cuts everything \u2014 $2,000 "
    "of the $5,000 is his. The rest covers the AI production, SEO, posting and tools.",
    body),
]))

A(KeepTogether([
  Paragraph("What I can and cannot promise", h2),
  Paragraph(
    "I cannot promise results, and I cannot promise a fixed count \u2014 four is a "
    "target, and what gets made depends on the time and resources available that "
    "month. Clause 3 spells that out. Nobody honest can guarantee views, calls or "
    "walk-ins.", body),
  Paragraph(
    "What I will do is tell you <b>before</b> a month falls short, not after. And if "
    "it is not working for you, you stop \u2014 any month, no reason needed.", body),
]))

A(Spacer(1, 3))
A(box([
    Paragraph("There is no contract term.", calloutH),
    Paragraph(
      "No minimum number of months. No notice period. No cancellation fee. Email me "
      "and we stop \u2014 you are paid up through the month you are in.", callout),
], edge=ACC))

A(Spacer(1, 10))
A(Paragraph(
  "Sign the agreement overleaf and send it back. Any questions first, call me on "
  "<b>806-544-8098</b>.",
  body))

A(PageBreak())

# --------------------------------------------------------------- AGREEMENT
A(Paragraph("AGREEMENT", kicker))
A(Spacer(1, 5))
A(Paragraph("Video and SEO agreement", h1))
A(Spacer(1, 3))
A(Paragraph(
  "Between <b>Kyle Fries Marketing</b> (\u201cwe\u201d) and <b>Dick's Pawn Superstore</b> "
  "(\u201cyou\u201d) \u00b7 %s" % TODAY, sub))
A(Spacer(1, 9))

BOXSIDE = 11
def tick(label):
    sq = Table([[""]], colWidths=[BOXSIDE], rowHeights=[BOXSIDE])
    sq.setStyle(TableStyle([("BOX",(0,0),(-1,-1),0.9,INK),
                            ("LEFTPADDING",(0,0),(-1,-1),0),
                            ("RIGHTPADDING",(0,0),(-1,-1),0),
                            ("TOPPADDING",(0,0),(-1,-1),0),
                            ("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return sq, Paragraph(label, clause)

sq1, l1 = tick("<b>Standard</b> \u2014 $5,000 per month")
sq2, l2 = tick("<b>Full production</b> \u2014 $10,000 per month")
sel = Table([[Paragraph("Plan (tick one)", tlabel), sq1, l1, sq2, l2]],
            colWidths=[1.02*inch, BOXSIDE+4, 2.16*inch, BOXSIDE+4, 2.4*inch],
            rowHeights=[16])
sel.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                         ("LEFTPADDING",(0,0),(-1,-1),0),
                         ("RIGHTPADDING",(0,0),(-1,-1),0),
                         ("TOPPADDING",(0,0),(-1,-1),0),
                         ("BOTTOMPADDING",(0,0),(-1,-1),0)]))
A(sel)
A(Spacer(1, 4))
for f in rule(space_before=0, space_after=2): A(f)

CL = [
 ("1. What we do",
  "A target of four finished short-form videos each month, posted to your social "
  "accounts, plus ongoing SEO work on your website and your Google Business Profiles "
  "for all five "
  "stores. Each runs 30 to 60 seconds, vertical and captioned, covering idea, "
  "script, production, editing, graphics and posting."),
 ("2. What it costs",
  "The monthly price of the plan ticked above, invoiced on the first and due within "
  "15 days. That is the whole cost \u2014 we will not invoice you for anything else "
  "unless we ask you first and you say yes in writing."),
 ("3. What we do not guarantee",
  "We do not guarantee any particular result: views, followers, calls, walk-ins, "
  "search ranking or sales. Anything we have said about likely outcomes is an "
  "informed expectation based on research, past work and experience \u2014 not a "
  "promise.<br/><br/>"
  "We also do not guarantee a fixed number of deliverables. Four videos a month is a "
  "target. What actually gets made in a given month depends on the time and the "
  "resources available \u2014 including your staff for filming, a location we can "
  "film in, and access to the accounts. Where those fall short, the month's output "
  "falls short with them.<br/><br/>"
  "What we commit to is telling you before the month ends rather than after. "
  "Payments are not refundable, and we do not issue credits or make-good work for a "
  "month that falls short. If you are not happy with what a month produced, your "
  "remedy is to stop: you can do that at any time under clause 4, and you will not be "
  "invoiced again."),
 ("4. Stopping",
  "You can stop at any time, for any reason, by email. No minimum term, no notice "
  "period, no cancellation fee. We stop posting, hand back your account access and "
  "hand over everything we have made for you. We do not invoice you again. If we ever "
  "need to stop, you get 30 days' notice."),
 ("5. Running it without you",
  "You approve nothing. We write, produce and post on our own \u2014 no drafts to "
  "review and no emails to answer. Every claim we put on screen comes from a short "
  "list of facts you confirm once at the start. If you ever see something you do not "
  "want up, tell us and it comes down the same day."),
 ("6. Filming, on the Standard plan",
  "Some of each month's videos are filmed in your stores with your staff on camera. "
  "That needs about half a day a month, at a time you pick, worked around your "
  "opening hours. We bring everything else.<br/><br/>"
  "If a month comes when you cannot spare the time, we make that month's videos "
  "without filming and the invoice does not change. Full production uses our own "
  "talent and needs none of your people."),
 ("7. Who owns the videos",
  "You do. Once a month's invoice is paid, that month's videos are yours outright, to "
  "use however and for as long as you want, including after you stop. We would like "
  "to show the work in our portfolio, but we will ask you first."),
 ("8. What we need from you",
  "Photos of the stores, access to the accounts we post to, one pass over the facts "
  "list in clause 5, and staff for filming as described in clause 6."),
 ("9. Privacy, and the rest",
  "Anything you share with us that is not already public stays between us, and "
  "account logins are used only to post your videos and handed back when we stop. "
  "This is the whole agreement and it replaces anything discussed before it. South "
  "Carolina law governs it, and it can only be changed in writing, signed by both "
  "of us."),
]
# Deliberate break: clauses 1-6 on page 2, the rest with the signature on
# page 3. Left to flow, everything lands on page 2 and the signature block is
# stranded alone on a third page.
for i, (h, t) in enumerate(CL):
    A(KeepTogether([Paragraph(h, clauseH), Paragraph(t, clause)]))
    if i == 5:
        A(PageBreak())

A(Spacer(1, 6))
for f in rule(space_before=0, space_after=9): A(f)

role = S("role", fontName="Sans-B", fontSize=10.2, leading=13, textColor=INK)
LINE = colors.HexColor("#8b9aa8")
COL  = 3.05*inch
GUT  = (PW - 2*M) - 2*COL
sig = Table(
    [[Paragraph("Dick's Pawn Superstore", role), "", Paragraph("Kyle Fries Marketing", role)],
     ["", "", ""],
     [Paragraph("Signature", sigLbl), "", Paragraph("Signature", sigLbl)],
     ["", "", ""],
     [Paragraph("Name and date", sigLbl), "", Paragraph("Name and date", sigLbl)]],
    colWidths=[COL, GUT, COL],
    rowHeights=[13, 24, 10, 22, 10])
sig.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),0),  ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ("LINEBELOW",(0,1),(0,1),0.8,LINE), ("LINEBELOW",(2,1),(2,1),0.8,LINE),
    ("LINEBELOW",(0,3),(0,3),0.8,LINE), ("LINEBELOW",(2,3),(2,3),0.8,LINE),
]))
A(sig)

doc = BaseDocTemplate("/home/user/dicks-pawn-redesign/business/dicks-pawn-proposal-and-agreement.pdf",
                      pagesize=LETTER, leftMargin=M, rightMargin=M,
                      topMargin=M, bottomMargin=M,
                      title="Proposal and Agreement — Dick's Pawn Superstore",
                      author="Kyle Fries Marketing",
                      subject="Short-form video production, $5,000/month, no minimum term")
frame = Frame(M, M, PW-2*M, PH-2*M, id="f", leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=header_footer)])
doc.build(story)
print("built")
