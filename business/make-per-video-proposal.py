"""Per-video proposal + agreement: $300 a video, minimum ten, production only.

Chrome (fonts, letterhead, box/rule helpers) mirrors make-proposal.py. Kept as a
copy rather than a shared module on purpose: that document is already out with
the client and dated, and importing it here would rebuild and re-date it. If a
THIRD document appears, extract business/letterhead.py first — see README.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime

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
M = 0.8*inch

def S(name, **kw):
    base = dict(fontName="Sans", fontSize=10.2, leading=15.4, textColor=INK,
                spaceAfter=0, spaceBefore=0)
    base.update(kw); return ParagraphStyle(name, **base)

body     = S("body", fontSize=10, leading=14.6, spaceAfter=7)
lead     = S("lead", fontSize=11.2, leading=16.4, spaceAfter=9)
h1       = S("h1", fontName="Sans-B", fontSize=19, leading=23, spaceAfter=3)
h2       = S("h2", fontName="Sans-B", fontSize=11.8, leading=15, textColor=ACC,
             spaceBefore=11, spaceAfter=5)
kicker   = S("kicker", fontName="Sans-B", fontSize=8.2, leading=11, textColor=MUTED)
sub      = S("sub", fontSize=10.2, leading=14, textColor=MUTED, spaceAfter=2)
bullet   = S("bullet", fontSize=10, leading=14.2, spaceAfter=3,
             leftIndent=15, bulletIndent=2, firstLineIndent=0)
callout  = S("callout", fontSize=10.6, leading=15.6, spaceAfter=0)
calloutH = S("calloutH", fontName="Sans-B", fontSize=12.2, leading=16, textColor=ACC,
             spaceAfter=5)
clause   = S("clause", fontSize=9.5, leading=13.2, spaceAfter=4)
clauseH  = S("clauseH", fontName="Sans-B", fontSize=10.2, leading=13, spaceBefore=5,
             spaceAfter=3)
sigLbl   = S("sigLbl", fontSize=8.4, leading=11, textColor=MUTED)
tcell    = S("tcell", fontSize=9.2, leading=12.6)
tlabel   = S("tlabel", fontName="Sans-B", fontSize=9.2, leading=12.6, textColor=MUTED)
tbig     = S("tbig", fontName="Sans-B", fontSize=15, leading=18)
tnote    = S("tnote", fontSize=9.2, leading=12.4, textColor=MUTED)

TODAY = datetime.date.today().strftime("%B %-d, %Y")

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Sans-B", 10.6); canvas.setFillColor(INK)
    canvas.drawString(M, PH - M + 26, "KYLE FRIES MARKETING")
    canvas.setFont("Sans", 8.4); canvas.setFillColor(MUTED)
    canvas.drawRightString(PW - M, PH - M + 26,
                           "Kylefriesmarketing@gmail.com · 806-544-8098")
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.7)
    canvas.line(M, PH - M + 18, PW - M, PH - M + 18)
    canvas.setFont("Sans", 8.2); canvas.setFillColor(MUTED)
    canvas.drawString(M, M - 34, "Dick's Pawn Superstore · Video production · %s" % TODAY)
    canvas.drawRightString(PW - M, M - 34, "Page %d" % doc.page)
    canvas.restoreState()

def rule(space_before=4, space_after=10):
    t = Table([[""]], colWidths=[PW - 2*M], rowHeights=[0.7])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),RULE),
                           ("TOPPADDING",(0,0),(-1,-1),0),
                           ("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return [Spacer(1, space_before), t, Spacer(1, space_after)]

def box(flows, pad=10, bg=TINT, edge=None):
    t = Table([[flows]], colWidths=[PW - 2*M])
    st = [("BACKGROUND",(0,0),(-1,-1),bg),
          ("LEFTPADDING",(0,0),(-1,-1),pad), ("RIGHTPADDING",(0,0),(-1,-1),pad),
          ("TOPPADDING",(0,0),(-1,-1),pad),  ("BOTTOMPADDING",(0,0),(-1,-1),pad)]
    if edge: st.append(("LINEBEFORE",(0,0),(0,-1),3,edge))
    t.setStyle(TableStyle(st)); return t

def bullets(items):
    return [Paragraph(x, bullet, bulletText="•") for x in items]

story = []; A = story.append

# ---------------------------------------------------------------- PROPOSAL
A(Paragraph("PROPOSAL", kicker))
A(Spacer(1, 5))
A(Paragraph("Video production for Dick's Pawn Superstore", h1))
A(Spacer(1, 3))
A(Paragraph("Prepared for Jill &nbsp;·&nbsp; %s" % TODAY, sub))
A(Spacer(1, 10))

A(Paragraph(
  "<b>$300 a video.</b> I make them, you post them. Order ten to start, order more "
  "whenever you want them, and stop whenever you do not — there is no monthly "
  "fee and nothing to cancel.", lead))
A(Spacer(1, 6))

PRICE = [
  [Paragraph("Per video", tlabel),
   Paragraph("Minimum order", tlabel),
   Paragraph("Above ten", tlabel)],
  [Paragraph("$300", tbig),
   Paragraph("10 videos — $3,000", tbig),
   Paragraph("No limit, same $300", tbig)],
  [Paragraph("Finished, captioned, ready to upload", tnote),
   Paragraph("One order, delivered in batches", tnote),
   Paragraph("Ordered in tens, whenever you like", tnote)],
]
pt = Table(PRICE, colWidths=[2.0*inch, 2.55*inch, 2.35*inch])
pt.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), TINT),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LEFTPADDING",(0,0),(-1,-1),11), ("RIGHTPADDING",(0,0),(-1,-1),11),
    ("TOPPADDING",(0,0),(-1,0),9),    ("TOPPADDING",(0,1),(-1,-1),1),
    ("BOTTOMPADDING",(0,0),(-1,-2),2),("BOTTOMPADDING",(0,-1),(-1,-1),10),
    ("LINEAFTER",(0,0),(-2,-1),0.5,RULE),
]))
A(pt)
A(Spacer(1, 9))

A(Paragraph("What $300 buys", h2))
for f in bullets([
  "A finished short-form video, up to 60 seconds, vertical and fully captioned.",
  "The idea and the script, written from your own facts — no invented claims.",
  "Production: the AI host format built from your store photos, or your own footage "
  "cut together. Both are $300.",
  "Edit, on-screen graphics, burned captions and your logo.",
  "<b>One round of changes</b> on each video.",
  "Delivered as an MP4, ready to upload. Yours outright — use them anywhere, "
  "forever.",
]): A(f)

A(Paragraph("What this does not include", h2))
A(Paragraph(
  "This is production only. Once a video lands in your hands, the rest is yours:", body))
for f in bullets([
  "Posting and scheduling to Instagram, Facebook or TikTok.",
  "Writing the post copy and hashtags, and replying to comments.",
  "Tracking what works and steering the next batch off it.",
  "SEO on your site or your Google Business Profiles.",
]): A(f)
A(Spacer(1, 3))
A(Paragraph(
  "If you would rather not take that on, the managed plan covers all of it — "
  "separate proposal, monthly fee. This one is for when you want the videos and "
  "nothing else.", body))

A(Spacer(1, 2))
A(box([
    Paragraph("You only ever pay for videos you have.", calloutH),
    Paragraph(
      "Half up front to start the block, the balance when the tenth video lands. If "
      "you stop partway through, you pay $300 for each video already delivered and "
      "the rest of your deposit comes straight back. There is no scenario where you "
      "have paid me for something you do not have.", callout),
], edge=ACC))

A(Spacer(1, 9))
A(Paragraph(
  "<b>How the videos get made.</b> Most are built with AI — the presenter and "
  "store generated from photographs of your own locations, which is how the cost "
  "stays where it is. The five-myths video I sent you was made that way. Where you "
  "want real footage of your stores and staff instead, I film it, same price.", body))
A(Paragraph(
  "Say the word and I will start on the first ten. Questions first, call me on "
  "<b>806-544-8098</b>.", body))

A(PageBreak())

# --------------------------------------------------------------- AGREEMENT
A(Paragraph("AGREEMENT", kicker))
A(Spacer(1, 5))
A(Paragraph("Video production agreement", h1))
A(Spacer(1, 3))
A(Paragraph(
  "Between <b>Kyle Fries Marketing</b> (“we”) and <b>Dick's Pawn "
  "Superstore</b> (“you”) · %s" % TODAY, sub))
A(Spacer(1, 8))

ORD = Table([[Paragraph("This order", tlabel),
              Paragraph("_______ videos at $300 each &nbsp;=&nbsp; $__________", clause)]],
            colWidths=[1.02*inch, PW - 2*M - 1.02*inch], rowHeights=[16])
ORD.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                         ("LEFTPADDING",(0,0),(-1,-1),0),
                         ("RIGHTPADDING",(0,0),(-1,-1),0),
                         ("TOPPADDING",(0,0),(-1,-1),0),
                         ("BOTTOMPADDING",(0,0),(-1,-1),0)]))
A(ORD)
A(Spacer(1, 4))
for f in rule(space_before=0, space_after=2): A(f)

CL = [
 ("1. What you are buying",
  "Finished short-form videos, at $300 each, in a minimum order of ten. Each video "
  "runs up to 60 seconds, is vertical and fully captioned, and covers the idea, the "
  "script, the production, the edit, the on-screen graphics and your logo. It is "
  "delivered as a finished MP4 file, ready for you to upload.<br/><br/>"
  "Unlike a monthly plan, the count here is fixed: you order a number of videos and "
  "we owe you that number of videos."),
 ("2. What it costs, and when",
  "$300 per video. Half the order is due before we start and the balance is due when "
  "the last video in the order is delivered. We will not invoice you for anything "
  "else unless we ask first and you agree in writing.<br/><br/>"
  "Further orders are at the same $300, in blocks of ten, whenever you want them. "
  "There is no monthly fee, no minimum term and nothing to cancel."),
 ("3. Stopping partway, and refunds",
  "You can stop an order at any time, by email. We work out what is owed at $300 for "
  "each video already delivered to you, and <b>the remainder of your deposit is "
  "returned within 14 days</b>. You never pay for a video you have not received, and "
  "we never keep money for work we have not done.<br/><br/>"
  "Delivered videos are not refundable, and a video is delivered once the file has "
  "been sent to you. If something about a delivered video is wrong, clause 4 covers "
  "it — raise it with us in writing within 14 days and we will put it right."),
 ("4. Changes",
  "Each video includes one round of changes: the script, the captions, the on-screen "
  "graphics, the music, the pace, the cut. Ask for them within 14 days of delivery "
  "and they are free.<br/><br/>"
  "What one round does not cover is starting again — a different topic, a "
  "different script from scratch, or re-generating the footage because you would "
  "prefer a different take. That is a new video at $300, and we will tell you which "
  "one you are asking for before we do anything."),
 ("5. When they arrive",
  "The first ten are delivered within 21 days of us having the photos and the "
  "confirmed facts list in clause 7, in batches rather than all at the end. For "
  "larger or repeat orders we agree the schedule in writing before you pay.<br/><br/>"
  "If we are going to miss a date we will tell you before it passes, not after. If we "
  "miss it by more than 14 days you may cancel the rest of the order under clause 3 "
  "with nothing further owed."),
 ("6. What we do not guarantee",
  "We do not guarantee any result: views, followers, calls, walk-ins, search ranking "
  "or sales. Anything we have said about likely outcomes is an informed expectation "
  "based on research, past work and experience — not a promise. Whether these "
  "videos work also depends heavily on how and when they are posted, which under this "
  "agreement is yours to do.<br/><br/>"
  "What we do guarantee is the videos themselves: the number you ordered, to the "
  "specification in clause 1."),
 ("7. What we need from you",
  "Photographs of the stores, and one pass over a short list of facts — the "
  "claims we are allowed to put on screen. We confirm that list once, at the start, "
  "and we do not put anything on screen that is not on it. Where a video is filmed "
  "rather than generated, we also need access to the store and whoever is appearing "
  "in it, at a time you pick."),
 ("8. Posting is yours",
  "We do not post these videos, schedule them, write the post copy, reply to comments "
  "or report on how they do, and we are not responsible for what happens after a file "
  "leaves our hands. You decide what goes up, where and when.<br/><br/>"
  "If you would like that side handled, it is a separate agreement and a monthly fee."),
 ("9. Who owns them, and how they are made",
  "You do. Once an order is paid, those videos are yours outright, to use however and "
  "for as long as you like. We would like to show the work in our portfolio, but we "
  "will ask you first.<br/><br/>"
  "Some or all of the footage is generated with AI tools, built from photographs of "
  "your own stores, and the presenter is a generated character rather than a real "
  "employee. You are agreeing to that, and you are free to disclose it however you "
  "wish on your channels."),
 ("10. Liability, and the rest",
  "Our total liability to you for anything arising out of this agreement is limited "
  "to what you paid us for the video the issue relates to, and neither of us is "
  "liable to the other for lost profits, lost revenue, lost goodwill or any other "
  "indirect loss. Any claim must be brought within six months of the delivery it "
  "relates to.<br/><br/>"
  "Anything you share with us that is not already public stays between us. By "
  "signing, you confirm you have read this agreement and are not relying on anything "
  "said outside it. This is the whole agreement and it replaces anything discussed "
  "before it. If any part is found unenforceable the rest still stands. South "
  "Carolina law governs it, and it can only be changed in writing, signed by both "
  "of us."),
]
for i, (h, t) in enumerate(CL):
    A(KeepTogether([Paragraph(h, clauseH), Paragraph(t, clause)]))
    if i == 5:
        A(PageBreak())

A(Spacer(1, 6))
for f in rule(space_before=0, space_after=9): A(f)

role = S("role", fontName="Sans-B", fontSize=10.2, leading=13)
LINE = colors.HexColor("#8b9aa8")
COL  = 3.05*inch
GUT  = (PW - 2*M) - 2*COL
sig = Table(
    [[Paragraph("Dick's Pawn Superstore", role), "", Paragraph("Kyle Fries Marketing", role)],
     ["", "", ""],
     [Paragraph("Signature", sigLbl), "", Paragraph("Signature", sigLbl)],
     ["", "", ""],
     [Paragraph("Name and date", sigLbl), "", Paragraph("Name and date", sigLbl)]],
    colWidths=[COL, GUT, COL], rowHeights=[13, 24, 10, 22, 10])
sig.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LEFTPADDING",(0,0),(-1,-1),0), ("RIGHTPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),0),  ("BOTTOMPADDING",(0,0),(-1,-1),2),
    ("LINEBELOW",(0,1),(0,1),0.8,LINE), ("LINEBELOW",(2,1),(2,1),0.8,LINE),
    ("LINEBELOW",(0,3),(0,3),0.8,LINE), ("LINEBELOW",(2,3),(2,3),0.8,LINE),
]))
A(sig)

OUT = "/home/user/dicks-pawn-redesign/business/dicks-pawn-per-video-proposal.pdf"
doc = BaseDocTemplate(OUT, pagesize=LETTER, leftMargin=M, rightMargin=M,
                      topMargin=M, bottomMargin=M,
                      title="Video production proposal and agreement — Dick's Pawn Superstore",
                      author="Kyle Fries Marketing",
                      subject="Short-form video production, $300 per video, ten minimum")
frame = Frame(M, M, PW-2*M, PH-2*M, id="f", leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=header_footer)])
doc.build(story)
print("built", OUT)
