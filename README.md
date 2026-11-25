# Duskline Lights Out

[![make.fun · u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Sesshomaru-9/duskline-lights-out/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Sesshomaru-9/duskline-lights-out/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

A single line spoken by a laptop whose lid has just snapped shut, while its
chat reply is still stuck on "typing". Entry for the make.fun bounty
[One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e).

## The line

> The lid clicked shut at 23:41. My reply still says 'typing'. It will say that all night.

88 characters, one line. The machine is closed and the conversation is
finished, yet the typing indicator never got the news — it will sit there
blinking "typing…" until morning, mid-sentence forever, with nobody left on
either side of the lid to complete it. 23:41 is the hinge: late enough that
closing the lid is final, early enough that the indicator still has the whole
night in front of it.

## What the code does

`main.py` (Python 3.13, standard library only, deterministic, no network)
builds the line from its three beats, checks it against the bounty gate
(1–200 characters, valid UTF-8, not blank), then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and reads it back to make sure the bytes
match what was written.

Guard rail: when the resolved output directory is the repository directory
itself (or anywhere inside it), the program writes nothing and exits 0. When
`$MAKEFUN_OUTPUT_DIR` is not set, it falls back to a fresh temporary
directory. The program never raises an exception: any failure exits 0
without writing a file.

## Try it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
