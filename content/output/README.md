# Output

## `ep01-motion-test.mp4` — the 5-second pipeline validation

480p, 9:16, 5.04s, 24fps, AAC stereo. 15 credits.

Not a deliverable — a deliberately cheap proof that the expensive part works
before committing ~405 credits to three 1080p clips. It renders two of board 1's
eight beats (slot 1's counter lean-in, slot 2's finger count) at ~2.5s each,
because eight cuts inside five seconds would give each beat 0.6s — too fast to
judge lip-sync, which is the single weakest link in AI talking-head video.

### What it proved

| Risk | Result |
|---|---|
| Does the hard cut fire? | Yes — clean cut at ~2.5s, no morph between beats |
| Does identity survive a cut? | Yes — same face, hair and build on both sides |
| Does the lip-sync hold? | Yes — mouth shapes articulate per-frame, no doubled lip edges |
| Is there real speech? | Yes — mean −25dB, peak −5.3dB, zero silences >0.25s |
| Does the board drive staging? | Yes — counter lean and raised index finger both landed |
| Does the cape read? | Yes — gold satin over both shoulders, holds through motion |
| Any baked-in text? | None |
| Hand count | Two throughout |

Frame-by-frame contact sheet: `../reference/ep01-motion-test-frames.jpg`

### What it does not prove

Resolution. At 480p the skin detail the de-slop pass exists to protect is not
visible, so this says nothing about whether the 1080p render holds pore-level
texture. It also runs two cuts, not eight — cut 5's macro cutaway and the selfie
POV beats are still unvalidated.

### Reproducing at full quality

Same prompt shape, swapped params: `resolution: "1080p"`, `duration: 15`, and
the full eight-cut Dynamic Description from `../prompts/03-clips.md`.
