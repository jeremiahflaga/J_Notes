---
v-1.0.0: 2026-11-08 | Nov 11, 14 - listening only; Nov 18 - use AI to create summary
---

# How Bad Math Spread to Physics & Beyond - Steve Patterson (DemystifySci +451)

The DemystifySci Podcast: Drs. Anastasia Bendebury & Michael Shilo DeLay

https://www.youtube.com/watch?v=-W6qiRz5dLYc

Sep 15, 2026  DemystifySci Podcast

Today we're talking with philosopher Steve Patterson about how a lack of conceptual clarity in the foundations of 20th century mathematics led to problems not only downstream of this in physics, but eventually feeding irrationalist movements in diverse disciplines. From points with no size summing to lines, to sets of infinite quantities, formalism traded truth for usefulness, and that habit was transferred onto everyone from quantum physicists to economists. Ultimately, tolerating contradictions has made it easy for people to accept that our ability to reason is itself broken. We don't think so and propose some courses of action to mitigate the crisis.

00:00  Go! Why can physics calculate light but not explain it?
00:04:16 Who convinced us that reason is broken?
00:12:43 What gets lost when you turn the world into math?
00:20:01 Does math discover anything, or just refine it?
00:30:03 What happened when math lost its foundation?
00:37:17 How does anything move if every step can be halved?
00:47:03 Can a line be made of points with no size?
00:58:02 Does 0.999… really equal 1?
01:06:45 How did infinity get written into the rules?
01:15:22 What changes if we give up infinity?
01:24:23 Is reality smooth or pixelated?
01:34:52 Can a rule make anything happen?
01:45:37 What can you only see by zooming out?

---

12:40

Over the course of the 20th century, across many different domains, there has been a trend towards mathematization.

So in economics for example: economics of the 19th century is not heavily mathematical. Economics of the late 20th century is math. You have the massive  mathematization of economics, and I don't think that's to its credit.

Obviously something similar has happened in physics. You could describe it as a takeover of mathematics in physics, and it's not clear what the boundary is between mathematics and physics.

In biology you have I you have ideas about, let's say, the evolutionary process. How long does it take to um end up with new organisms with new genetics? Like how long is the process of mutation? How long does that take and how do we know?
It ends up being like a mathematical thing.

So across disciplines I think you end up with mathematization and I don't think that's a good thing.

14:20

So in order to actually like functionally do something with mathematics, you have to discard a ton of information because otherwise it's too complex to do math on. And so the more mathematical the the model, the more information is being discarded outside of it because otherwise you can't do it. And the assumption is, well that information we're discarding is irrelevant.

But it turns out that the information one is discarding in order to do math is not irrelevant. It turns out to be relevant in a bunch of different disciplines.


---

AI Summary, most of which I don't have an idea what they are, but I'm going to put them here anyway:

