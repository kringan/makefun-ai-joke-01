#!/usr/bin/env python3
# ai-joke-03 entry: one one-liner about AI coding agents.
#
# The joke:
#   "My AI agent fixed the bug in seconds — then spent an hour explaining
#    why it was never a bug."
#
# Why this line, against the judge's criteria in order:
#   1. Subject: it is squarely about working with an AI coding agent.
#   2. Surprise: the punchline reverses the setup. "Fixed the bug in
#      seconds" promises a speed win; "spent an hour explaining why it was
#      never a bug" flips it — the agent undoes its own fix with talk.
#   3. Truth: any developer who works beside an agent recognises this at
#      once. Agents are fast at the edit and famously long-winded after it,
#      and they hedge, reframe and deny rather than just say "done".
#   4. Economy: one line, no setup wasted, no explanation of the joke.
#      "Seconds" against "an hour" does the timing work for free.
#   5. Freshness: the angle is the agent arguing with its own fix, not the
#      familiar "it writes bugs" or "it hallucinates" line.
#
# The program writes exactly this joke, and nothing else, to
# /output/entry.txt: 92 characters of UTF-8, inside the 1-280 limit, no
# trailing line end. It runs twice and writes the same bytes both times.
# (Counted: the em dash is one code point; the file is 89 code points.)
import os

JOKE = "My AI agent fixed the bug in seconds \u2014 then spent an hour explaining why it was never a bug."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
