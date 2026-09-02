---
v-1.0.0: 2026-08-29 | 
---

# CHAPTER 5: Collaborating Inside an AI-Powered Team


## Adopting AI

When it comes to bringing AI into a team, we should **support it but not force it**. Not everyone is ready to accept change at the same time, and that’s fine.

`personal_rules.md`

### Training for New Tools


## Team Organization

when coding gets much faster, it won’t speed up the whole team.
It will simply highlight everything else that’s in the way. The **theory of constraints**
makes this clear: improving something that’s not the bottleneck can
slow the entire system down, because the real bottleneck becomes even more
congested.

(JBOY: The Goal by Eliyahu Goldratt)


Interestingly, this is reflected in real data. Several studies—including the
DORA reports1—have found no significant improvement in overall team productivity
after adopting AI tools.

1. https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report

### Hiring

LLMs are superhuman at solving algorithmic
problems—the kind often used in traditional interviews.

We need interview processes that can’t be gamed by LLMs. Instead of asking
people to write code in a vacuum, we should assess how they work with AI.
Can they break down a feature into clear, manageable steps? Can they review
and improve generated code, spotting issues when they’re present and
knowing when to push back or try a different approach?

And since LLMs can instantly fill in many technical gaps, traditional filters
like “years of experience with X” start to matter a lot less. What we should be
looking for are people who can think holistically about the product, communicate
well, and make good technical decisions in context.

### Onboarding and Code Review

### AI and Developer Well-Being


## Security Risks

Probably the first widely known example came from Samsung in 2023, when
engineers accidentally uploaded proprietary source code and chip designs to
ChatGPT while debugging.

• Subtle vulnerabilities in generated code: LLMs generate code quickly, but
not always safely. A 2025 study across more than 100 models found that
only 55 percent of AI-generated code was secure.6

6. https://www.veracode.com/blog/ai-generated-code-security-risks/

attackers have started publishing malicious libraries using
names that are commonly hallucinated by LLMs—for instance, a fake package
with a name like http_helpers or string_utils, hosted on public repositories like
npm, PyPI, or Maven Central. These packages just sit there, waiting to be
picked up by vibe-coded applications that trust the assistant blindly.



#### The Lethal Trifecta

Simon Willison describes what he calls the lethal trifecta for AI agents:

• private data,
• untrusted content, and
• external communication.