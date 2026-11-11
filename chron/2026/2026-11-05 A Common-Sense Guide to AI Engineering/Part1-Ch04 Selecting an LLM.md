---
v-1.0.0: 2026-11-11 | 
---

# CHAPTER 4: Selecting an LLM

Generally speaking, there are three
options for obtaining an LLM:

1. Build an LLM from scratch
2. Host an open source LLM
3. Use an LLM-as-a-service

(Build a Large Language Model from Scratch by Sebastian Raschka.)

open source vs open weight

Ollama - open source LLM

MLOps, short for machine learning operations

GPUs, or graphics processing units

In most cases, you don’t need to fine-tune an LLM to get it to do
what you want. The techniques you’ll learn in this book are highly
effective and are likely all you’ll need. As such, this book will not
cover the details of **fine-tuning**.

6. https://commonsensedev.com/fine-tuning-pros-cons

7. https://commonsensedev.com/fine-tuning-intro


### Comparing Different LLMs

### Hard Constraints

### Quality, Cost, and Latency

The Trade-Off Trifecta

### Context Window

### Reasoning Models

Reasoning models have
been optimized to excel at breaking down complex problems into simpler
steps in order to solve them. The term “complex” here doesn’t have a strict
definition but generally refers to a problem that is more easily solved by
breaking it down into **smaller, logical steps**.

I want to emphasize that **the term “reasoning” is misleading**, since even reasoning
LLMs are still just SNWPs and don’t actually reason. They’ve just been
optimized using various techniques to help them generate tokens that **increase the likelihood that they’ll stumble upon** a better response.

8. https://commonsensedev.com/reasoning

slower and more expensive

they sometimes underperform nonreasoning models when it
comes to simple prompts, since reasoning models may **“overthink”** the simple
problem.



## Deciding on an LLM

If you search the web for “LLM Leaderboards,” you’ll find websites (such as
this9 one) that provide a lot of interesting information about various LLMs.

9. https://commonsensedev.com/leaderboard

