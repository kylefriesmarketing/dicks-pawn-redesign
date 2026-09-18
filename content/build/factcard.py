from PIL import Image, ImageDraw, ImageFont
F = "/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf"
NAVY=(19,53,100); GOLD=(201,162,75); WHITE=(255,255,255)
W,H = 1080,1920
img = Image.new("RGB",(W,H),NAVY); d = ImageDraw.Draw(img)

def fit(text, target_w, lo=20, hi=220):
    best = lo
    while lo <= hi:
        mid = (lo+hi)//2
        f = ImageFont.truetype(F, mid)
        if d.textlength(text, font=f) <= target_w:
            best = mid; lo = mid+1
        else:
            hi = mid-1
    return ImageFont.truetype(F, best)

def centre(text, y, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W-w)/2, y), text, font=font, fill=fill)

# subtle diagonal texture so it isn't a flat plate
for i in range(-H, W, 46):
    d.line([(i,0),(i+H,H)], fill=(24,62,112), width=12)

f_kick = ImageFont.truetype(F, 40)
centre("FACT", 560, f_kick, GOLD)

f_big = fit("NO CREDIT CHECK", 930)
centre("NO CREDIT CHECK", 630, f_big, WHITE)

d.rectangle([(390,810),(690,818)], fill=GOLD)

f_sub = fit("IT NEVER TOUCHES", 760)
centre("IT NEVER TOUCHES", 880, f_sub, WHITE)
centre("YOUR CREDIT SCORE", 975, fit("YOUR CREDIT SCORE", 760), WHITE)

lg = Image.open("logo.png").convert("RGBA").resize((190,190), Image.LANCZOS)
img.paste(lg, ((W-190)//2, 1180), lg)

img.save("factcard.png")
print("factcard.png written")