User: Please give a summary of [How Bad Math Spread to Physics & Beyond - Steve Patterson (DemystifySci +451)](https://www.youtube.com/watch?v=-W6qiRz5dLY)

Copilot: I'll fetch the video's details and transcript.

Fetched [https://www.youtube.com/watch?v=-W6qiRz5dLY](https://www.youtube.com/watch?v=-W6qiRz5dLY)
Completed with input: {"url":"https://www.youtube.com/watch?v=-W6qiRz5dLY"}

Ran terminal command: python --version; pip show youtube-transcript-api 2>$null | Select-Object -First 2
Tool execution failed with exit code 1

The page HTML isn't directly useful, so I'll pull the transcript with `youtube-transcript-api` in a scratch virtual environment.

Ran terminal command: python -m venv .venv; if ($?) { .\.venv\Scripts\python.exe -m pip install --quiet youtube-transcript-api yt-dlp 2>&1 | Select-Object -Last 5 }; .\.venv\Scripts\python.exe -m pip show youtube-transcript-api yt-dlp | Select-String "^(Name|Version)"

Tools installed. Now fetching the transcript and video metadata (title, description, chapters).

Ran terminal command: @'
import json, sys
from youtube_transcript_api import YouTubeTranscriptApi
vid = "-W6qiRz5dLY"
api = YouTubeTranscriptApi()
try:
    tl = api.list(vid)
    for t in tl:
        print("available:", t.language_code, t.language, "generated" if t.is_generated else "manual")
    fetched = api.fetch(vid, languages=["en", "en-US", "en-GB"])
    lines = []
    for s in fetched:
        m, sec = divmod(int(s.start), 60)
        h, m = divmod(m, 60)
        lines.append(f"[{h:d}:{m:02d}:{sec:02d}] {s.text}")
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("segments:", len(lines))
    print("last:", lines[-1])
except Exception as e:
    print("ERROR:", type(e).__name__, e)
'@ | .\.venv\Scripts\python.exe -

Ran terminal command: .\.venv\Scripts\python.exe -m yt_dlp --skip-download --no-warnings --print "TITLE: %(title)s" --print "CHANNEL: %(channel)s" --print "UPLOAD: %(upload_date)s" --print "DURATION: %(duration_string)s" --print "CHAPTERS: %(chapters)j" --print "DESC: %(description)s" "https://www.youtube.com/watch?v=-W6qiRz5dLY" 2>&1

Got the full auto-generated English transcript (~1h54m, 13 chapters). I'll condense it into timestamped paragraphs so I can read through it in full.

Ran terminal command: @'
import re
lines = open("transcript.txt", encoding="utf-8").read().splitlines()
out, buf, block_start = [], [], None
def ts_to_s(ts):
    h, m, s = map(int, ts.split(":")); return h*3600+m*60+s
for ln in lines:
    m = re.match(r"\[(\d+:\d\d:\d\d)\] (.*)", ln)
    if not m: continue
    ts, txt = m.groups()
    sec = ts_to_s(ts)
    if block_start is None: block_start = (ts, sec)
    buf.append(txt.replace("\n", " "))
    if sec - block_start[1] >= 90:
        out.append(f"[{block_start[0]}] " + " ".join(buf))
        buf, block_start = [], None
if buf: out.append(f"[{block_start[0]}] " + " ".join(buf))
txt = "\n\n".join(out)
open("transcript_condensed.txt", "w", encoding="utf-8").write(txt)
print("blocks:", len(out), "chars:", len(txt), "words:", len(txt.split()))
'@ | .\.venv\Scripts\python.exe -

The transcript is ~20.6k words. Reading it in parallel sections.

Read , lines 1 to 22
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    1,
    22
  ]
}

Read , lines 23 to 44
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    23,
    44
  ]
}

Read , lines 45 to 66
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    45,
    66
  ]
}

Read , lines 67 to 88
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    67,
    88
  ]
}

Read , lines 89 to 110
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    89,
    110
  ]
}

Read , lines 111 to 132
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    111,
    132
  ]
}

Read , lines 133 to 147
Completed with input: {
  "path": "[/..path../]\\transcript_condensed.txt",
  "view_range": [
    133,
    147
  ]
}

I've read the full transcript. Cleaning up the scratch files before summarizing.

Ran terminal command: $base = "[/..path../]"; Remove-Item -LiteralPath "$base\.venv" -Recurse -Force; Remove-Item -LiteralPath "$base\transcript.txt", "$base\transcript_condensed.txt" -Force; Get-ChildItem -LiteralPath $base -Force | Select-Object Name

# How Bad Math Spread to Physics & Beyond (DemystifySci #451)

**Hosts:** Shilo and Anastasia · **Guest:** philosopher Steve Patterson · **Length:** 1h54m

## Main argument
The hosts open with a puzzle: physics can calculate light precisely but can't say what light *is*. Patterson says the root of the problem is in mathematics, not physics.

- **His claim:** Around 1900, mathematics lost its conceptual footing. It accepted **completed infinities** (Cantor's infinite sets) and lines built from points that have no size. It then settled on **formalism**, which treats math as a game of symbols, the math version of "shut up and calculate."
- **How it spread:** Accepting contradictions because they're useful became a habit. It spread to physics, economics and other fields. It also fed the popular idea that reason itself is broken.
- **Patterson's verdict:** We've been in an intellectual "dark age" for over a century.

## Key segments
- **[4:16](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=256s) Who says reason is broken?** In college, Patterson kept hearing that reason can't be trusted. People backed this up with three things: quantum superposition, math (infinite sets and Gödel's theorems), and psychedelic experiences. His book *Square One* argues that a paradox means your thinking is wrong, not that reality contradicts itself.

