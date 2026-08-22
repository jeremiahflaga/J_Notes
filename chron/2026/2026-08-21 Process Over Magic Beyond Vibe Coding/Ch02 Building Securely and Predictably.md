---
v-1.0.0: 2026-08-22 | 
---

# CHAPTER 2: Building Securely and Predictably

In this chapter, we’ll explore how to guide AI assistants to produce solid,
reliable code — not just prototypes, but production-quality software.


## Keep the Edge

Do you need to be a programmer to do it?
Not necessarily, but you do need to think like one.

the trick to making LLMs work for coding isn’t
finding some magical “perfect prompt;” it’s about setting up a solid process
and sticking to it.


## One Prompt, One Commit

• Only commit working code:

That means writing tests—both unit
and end-to-end — for every new piece of functionality.

• Always review before committing:

If unsure, you can always ask for an explanation from the AI
assistant itself.

• Focused prompts:

Either you’re adding a new feature or you’re refactoring — not
both.

• When stuck, roll back:

don’t waste time fighting it


For production code you should check the code **line by line** just like a normal PR review from someone you don’t fully trust.


### Mastering Git

In particular, `git worktree` is a little-known gem that lets you (and the AI) work on multiple
branches at the same time — without constantly checking out or stashing changes.

It allows you to **check out several branches, each in its own subfolder**, making it
ideal for experimenting: you can compare results quickly, merge the good parts, and
keep your main branch clean.



## An AI with Good Habits

### What’s the Ruleset?

This is often written in a file called
`agents.md` or `rules.md` that contains all the rules that the AI agent will have to
follow throughout the session.

(see book for examples)

### Your Code, Your Rules

Test-Driven Development (TDD)

when working with
an LLM, it’s critical to **write tests** alongside the code.
Why? Because tests become the **main feedback loop for the AI**. Unlike human
developers, the assistant can’t reason abstractly or run the full application
on its own. Tests are how we help it check its work and keep it honest.

And if we wait until the end to add tests, we
often discover the code is hard — or even impossible — to test without refactoring.
That’s wasted time. Writing the tests first, or at least together with the
code, helps us avoid all that.

Once testing is in place, we can talk about code design. For that, we can rely
on the classic **Four Rules of Simple Design (from Kent Beck)**:

(see book)

Next—and this is just my personal preference (feel free to use your own
style)—I want the LLM to adopt a **functional style** whenever possible:

(see book)

At the architecture level, here’s what we aim for:

(see book)

And above all, we want to keep it simple: short functions, minimal dependencies,
with no unnecessary complexity.

Now we also need to add a few rules about the process itself.

(see book)

Here’s a sample ruleset file you can use as a starting point.

```
### Interaction Rules

* Ask clarifying questions if input is unclear.
* Explain why and suggest alternatives if task is not feasible.
* Use structured, readable formatting (headings, lists, code blocks).
* Follow instructions closely and explain clearly what you have done.
* Don't modify code unrelated to the current task.
* Try always to match the style of the code you are touching.

### Coding Standards

* Write meaningful tests with assertions for all code.
* Avoid duplicated test assertions.
* Maintain evolving test coverage.
* Apply Four Rules of Simple Design:

    1. Code works (passes tests).
    2. Reveals intent.
    3. No duplication.
    4. Minimal elements.

* Prefer functional style:

    * Use explicit parameters.
    * Prefer immutability.
    * Prefer declarative over imperative.
    * Minimize state.

### Architecture

* Modularize by concern, not by technical layer.
* One responsibility per module.
* Low inter-module coupling.
* Short functions, no overengineering.

### Workflow

* Read `spec.md` before coding.
* Update `spec.md` after task (log changes).
* Write and pass tests before finalizing.
* Keep a `README.md` with setup/run info.
* Store all docs/specs in Markdown.

### Commit Strategy

* One prompt = one commit.
* Each commit:

    * Self-contained.
    * Includes tests.
    * Uses 50/70 commit message format.

### Safe Practices

* Do not change test assertions during refactoring.
* Do not skip failing tests.
* Do not invent unknown APIs; ask if you are unsure.

### Project Preferences (Example)

* Python: use Poetry.
* Kotlin: expression-bodied functions.
* JS: use ES Modules.
* Follow `.editorconfig` + linter rules.

### Goal

Produce consistent, safe, testable, and maintainable code.
Stick to the rules---no shortcuts.
```


### Skillful Assistants

Instead of putting everything in one large rules file, we keep only the core ideas
there. The details move into small, focused instructions called **skills** — for
example: how to write tests, how to review for security, or which UI style to
follow.


