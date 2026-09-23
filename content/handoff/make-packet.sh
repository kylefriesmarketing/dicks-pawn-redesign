#!/usr/bin/env bash
#
# Rebuild the handoff packet from tracked repo files.
#
# The packet's build target is EP02; EP01 ships inside it as the reference
# build, which is why the finished video lands in 06-reference-video/.
#
# Needs ffmpeg and ImageMagick. Neither is installed in this dev container —
# the real run was done in the Higgsfield sandbox (sandbox_exec), which has both.
# Anywhere with those two binaries produces an identical packet.
#
# Output: dist/dicks-pawn-handoff-packet.zip  (~11 MB)

set -euo pipefail
cd "$(dirname "$0")/../.."          # repo root
OUT=dist/packet
rm -rf "$OUT" && mkdir -p "$OUT"/{02-prompts,03-reference/store-photos,04-build,06-reference-video,07-commercial}

# --- text ---------------------------------------------------------------
cp content/handoff/START-HERE.md          "$OUT/00-START-HERE.md"
cp content/video-series-bible.md          "$OUT/01-series-bible.md"
cp content/prompts/00-runbook.md          "$OUT/02-prompts/"
cp content/prompts/01-character.md        "$OUT/02-prompts/"
cp content/prompts/ep0{1,2,3}-*.md          "$OUT/02-prompts/"
cp content/output/README.md               "$OUT/02-prompts/post-production-notes.md"
cp content/handoff/conversation.md        "$OUT/05-full-conversation.md"
cp business/dicks-pawn-proposal-and-agreement.pdf "$OUT/07-commercial/"

# --- build scripts ------------------------------------------------------
cp content/build/{burn.py,factcard.py,caps.ass} "$OUT/04-build/"

# --- reference images ---------------------------------------------------
# Contact sheets and boards are already JPEG and already small enough.
cp content/reference/ep01-board{1,2,3}.jpg \
   content/reference/ep01-{clips-raw,fact-card,final-frames}.jpg "$OUT/03-reference/"
cp assets/dp-logo.png "$OUT/03-reference/dicks-pawn-logo.png"

# The host plate and the store photos are large PNGs (~30 MB together).
# Downscale to 1800px JPEG — plenty for a reference, 20x smaller.
convert content/reference/super-dick-host.png \
        -resize 1800x1800\> -quality 86 "$OUT/03-reference/super-dick-host-LOCKED.jpg"
for f in content/reference/store-photos/*.png; do
  convert "$f" -resize 1800x1800\> -quality 86 \
          "$OUT/03-reference/store-photos/$(basename "${f%.png}").jpg"
done

# --- video --------------------------------------------------------------
# 720p reference cut of the delivered EP01 master: 27 MB -> 5.4 MB.
ffmpeg -y -v error -i content/output/ep01-5-myths-FINAL.mp4 \
  -vf "scale=720:1280" -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p \
  -c:a aac -b:a 112k -movflags +faststart "$OUT/06-reference-video/ep01-5-myths-720p.mp4"

# --- zip ----------------------------------------------------------------
( cd dist && rm -f dicks-pawn-handoff-packet.zip \
  && zip -rq dicks-pawn-handoff-packet.zip packet -x '*.DS_Store' )

echo "built dist/dicks-pawn-handoff-packet.zip"
unzip -l dist/dicks-pawn-handoff-packet.zip | tail -3