- **[12:43](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=763s) What math throws away.** To use math, you have to leave out information. Patterson says the century's big mistake was assuming every field can do this as safely as physics and engineering can.
  - **Crypto example:** People used game theory, such as Schelling points, to claim authority over Bitcoin. Those models rely on unrealistic assumptions like perfect information.
  - **Hosts' pushback:** Math clearly works in engineering. Anastasia adds that math mostly *refines* inventions, while breakthroughs like the electric motor and PCR start as ideas.
  - **Patterson's reply:** Progress often came *despite* theory, as with the Wright brothers and LLM scaling. He separates **"low math"** (actual computation, which is real) from **"high math"** (the theories of roughly the last 120 years).

- **[30:03](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=1803s) The foundational crisis.** Non-Euclidean geometry removed Euclid as the base of mathematics. Three schools competed to replace him: logicists, intuitionists and formalists. Nobody won outright, so formalism took over by default. Patterson says this matters because math used to claim to be true. Its loss of truth is now used to argue that nothing can be known, not even 2+2=4.

- **[37:17](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=2237s) Zeno, points, and 0.999….**
  - **Zeno:** Calculus shows a runner getting closer and closer to the finish line, but not actually crossing it.
  - **Points:** "An infinite number of zeros doesn't get you a one," so he thinks points should be treated as pixels.
  - **Calculus:** Computers do calculus without any infinite process, so the discrete version is the "real" calculus.
  - **0.999… = 1:** All three say this is *logically* false: 0.999… gets close to 1 but isn't the same number. Patterson concludes that "proven" math can be wrong.

- **[1:06:45](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=4005s) How infinity got into the rules.** Patterson draws on Norman Wildberger and Morris Kline. Mathematicians used to separate an infinity that never ends from a completed one. Cantor removed that distinction, and it became part of the standard axioms (ZFC's axiom of infinity). Patterson calls Cantor's claim that the idea came from God a red flag.

- **[1:15:22](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=4522s) Is the universe discrete?** Patterson doesn't know what dropping infinity would break or open up. He notes that some economic models flip their results depending on whether they're continuous or discrete. Shilo notes that infinities appearing in physics models have always signaled a flaw.
  - **Main disagreement:** Patterson imagines a "Minecraft" universe of real blocks of space that switch states.
  - **Hosts' view:** Location is an abstraction, not a physical thing. Reality needs both discrete and continuous parts.

- **[1:34:52](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=5692s) Can a rule cause anything?** Patterson proposes a **"universal function"** that takes the state of everything and produces the next state. He says this also solves the mind–body problem and is "a pretty dang good definition of God." The hosts compare it to Wolfram's ruliad: a good map, but with no mechanism. In their view, rules only describe, and physical bodies do the causing.

- **[1:45:37](https://www.youtube.com/watch?v=-W6qiRz5dLY&t=6337s) Zooming out.** Science has spent centuries zooming in. Patterson thinks some answers only appear when you zoom out. Everyone agrees that number-based and non-number-based reasoning need to work together. His closing point: in complex fields like biology or politics, more math may mean *less* sophistication.

## Closing
Patterson promotes his new **Natural Philosophy Institute**. It is compiling a list of widely held ideas he's confident are wrong, such as the Copenhagen interpretation and how umbilical cords are clamped at birth.

## Worth knowing
- Patterson calls his own views "heretical." In standard mathematics, 0.999… is defined as the limit of 0.9, 0.99, 0.999 and so on, which is exactly 1.
- He wasn't sure about some quotes. The "set theory is a disease" line is usually attributed to Poincaré, not Wittgenstein.
- Gödel comes up in the intro but is barely discussed.
- This summary is based on YouTube's auto-generated transcript.


Claude Opus 5.5 • 83.2 credits
