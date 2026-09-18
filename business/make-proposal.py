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
clause    = S("clause", fontSize=9.5, leading=13.4, spaceAfter=5)
clauseH   = S("clauseH", fontName="Sans-B", fontSize=10.2, leading=13, textColor=INK,
              spaceBefore=7, spaceAfter=3)
sigLbl    = S("sigLbl", fontSize=8.4, leading=11, textColor=MUTED)
fine      = S("fine", fontSize=8.6, leading=12.6, textColor=MUTED)

TODAY = datetime.date.today().strftime("%B %-d, %Y")

def header_footer(canvas, doc):
    canvas.saveState()
    # letterhead
    canvas.setFont("Sans-B", 10.6); canvas.setFillColor(INK)
    canvas.drawString(M, PH - M + 26, "KYLE FRIES MARKETING")
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.7)
    canvas.line(M, PH - M + 18, PW - M, PH - M + 18)
    # footer
    canvas.setFont("Sans", 8.2); canvas.setFillColor(MUTED)
    canvas.drawString(M, M - 34, "Dick's Pawn Superstore · Social video · %s" % TODAY)
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

# ---------------------------------------------------------------- PROPOSAL
A(Paragraph("PROPOSAL", kicker))
A(Spacer(1, 5))
A(Paragraph("Short-form video for Dick's Pawn Superstore", h1))
A(Spacer(1, 3))
A(Paragraph("Prepared for Jill &nbsp;·&nbsp; %s" % TODAY, sub))
A(Spacer(1, 16))

A(Paragraph(
  "Here is the whole thing in three lines. You get four videos a month, written, "
  "made and posted for you. It costs $5,000 a month. You can stop any time you "
  "want, and there is nothing to get out of.", lead))

A(Spacer(1, 6))
A(box([
    Paragraph("There is no contract term.", calloutH),
    Paragraph(
      "No minimum number of months. No notice period. No cancellation fee. "
      "If you want to stop, send me an email and we stop — you are paid up "
      "through the month you are in, and that is the end of it.<br/><br/>"
      "If the first month doesn't convince you, you have spent one month.", callout),
], edge=ACC))

A(Paragraph("What you get each month", h2))
A(Paragraph(
  "Four videos a month, on your channels, without you touching any of it.", body))
for f in bullets([
    "<b>Four videos a month</b> \u2014 30 to 60 seconds each, vertical, posted to "
    "TikTok, Instagram Reels and YouTube Shorts.",
    "<b>Everything included</b> \u2014 idea, script, production, editing, graphics, "
    "captions and the posting itself.",
    "<b>Nothing for you to do</b> \u2014 no drafts to approve, no emails to answer, "
    "nothing to upload.",
    "<b>Pull anything, any time.</b> You never have to look, but one message takes a "
    "video down the same day.",
]): A(f)

A(Paragraph("What it costs", h2))
A(Paragraph(
  "<b>$5,000 a month.</b> That is the full cost \u2014 production, posting, captions "
  "and graphics are all in it. No setup fee, no per-video charges, and nothing gets "
  "added to an invoice without asking you first.", body))

A(Paragraph("How the videos get made", h2))
A(Paragraph(
  "The presenter and the store around him are generated, built to match your real "
  "stores from your own photos. No shoot days, no crew in your stores, no working "
  "around business hours. Telling you up front so it is never a surprise later.",
  body))

A(KeepTogether([
  Paragraph("The one thing we need up front", h2),
  Paragraph(
    "So we can run without checking in, you confirm a short list of facts we are "
    "allowed to state on camera \u2014 policies, licensing, store count. One sitting, "
    "at the start, and nothing goes on screen that is not on it.", body),
]))

A(KeepTogether([
  Paragraph("Getting started", h2),
  Paragraph(
    "Sign the agreement on the next page and send it back. First invoice goes out the "
    "day we start, first videos go up within ten business days.", body),
  Paragraph(
    "If you want to talk anything through first, call me any time \u2014 "
    "<b>[ your phone ]</b> or <b>[ your email ]</b>.", body),
]))

from reportlab.platypus import PageBreak
A(PageBreak())

# --------------------------------------------------------------- AGREEMENT
A(Paragraph("AGREEMENT", kicker))
A(Spacer(1, 5))
A(Paragraph("Video production agreement", h1))
A(Spacer(1, 3))
A(Paragraph(
  "Between <b>Kyle Fries Marketing</b> (“we”) and <b>Dick's Pawn Superstore</b> "
  "(“you”) · %s" % TODAY, sub))
A(Spacer(1, 4))
for f in rule(): A(f)

CL = [
 ("1. What we do",
  "Four finished short-form videos each month, posted to your social accounts. Each "
  "runs 30 to 60 seconds, vertical and captioned. That covers the idea, the script, "
  "the production, the editing, the graphics, the captions and the posting."),
 ("2. What it costs",
  "$5,000 per month, invoiced on the first and due within 15 days. That is the whole "
  "cost \u2014 we will not invoice you for anything else unless we ask you first and "
  "you say yes in writing."),
 ("3. Stopping",
  "You can stop at any time, for any reason, by email. No minimum term, no notice "
  "period, no cancellation fee.<br/><br/>"
  "We stop posting, hand back your account access and hand over everything you have "
  "paid for. We do not invoice you again \u2014 you are never billed for a month you "
  "did not want. If we ever need to stop, we will give you 30 days' notice."),
 ("4. Running it without you",
  "You approve nothing. We write, produce and post on our own \u2014 no drafts to "
  "review and no emails to answer.<br/><br/>"
  "Two things keep that safe. Every claim we put on screen comes from a short list of "
  "facts you confirm once at the start, and nothing goes on screen that is not on it. "
  "And if you ever see something you do not want up, tell us and it comes down the "
  "same day, no reason needed."),
 ("5. Who owns the videos",
  "You do. Once a month's invoice is paid, that month's videos are yours outright, to "
  "use however and for as long as you want, including after you stop. We would like to "
  "show the work in our portfolio, but we will ask you first."),
 ("6. What we need from you",
  "Three things, all at the start: photos of the stores, access to the accounts we "
  "post to, and one pass over the facts list in clause 4. After that we do not need "
  "anything from you."),
 ("7. Keeping things private",
  "Anything you share with us that is not already public stays between us. Account "
  "logins are used only to post your videos and are handed back when we stop."),
 ("8. The rest",
  "This is the whole agreement and it replaces anything discussed before it. South "
  "Carolina law governs it. It can only be changed in writing, signed by both of us."),
]
for h, t in CL:
    A(KeepTogether([Paragraph(h, clauseH), Paragraph(t, clause)]))

A(Spacer(1, 6))
for f in rule(space_before=0, space_after=9): A(f)

# Signature grid with explicit row heights — nested flowable cells make
# reportlab over-estimate the block and bump it to its own page.
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
    rowHeights=[14, 28, 11, 26, 11])
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
