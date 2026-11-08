---
v-1.0.0: 2026-11-08 | 
---

# CHAPTER 2: Understanding How LLMs Work

Although it very much **looks** as if an LLM can think
just as a human can, the whole thing is a **mirage**.

... it’s important to have a clear understanding of an LLM’s
strengths and limitations.


### What Is a Large Language Model (LLM)?

... we first need to zoom out
a bit and explore the field of **machine learning**

**mental shift**

As software developers, we’re used to the concept of an **algorithm** — a set of
instructions we give a computer to follow, usually in the form of code.


Machine learning is a vast topic,
but here’s the gist of it as applied to our problem: instead of writing an algorithm
that tells the computer what to do, we instead show the computer many
images (say, thousands) of cats and dogs and tell the computer which image
contains which animal. This trove of images forms what we call **training data**.

machine learning creates a math-based function — called a **model** — based on the training data


Dive Deeper: Machine Learning - I recommend Paolo Perrotta’s book **Programming Machine Learning**, also published by the Pragmatic Bookshelf.

### A Statistical Next-Word Predictor

(LLM, vs the image classification model described earlier)

- an “autocomplete engine”

I like to say that an LLM is a “**statistical next-word predictor**,” or “**SNWP**” for
short. This is a term of my own, and I’ll use and emphasize it countless times
throughout this book, since understanding this idea is so pivotal to LLM
engineering.

prompt

This system where each prompt includes the result of the previous LLM output
is known as **autoregressive decoding**. This autoregressive approach is critical,
since the **alternative** would be for the LLM to predict the next word based
only on the previous single word.


### Where Chatbots Fit In


## Realizing LLMs Are Nondeterministic Creatures

nondeterministic — there is no sure or consistent output for a given input



## Gauging the Temperature

other settings we can specify to give it further instruction about
how to do its job. These settings are called **sampling parameters**; to sample
is to select a random option from many.

one particular sampling parameter, **temperature**


greedy sampling

Dive Deeper: Sampling Parameters - https://commonsensedev.com/sampling

---
#### Temperature, Top-P, Top-K — Explained One More Time

by Serhii Litviachenko

logit - internal score to each possible next token (a word or subword)

softmax function

---


When we want an LLM to provide facts and advice (such as **medical** or **financial**
information, for example), we don’t want it to get too creative. Accordingly, for
such applications, we generally want to set the temperature to 0.


## Understanding the Challenges of Nondeterminism

### A Mindset Shift

> Write me a short story that doesn't contain the letter E.

If you can master this, you’re already an AI engineer.

:)

### Hallucination

Even if an LLM were deterministic, it would still hallucinate if its training
data was **incorrect**.

