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
| Video clip | `seedance_2_0_mini` | 9:16, 720p, 15s | **37.50** |
| Video clip | `seedance_2_0_mini` | 9:16, 480p, 15s | **15.00** |
| Video clip | `seedance_2_0` (fast) | 9:16, 720p, 15s | **52.50** |
| Video clip | `seedance_2_0` (std) | 9:16, 1080p, 15s | **165.00** |

Seedance is billed **per second of output**, and resolution is the multiplier:

| Model + resolution | Credits/sec | Full 45s episode |
|---|---|---|
| `seedance_2_0_mini` 480p | 1.0 | **45** |
| `seedance_2_0_mini` 720p | 2.5 | **112.5** |
| `seedance_2_5` 480p | 3.0 | 135 |
| `seedance_2_0` fast 720p | 3.5 | 157.5 |
| `seedance_2_5` 720p | 6.5 | 292.5 |
| `seedance_2_5` 1080p | 9.0 | 405 |
| `seedance_2_0` std 1080p | 11.0 | 495 |

**Pick the model before you pick the resolution.** Seedance 2.0 Mini at 720p
costs less per second than Seedance 2.5 does at 480p — it is cheaper *and*
higher resolution. A whole 45-second episode on Mini at 720p (112.5) costs less
than a single 15-second Seedance 2.5 clip at 1080p (135).

The catch is that Mini is a budget model and its output quality here is
**unverified** — the 5-second motion test validated `seedance_2_5`, not Mini.
Lip-sync and identity hold are exactly the things a cheaper model degrades
first, and they are the two things this format cannot survive losing. Spend 15
credits on one Mini clip and compare it against `content/output/` before
committing an episode to it.

### Porting a clip prompt from 2.5 to 2.0 Mini

The prompt text carries over unchanged. The params do not:

| 2.5 | 2.0 Mini |
|---|---|
| `mode: "omni_reference"` | *(no `mode` param — remove it)* |
| `medias[].role: "image"` | `image_references` |
| `resolution: "1080p"` | 480p / 720p only |
| `duration` up to 30 | 4-15 |

`generate_audio: true` is the default on both. Mini and `seedance_2_0` also
carry `supports_unlim`, which `seedance_2_5` does not — so if a free-trial
unlimited allowance ever applies to this account, it applies to these models and
never to 2.5.

**Video is ~95% of the budget.** Images are rounding error. Every cost decision
in this series is a decision about seconds of video, not about image quality.

## Cost per episode

| Build | Boards | Clips | Total |
|---|---|---|---|
| 45s, Mini @ 480p | 19.5 | 45 | **~65** |
| 45s, Mini @ 720p | 19.5 | 112.5 | **~132** |
| 45s, 2.5 @ 480p | 19.5 | 135 | **~155** |
| 30s, 2.5 @ 1080p (2 clips) | 13.0 | 270 | **~283** |
| 45s, 2.5 @ 720p | 19.5 | 292.5 | **~312** |
| 45s, 2.5 @ 1080p (the spec) | 19.5 | 405 | **~425** |

A 500-credit pack covers one full 45s episode at 1080p on Seedance 2.5 — or
roughly **four** episodes at 720p on Mini.

**Levers in order of value: model, then duration, then resolution.** Switching
2.5 → Mini at the same 720p saves 60% with an unknown quality cost. Dropping 45s
to 30s saves a third and costs you two myths. Dropping resolution saves the
least and costs the thing people actually notice on a phone.

## Run order

**EP01 is fully produced.** Every step below was run; the locked IDs are here so
EP02-05 reuse the same host and the same proven parameters.

1. **Host** — `soul_2`, prompt in `01-character.md`.
   Locked: `9024359d-0dd1-48a7-9665-e942806a4964`
   Never regenerate. This is the series' face.

2. **Boards 1-3** — `gpt_image_2`, prompts in `02-boards.md`.
   Locked: board 1 `fdf7972f-04ee-4e2f-a23d-a288505bc67d`,
   board 2 `18a1eb71-8a34-485e-b7c4-b4eeb723fc7d`,
   board 3 `bb0e989e-47fc-4733-9e8c-d88e60fb595c`

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

## Three things that will bite you

**A preset can intercept your submission.** `generate_video_batch` may return
`submission_failed` saying a preset "was recommended instead of submitting a
job" — no job is created and nothing is charged. This run got offered a preset
called "IN THE DARK", which would have thrown a moody night grade over a bright
daylight pawn shop. Retry the same index with `declined_preset_id` set to the id
in the error. Never accept a preset you did not choose; it silently overrides
the whole Style & Mood block.

**Media roles get coerced.** Seedance 2.5 takes `role: "image"` and rewrites it
to `image_references`, reporting the swap in `adjustments`. Harmless, but it
means the role you write is not always the role that runs — read `adjustments`
on every submission rather than assuming your params went through verbatim.

## The one thing that will bite you

`generate_video_batch` returns `submission_failed` rather than queuing when the
balance is short, and the failure names the workspace, not the shortfall. Always
`get_cost` a 15-second probe before submitting a batch of three — a batch that
half-submits leaves you paying for clips you cannot use.
