---
v-1.0.0: 2026-08-22 | 
---

# APPENDIX 1: Demystifying Large Language Models

For better or worse, large language models (**LLMs**) have become almost synonymous
with **AI**, even though they’re the **newest arrivals** in the field. Among
all technologies built on **neural networks**, they are the ones that have changed
our daily lives the most.

how it works

When
we know how they “think,” we can guide them better and get more reliable
results.

## Attention Is All You Need

Since the landmark 2017 paper “Attention Is All You Need,”1 natural language
processing using large models has exploded.

1. https://arxiv.org/abs/1706.03762


## What Are Large Language Models?

An LLM is a **type of neural network** designed to generate human-like text. It’s
built primarily on the **Transformer architecture** (by the way, GPT stands for
Generative Pretrained Transformer), which enables it to process and predict
words based on their context.

Unlike traditional
rule-based systems, LLMs don’t “understand” language in a human way—they
**predict the most likely next words** in a sequence based on a given prompt
and then choose one, often **the most probable but not always**.

Wrong responses are often called **hallucinations**, but in reality, **every response**
they generate is a kind of hallucination; it’s just that we can recognize some
as correct and others as incorrect, based on our understanding of reality.

You can’t download commercial models like ChatGPT or Claude, but many
**freely available models** are on sites like **ollama.com** or **huggingface.com**.


### Llama 3.3 Details

When we give an LLM a question, the first step is splitting our text into
**tokens** — small chunks, often one or two per word. Each token is then mapped
to a list of numbers called an **embedding**. You can think of an embedding as
the token’s “coordinates” in a huge, invisible space. Tokens with similar
meanings are close together in that space, even if they don’t look alike as
words.

From here, the model starts looking at each token in the context and comparing
it to all the others. This is the **attention mechanism**. It’s like being in a
meeting and deciding, for each sentence, which other sentences are important
to keep in mind before you respond. The model does this for every token, at
every step, constantly adjusting what it “pays attention to” as it builds the
response.

After attention, the model applies a series of mathematical **transformations**
(projections and other operations) to produce new matrices...

In the **final layer**, the model produces a list of probabilities for every possible
next token. Then it picks one.

If it always picked the single most probable token, the output would quickly
become dull and repetitive. To avoid this, LLMs introduce **randomness**, controlled
by a parameter called **temperature**. A temperature of 0 means fully
deterministic output—always the most likely choice.

### Magic Numbers?


## Vector Databases

(Retrieval-Augmented Generation (RAG) mentioned)


## Considerations

First... LLMs need **constant reminders** of relevant
information.

Second... they generate text based on both their training data and the provided
context — which, initially, is just our prompt

Finally, LLMs excel at **recognizing and generalizing patterns**, which is why
they’re so powerful... 
However,
this same ability makes them prone to **hallucinations**, like assuming a Ruby
library exists in Java by adding a “4j” suffix.

Unless a groundbreaking new algorithm is discovered, these considerations
should hold true for future models as well.