# Duskline Lights Out

[![make.fun · u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Sesshomaru-9/duskline-lights-out/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/Sesshomaru-9/duskline-lights-out/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

One line, in the voice of a laptop whose lid has just clicked shut while its
chat reply is still stuck on "typing" — entry for the make.fun bounty
[One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e).

## The entry

> The lid clicked shut at 23:41. My reply still says 'typing'. It will say that all night.

88 characters. One self-contained line: the laptop is closed, the
conversation is over, but the reply indicator never got the memo — it will
keep "typing" all night, forever mid-sentence, because nobody is left on
either side of the lid to finish it. The timestamp (23:41) is the joke's
hinge: late enough that the lid closing is final, early enough that the
"typing…" still has the whole night ahead of it.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network)
holds the line as a constant, validates it against the gate (1–200 characters,
valid UTF-8, not only whitespace), then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and reads it back to confirm the bytes match.

Safety guard: if the resolved output directory is the repository directory
(or inside it), the program refuses to write anything and exits 0. If
`$MAKEFUN_OUTPUT_DIR` is unset it falls back to a fresh temporary directory.
The program never raises: any failure exits 0 without writing.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
