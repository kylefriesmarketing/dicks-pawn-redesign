# Production runbook — what it costs and what order to run it

## Measured costs (Higgsfield, September 2026)

These are metered, not estimated — each was read from a `get_cost` preflight or
observed as a balance delta on a real job.

| Step | Model | Params | Credits |
|---|---|---|---|
| Host character | `soul_2` | 3:4, 2k | **0.12** |
| Storyboard sheet | `gpt_image_2` | 21:9, 2k, high | **6.50** |
| Video clip | `seedance_2_5` | 9:16, 1080p, 15s | **135.00** |
| Video clip | `seedance_2_5` | 9:16, 720p, 15s | **97.50** |
| Video clip | `seedance_2_5` | 9:16, 480p, 15s | **45.00** |

Seedance is billed **per second of output**, and resolution is the multiplier:

| Resolution | Credits/sec |
|---|---|
| 1080p | 9.0 |
| 720p | 6.5 |
| 480p | 3.0 |

**Video is ~95% of the budget.** Images are rounding error. Every cost decision
in this series is a decision about seconds of video, not about image quality.

## Cost per episode

| Build | Boards | Clips | Total |
|---|---|---|---|
| 45s @ 1080p (the spec) | 19.5 | 405 | **~425** |
| 45s @ 720p | 19.5 | 292.5 | **~312** |
| 30s @ 1080p (2 clips) | 13.0 | 270 | **~283** |
| 15s @ 1080p (1 clip) | 6.5 | 135 | **~142** |
| 45s @ 480p (proof only) | 19.5 | 135 | **~155** |

A 500-credit pack covers one full 45s episode at 1080p with change left over.
2,000 credits covers roughly four.

**The cheapest real lever is duration, not resolution.** Dropping 45s to 30s
saves 135 credits and costs you two myths. Dropping 1080p to 720p saves 112 and
costs you the thing people actually notice on a phone. Cut the seconds first.

## Run order

Steps 1-2 are already done and committed; their IDs are below.

1. **Host** — `soul_2`, prompt in `01-character.md`.
   Locked: `9024359d-0dd1-48a7-9665-e942806a4964`
   Never regenerate. This is the series' face.

2. **Board 1** — `gpt_image_2`, prompt in `02-boards.md`.
   Locked: `fdf7972f-04ee-4e2f-a23d-a288505bc67d`

3. **Boards 2-3** — sequential, not parallel. Board K takes board K-1 as a
   trailing reference image so the counter, the light and the guitar wall hold
   still across cuts. Submitting them in parallel breaks continuity.

4. **De-slop each board** — `seedream_v5_pro`, 21:9, 2k, the board's imported
   URL as `image_references`, using the preservation prompt in `02-boards.md`.
   Skip only under budget pressure; `gpt_image_2` board 1 came back with
   convincing skin texture unaided, so this is polish rather than rescue.

5. **Clips 1-3** — `seedance_2_5`, prompts in `03-clips.md`. Submit all three in
   one `generate_video_batch` call once every prompt is written. Native speech
   comes from `mode: "omni_reference"` + `generate_audio: true`; never make a
   separate audio call.

6. **QA before stitching.** Check evenly spaced frames plus 2-3 mid-word frames
   for: doubled lip edges, a third hand, face drift between cuts, wardrobe
   changes, baked-in text. Re-run only the failing clip index.

7. **Concat** — `ffmpeg -f concat -safe 0 -i clips.txt -c copy final.mp4`.
   Stream copy, hard cuts, no transitions.

8. **Burn the numbers** — red `#d63031` numerals on the counting beats, then the
   logo from `assets/dp-logo.png` in a corner. `ffmpeg drawtext` + `overlay`.
   Never bake text at generation time; it renders as gibberish and cannot be
   edited afterwards.

## The one thing that will bite you

`generate_video_batch` returns `submission_failed` rather than queuing when the
balance is short, and the failure names the workspace, not the shortfall. Always
`get_cost` a 15-second probe before submitting a batch of three — a batch that
half-submits leaves you paying for clips you cannot use.
