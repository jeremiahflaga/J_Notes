---
v-1.0.0: 2026-08-21 | 
---

# Preface

We’re living in a truly exciting moment. For the first time in history, software
can answer questions, write code, and hold conversations that feel almost
human. After chatting with one of them for a while, it’s easy to feel like they
are reasoning or understanding in a human way.

And yet, at heart, these new AI models are just **ultra-sophisticated autocomplete machines**. This isn’t to downplay what they can do. It’s simply to
point out that, in a literal sense, they work by **predicting what will be the next word, based on the text that came before**.

a deep analysis shows that their reasoning is a **mirage**.1

1. https://arxiv.org/pdf/2508.01191


And just like when working with humans,
how clearly we communicate makes a huge difference in what they produce.
Clarity, structure, and readable prompts lead to better output.

What excites me most about their arrival is how much easier and faster it
has become to apply **good engineering practices**. Techniques like TDD, modular
design, and merciless refactoring were once dismissed as too slow for
“real development.” Now, with AI, they’ve become often the **safest and fastest**
way to build and evolve software.


## Why This Book

This book is **not** about **artificial general intelligence (AGI)** or philosophical debates.

With the right guidance from us, LLMs can produce clean, maintainable code
that fits into long-term projects. They’re not replacing developers anytime
soon, but they can dramatically speed up the work. That makes them a tool
every developer should learn to use well.

Alas, **there’s no magic prompt shortcut**. Getting good results isn’t about clever
one-liners. It’s about following a **solid, iterative process, step by step**, just like
we would when debugging a tricky issue or refactoring a tangled module.

Everything I share in this book comes from real-world experience—places
where LLMs **saved hours** of work and others where they completely **failed**.

And finally, we’re still just getting started. AI-assisted coding is in its early
days. Best practices are still evolving. The goal of this book isn’t to lock in
fixed rules but to give you the **mindset and tools** to keep learning as the field
grows.


## Who This Book Is For


## How This Book Is Structured

An appendix then follows where we peek under the hood of LLMs. You’ll get
a simple, practical explanation of how their interference and attention
mechanisms work, so you can understand how to better guide and control
them. Some readers may prefer to start there to build a bit of **background**
before reading the rest of the book. Others may want to jump straight to the
more hands-on parts and come back to the appendix only when they feel the
need.

At the end of the book, just before the appendix, you’ll find a one-page manual.
It gathers the most important techniques from the book onto a single
page you can print and keep handy as a quick reference.

### Screencast Sessions

A big part of this book comes from real coding sessions with AI assistants.
In those sessions, the AI wrote all the code, and my role is to act as your
guide. At the start of each session, you’ll find a **link to the full screen recording**, the total duration, and a link to the **Git repository**.

Across the sessions, we’ll work with three different programming languages:
Python, Elixir, and Kotlin, and different AI tools and IDE (in strictly alphabetical
order): ChatGPT, Claude Code, Codex, Cursor, IntelliJ Junie, and Windsurf.

You can find all the videos in the book YouTube channel. 2

2. https://www.youtube.com/@ProcessOverMagic


we’ve set up a collection of online
resources on the book’s companion site. 3

3. https://pragprog.com/titles/ubaidev/process-over-magic-beyond-vibe-coding/


You can also contact me here:
• Uberto’s blog 4
• Bluesky: @ramtop.bsky.social
• Linkedin 5

4. https://medium.com/@ramtop
5. https://www.linkedin.com/in/uberto/