## Building an Application Following Rules

(book recommendation: Vector Search with JavaScript [Gre25], an excellent book on the topic)

### Project Overview

### First Commit

screencast 1 of 5 (Build LLM Empowered Semantic Search tool)
3. https://youtu.be/IDy3B4oiIsc

### Building the First Command

This approach—implementing one small feature at a time—is sometimes
called **Inverse Salami** (a term introduced in Growing Object-Oriented Software,
Guided by Tests [FP09]). The idea is that we build the application one thin
slice at a time, starting from nothing and gradually adding functionality until
it’s complete. This is the opposite of how you eat a salami: there, you start
with the whole thing and take slices off until there’s nothing left.

(keyword: GOOS)

I personally
prefer building applications from the outside in. That way, I’m always making
sure we’re implementing something that’s needed.

(same approach as in GOOS)

### Find All Documents in a Folder

Cursor’s Git UI

(Cursor mentioned)

### Parsing PDF Files

### Chunking Text in Small Blocks

This step turned out to be problematic for the
assistant. It wasn’t able to write a sensible test that passed. Instead, it kept
trying to either change the requirements or modify the tests to match its
broken implementation, and I had to actively stop it from doing that.

### Updating the PDF Library

screencast 2 of 5 (Build LLM Empowered Semantic Search tool)
5. https://youtu.be/BTortzZHPBU


### Complete PDF Parsing and Chunking

This is a good lesson: always check
with double care what the generated tests are testing (around 12:30).

### Storing Chunks into the Vector Database

### Storing Metadata

While reviewing the tests before committing this step, I noticed they were
relying heavily on **mocks**. Now, nothing’s inherently wrong with mocking, but
it adds complexity to the test setup, and it’s easy to overuse it to the point
where we’re not testing anything meaningful.

### Introducing Ports and Adapters

First, we ask the assistant to introduce the Ports and Adapters design pattern
into the indexer service6 and then remove the mocks.

The problem came out in the tests. Instead of using simple, custom stubs for
the adapters, the assistant kept trying to mock them using the same mocking
libraries. I had to explicitly instruct it to implement test-only adapter stubs
that conformed to the expected interface. Watch the video.7

screencast 3 of 5 (Build LLM Empowered Semantic Search tool)
7. https://youtu.be/wYmTTx5iDTU

I suspect that decisions like this — architectural shifts, design patterns, and
long-term trade-offs — will remain firmly in the domain of human developers
for the foreseeable future. And I don’t think this is a bad thing.

But whatever your preference, the fact remains: LLMs are still limited to
**concatenating words**.

### Adding Search Command

As often happens, when adding the tests, the model fell back into its old
pattern and used mocks to simulate the search behavior. I had to step in and
explicitly tell it to remove the mocks and use proper adapters instead.

### End-to-End Testing

**Instead** of simply
writing a test that calls the existing index and search commands, the assistant
created a brand-new combined index and search feature in the codebase
without even reusing the code we already had. I only realized this when it
was time to commit. Watch the video.8

screencast 4 of 5 (Build LLM Empowered Semantic Search tool)
8. https://youtu.be/VOpyOc-DG6g

### Indexing Incrementally

screencast 5 of 5 (Build LLM Empowered Semantic Search tool)
10. https://youtu.be/-x_mvYOD7CM

### Final Test

``` terminal
> poetry run python -m less.cli search-dir /home/ubertobarbini/books_test
"handling the state in functional programming"

LESS CLI module loading...
Imports completed, loading Indexer...
LESS CLI initialization complete
Searching for: handling the state in functional programming
[1] From: from-objects-to-functions_P1.0.pdf, Page 144
Score: 0.2910
------
How can we model this mutable entity in functional programming?
Implement a Finite State Machine
Let's draw a diagram of all the states and their transitions:
This diagram illustrates how we can represent the entities that change
behavior according to their state using a state machine.
We map the transitions into domain events, then we constrain each state to
accept only some events, and finally, we allow events to change the entity
state to another one.
...
```

Notice how it selected a very good match from across the whole book (which
is about 500 pages) not by matching the words exactly but by matching the
meaning.


## Results and Reflections

You can also see that I’m not religiously following all my own rules. They’re
guidelines, not strict laws, and knowing when to bend them is part of knowing
your tools. Still, one golden rule I never broke: run the tests and verify before
every commit.

If all else
fails, and you’re stuck, ask the assistant to explain what’s happening. It’s
surprisingly good at helping you figure things out even if it often can’t fix the
problem by itself.

