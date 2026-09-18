# Handoff

A self-contained packet for giving this series to someone else — another
producer, another agency, or another AI.

**The packet's build target is EP02.** EP01 is already produced, so handing over
instructions to rebuild it would have bought nothing; instead EP01 ships inside
the packet as the *reference build* — the finished video, its boards, its raw
contact sheets and its post-production notes — and the instructions point at the
next episode.

## What is here

| File | What it is |
|---|---|
| `START-HERE.md` | The brief. Host spec, set spec, claim allowlist, EP02's script and structure, the eight clip rules, the graphics changes, and every trap already paid for. Written for a reader with no context at all. |
| `conversation.md` | The complete client conversation, 136 turns, verbatim. Tool calls and shell plumbing stripped; everything either party actually said is intact. |
| `make-packet.sh` | Rebuilds the distributable zip from tracked repo files. |

The episode prompts themselves live in `content/prompts/`, not here — the packet
copies them in. Episode-specific files are named `epNN-*`; `00-runbook.md` and
`01-character.md` are series-wide.

## Building the zip

```bash
content/handoff/make-packet.sh     # -> dist/dicks-pawn-handoff-packet.zip
```

Needs `ffmpeg` and ImageMagick's `convert`. Neither is installed in the dev
container; the real run happened in the Higgsfield sandbox, which has both.

The zip is **not committed**. It is ~11 MB and every byte is derived from files
already tracked here, so versioning it would duplicate the repo. The script is
the artifact; the zip is its output.

## Why the packet compresses the images

`content/reference/` holds the store photos and the host plate as PNGs — about
30 MB together. At 1800px JPEG q86 they come to 2.1 MB and lose nothing that
matters for a reference image. The video ships as a 720p cut of the delivered
master for the same reason: 27.2 MB → 5.4 MB, and the recipient is watching it
to understand the target, not to post it.

## What the packet deliberately does not solve

The video was generated on Seedance 2.5, which produces native synchronised
speech from a text prompt. Most other stacks do not. `START-HERE.md` says so in
its first section rather than burying it, because a recipient who discovers it at
assembly time has already spent the money.

Everything else — the prompts, the eight-beat structure, the claim rules, the
post-production spec — ports to any toolchain unchanged.

## Retargeting the packet at a later episode

EP03–EP05 are scripted in the series bible. To point the packet at one of them:

1. Write `content/prompts/epNN-boards.md` and `epNN-clips.md` against the bible
   script, following `ep02-*` as the model.
2. Write `epNN-graphics.md` only if the burn actually changes. EP02 needed one
   because its script counts with bare ordinals rather than "Number one", which
   breaks `burn.py`'s cue detector outright — that will not be true of every
   episode. Check before assuming.
3. Update §6, §7 and §11 of `START-HERE.md`, and the glob in `make-packet.sh`.

The host, the set, the claim allowlist and the traps section carry over
untouched. That is the point of them.
