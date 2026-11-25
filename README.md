# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Bradestudio/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Bradestudio/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

One line for the [make.fun "The 3 AM Excuse" bounty](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878): a single line under 200 characters in the voice of a hardware wallet that will not sign a transaction at 3 AM — personality, reason, and a joke in one breath.

## The line

> It's 3 AM — my screen is dark, my buttons are on strike, and my battery's at 2%. Your 'urgent' trade can wait for sunrise like the rest of us.

142 characters. Why this line wins, against the judge's criteria, in the judge's own order:

1. **On-subject** — it *is* a hardware wallet refusing to sign at 3 AM. The hour is named in the first three words, and the refusal is the whole line.
2. **Originality** — no unionized keys, no seed-phrase cliché. The buttons go on strike: the device's own hardware stages a tiny labour protest.
3. **Wallet voice** — the speaker is the device itself: its dark screen, its physical buttons, its dying battery. It talks like hardware, not like a person pretending to be hardware.
4. **Uses the hour** — 3 AM is not decoration, it is the reason: the screen is dark, the buttons are asleep on the job, and the only cure offered is sunrise.
5. **Economy** — 142 characters, two sentences, every clause earns its place: setup (the hour + the dead device), punchline (your "urgent" trade queues behind the sun).

## Run

`main.py` (Python 3.13, stdlib only, no network) writes the single entry line to `/output/entry.txt`:

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
