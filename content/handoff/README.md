# Handoff

A self-contained packet for giving this series to someone else — another
producer, another agency, or another AI. Built because the client asked for
everything needed to rebuild EP01 on a different toolchain.

## What is here

| File | What it is |
|---|---|
| `START-HERE.md` | The brief. Host spec, set spec, claim allowlist, script, beat structure, graphics spec, and every trap already paid for. Written to be read by someone with no context at all. |
| `conversation.md` | The complete client conversation, 136 turns, verbatim. Tool calls and shell plumbing stripped; everything either party actually said is intact. |
| `make-packet.sh` | Rebuilds the distributable zip from tracked repo files. |

## Building the zip

```bash
content/handoff/make-packet.sh     # -> dist/dicks-pawn-handoff-packet.zip
```

Needs `ffmpeg` and ImageMagick's `convert`. Neither is installed in the dev
container; the real run happened in the Higgsfield sandbox, which has both.

The zip is **not committed**. It is ~11 MB and every byte of it is derived from
files already tracked here, so versioning it would just duplicate the repo. The
script is the artifact; the zip is its output.

## Why the packet compresses the images

`content/reference/` holds the store photos and the host plate as PNGs — about
30 MB together. At 1800px JPEG q86 they come to 2.1 MB and lose nothing that
matters for a reference image. The video ships as a 720p cut of the delivered
master for the same reason: 27.2 MB → 5.4 MB, and the recipient is watching it
to understand the target, not to post it.

## What the packet deliberately does not solve

The video in this series was generated on Seedance 2.5, which produces native
synchronised speech from a text prompt. Most other stacks do not. `START-HERE.md`
says so in its first section rather than burying it, because a recipient who
discovers it at assembly time has already spent the money.

Everything else — the prompts, the eight-beat structure, the claim rules, the
post-production spec — ports to any toolchain unchanged.
