---
v-1.0.0: 2026-08-23 | and Aug 28
---

# CHAPTER 4: Working on a Large Codebase

This chapter is all about practical techniques for everyday tasks: making safe
code changes, refactoring small parts without breaking everything, and
speeding up the tedious but important work.


## Managing Technical Debt


## Understanding Legacy Code


## Enhancing Big Code Projects with AI

Alberto Brandolini once expressed that it is the developer’s understanding,
not the domain expert’s knowledge that becomes production code

(JBOY: Scott Wlaschin also said something like that in Domain Modeling Made Functional)

in my experience, the single biggest benefit of using AI
assistants is the ability to answer questions about the codebase—for example,
locating the function that determines a certain behavior, understanding why
it behaves that way, or figuring out which part of the code should be changed
to fix a related bug. It’s also extremely useful for explaining complex code or
frameworks you’re not familiar with.


### Avoiding the Gambling Mode

sunk cost fallacy


### A Typical Daily Flow

#### A Note on Pauses

What I noticed is simple: pauses are usually bad for focus.

I’ve found it unproductive to work on two different tasks in
parallel with AI. Whatever time I “saved” during the waiting moments, I later lost
trying to reload the context in my head.

### Starting Clean

Don’t start prompting until the code is in a clean, working state.


### Working in Small Steps

it’s often more effective to tell the model something like this:
“You are a junior developer doing your best. If an instruction seems unclear,
wrong, or unfamiliar, ask for more information before continuing.”

Another useful trick I often use is writing pseudocode directly into the file—just
a few lines that explain what I want to happen. Then I ask the assistant to
turn that into real code. This is often quicker and more precise than trying
to explain everything in plain English inside the chat window.

### Understanding with Ask Mode

The idea is simple: instead of asking the assistant to write code to solve a
problem, we ask it to tell us how to do something without writing any code,
and then we write it ourselves. In a way, it’s the opposite of the previous
recipe. But there’s a big advantage: by typing the code ourselves, we absorb
much more of what’s going on around it. We understand the structure, spot
conventions, and notice patterns we’d easily miss by just reading or copypasting.

This approach is a bit like rubber duck debugging, except the duck talks back
(even if it doesn’t always get everything right).

#### Fixing a Tricky Bug in Kondor-Json

Watch the video at https://youtu.be/HrZhIfeHTeU.


### Enjoying Ping-Pong

### Fixing the New Data Class Converter (Example)

### Providing Feedback with Acceptance Tests

We need to give the
assistant a clear and objective signal about whether the application is behaving
correctly so it can self-adjust. A good way to do this is through **acceptance tests**, where we verify that the overall behavior of the system is acceptable.

The easiest form of acceptance tests is **end-to-end tests**. They validate the
system from the outside, in the same way a user or another system would.

### Planning Your Bug Investigations

LLMs don’t reason through why the
failure happens—they lack a mental model of cause and effect. They optimize
for “change something that looks relevant,” not for understanding the system
as a whole.

To address this, we can shift the LLM into a different role—not as a code
modifier, but as a planner. Specifically, we can ask it to create a step-by-step
debugging plan that follows a progressive logic, starting with the most likely
causes, and then eliminating them one by one.

Surprisingly, this works best without showing the model any code. That way,
it won’t “cheat” by hallucinating based on incomplete or irrelevant context.
Instead, it’s forced to “reason” purely from its knowledge and the high-level
problem description.

### Fixing an Inexplicable Bug (Example)

Watch the video.4

4. https://youtu.be/Zo7HbTFd5LE

### Designing in Parallel

Here’s how it works: instead of aiming for a single clean solution, you ask the
assistant to write or rewrite a feature in a few different ways.

Using multiple assistants and git worktree (or just checking out the project
multiple times), we can even work on several branches at the same time.

### Explaining Unknown Libraries

#### Using Kondor in a New Project (Example)


One new thing to keep an eye on is the proposed standard for LLM-friendly
documentation. 7

7. https://llmstxt.org/


### Scaling Refactors with Scripts

Instead of asking the assistant to refactor everything directly, we ask it to
write a script that can iterate through all the files and apply the transformation
one by one.

#### Migrating from One Library to Another (Example)


### Empowering with MCP

MCP is a simple and powerful standard that lets us expose structured functionality
to AI models through a small web server. It works a bit like a plugin
system, but it’s more flexible and easier to build for. The core idea is an MCP
server advertises a list of capabilities (like “search documentation,” “get open
incidents,” “query logs”), and each capability describes how it works, what
parameters it expects, and what kind of result it returns.


#### Building an MCP Server (Example)

you don’t need MCP for everything. Tasks that assistants already
handle well—like accessing the file system, running shell commands, or using
a SQL console—don’t require extra endpoints.

It’s also important to be selective. As Simon Willison points out,9 adding too
many MCP tools at once can hurt performance. The assistant may struggle
to decide which tool to use, leading to slower or less relevant results.

9. https://simonwillison.net/2025/Aug/22/too-many-mcps/



### Generating Documentation and Diagrams

#### Documenting Kondor Better (Example)

But maybe the most helpful part is it also created some Mermaid diagrams
to show how the parser, tokenizer, and converters work together. Instead of
trying to explain all the moving parts in words, the diagrams give you a quick
visual of the flow: what calls what, how data moves around, and where each
piece fits in.



## Is It All Worth It?


As Kent Beck (yes, him again) famously said, “For each desired change, make
the change easy (warning: this may be hard), then make the easy change.”

AI is very good at making the easy changes. What it still cannot do reliably
is figure out how to make a hard change easy in the first place. That part still
requires our judgment and experience.


## What We Covered


### Cheat Sheet for Process Over Magic

(see book, page 88)
