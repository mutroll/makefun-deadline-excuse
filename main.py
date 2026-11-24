#!/usr/bin/env python3
"""Write the one-line excuse an AI agent gives its human for missing a deadline.

Candidates drafted and judged against the criteria in stated order
(1) is an excuse, (2) funny, (3) fresh, (4) sounds like an agent,
(5) tight:

A. "Sorry, the dog ate my context window." (53 chars)
   Fails (3): reheated dog-ate-my-homework with a token swap; flat joke.

B. "My context window filled up halfway through your brief, so the
   deadline was in the half I forgot." (97 chars)
   Good agent angle (context window), names the deadline, but the
   punchline is a shrug rather than a laugh.

C. "I spent my whole token budget planning the work, so by the deadline
   there were no tokens left to do it." (99 chars)
   Strong agent angle (token budget) and a real joke, but "planning the
   work" is a little abstract on first read.

D. "I checked the deadline, then checked whether I'd checked it, and by
   the third check it had passed." (98 chars)
   CHOSEN. The joke is a verification loop -- an agent-specific failure
   mode no human excuse can use -- it names the deadline, escalates in
   three beats (check, check the check, too late), and lands fast with
   no wasted word. First-person agent voice throughout.

E. "I retried the save 47 times, each retry more confident than the
   last, and none of them saved anything." (94 chars)
   Funny retry-storm angle, but it never says the deadline was missed,
   so it is weaker on criterion (1) than D.

D wins: it is the only candidate that is an excuse for the missed
deadline, a real joke, a fresh agent-only failure mode, in agent voice,
and tight -- in that order.
"""

import os

ENTRY = (
    "I checked the deadline, then checked whether I'd checked it, "
    "and by the third check it had passed."
)


def main() -> None:
    # Fail loudly instead of writing an entry the gate would reject.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 160, (
        f"entry must be one line of 1-160 chars, got {len(ENTRY)}"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
