---
v-1.0.0: 2026-11-05 | and Nov 6, read the chapter only; did not do the hands-on exercises
---

# CHAPTER 1: HeLLMo, World!

Throughout this book, we’ll use LLMs from OpenAI.

“OpenAI API”

you’ll need to purchase API credits

API key


## Creating Our First App

I’ll use the uv Python library to manage dependencies for the projects in this
book




Another important parameter here is the **temperature**, a concept that will be
explained at length in Gauging the Temperature, on page 20.

What you should know for now is that the greater the temperature, the more
unpredictable the LLM’s output.

We’ve therefore set the temperature in our code to 0, which is common among
apps that dispense facts.


## Tweaking the Model and Temperature

### Trying a Different Model

### Model Snapshots

when providers update models, they do so for the purpose of
making the model better. But given an LLM’s unpredictable nature, it’s possible
that an update can make the model worse for your specific application.

LLM providers typically provide different
versions of each model - "snapshot"

GPT-4o model
- gpt-4o-2024-11-21
- gpt-4o-2024-08-06

### Changing the Temperature

tokens - for now think of them as roughly equivalent to words

max_output_tokens


## Checking API Usage

**Input tokens** are the text I send to the LLM via
prompts, while **output tokens** are the text that the LLM generates in response.
LLM providers charge for **both**







