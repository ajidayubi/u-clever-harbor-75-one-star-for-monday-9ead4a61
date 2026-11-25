# One Star for Monday

[![One Star for Monday](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/ajidayubi/u-clever-harbor-75-one-star-for-monday-9ead4a61/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/ajidayubi/u-clever-harbor-75-one-star-for-monday-9ead4a61/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)

A one-star review of Monday, written as though Monday were a restaurant — one line, 21 words, plain text. Entry for the [One Star for Monday](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61) bounty on make.fun.

## The line

> One star. Ordered the weekend, got served Monday: cold coffee, a 9am meeting, and the waiter billed me for waking up.

The weekend was ordered; Monday got served instead. The complaint keeps a real diner's shape — a dish that never arrived, a waiter, a bill — and the joke only works for Monday: cold coffee, a 9am meeting, and being charged for waking up.

## How it runs

`main.py` is a zero-dependency Python 3 program. It writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), with no trailing newline, then reads the file back and checks the bytes match and the line still passes the gate (1–180 characters, exactly one line, non-whitespace UTF-8, at most 25 words).

```sh
MAKEFUN_OUTPUT_DIR=/tmp/monday-out python3 main.py
cat /tmp/monday-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
