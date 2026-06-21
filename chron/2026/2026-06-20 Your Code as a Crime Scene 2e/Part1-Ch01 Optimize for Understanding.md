---
v-1.0.0: 2026-06-21 | 
---

# CHAPTER 1: Optimize for Understanding

Know the Difference Between Essential and Accidental Complexity

- Fred Brooks’ influential No Silver Bullet [Bro86] essay

As programmers, we control the accidental side, the solution
complexity. Limiting the essential complexity means solving a
different problem, for example, by cutting the scope or decommissioning
a feature.


## Understand That Typing Isn’t the Bottleneck in Programming

In Facts and Fallacies of Software Engineering [Gla92], Robert Glass argues that **maintenance**
is the most important phase of any software product. Depending on
the product, maintenance accounts for 40 to 80 percent of the total life-cycle
cost. So what do we get for all this money? Glass estimates that 60 percent
of our maintenance work is genuine enhancements, not just bug fixes.

even if maintenance is time-consuming, it isn’t a problem in itself but
rather a good sign: only useful applications get maintained.

Given that we developers spend most of our time on understanding existing code, we have
one clear candidate. If we want to optimize any aspect of software development,
then we should **optimize for understanding**. That’s the big win.

### Understand Maintenance in an Agile World

maintenance now accounts for over 90 percent of a typical product’s life-cycle costs


## Meet the Challenges of Scale


**Joe asks: Can’t I Avoid Complexity by Getting It Right the First Time?**
No, a certain level of accidental solution complexity is inevitable. Let’s say we insist
on every single line of code being perfect, simple, and correct. As we will see in Design
for Human Problem-Solving, on page 173, even this noble approach isn’t enough. The
nature of software development and human problem-solving, in general, is inherently
iterative. We learn by doing and by observing the outcome.


## Beware the Lure of Complexity Metrics

cyclomatic complexity

Unfortunately, code metrics on their own are inadequate because they fail to capture the most important aspect of complexity: **impact**. Let’s see why.

### Approach Code from the Behavioral Perspective

**Complex code is only a problem if we need to deal with it.**