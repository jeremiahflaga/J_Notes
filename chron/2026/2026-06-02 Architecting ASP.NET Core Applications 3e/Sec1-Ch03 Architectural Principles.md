---
v-1.0.0: 2026-06-04 |
---

# Chapter 3: Architectural Principles

In this chapter, we cover the following topics:
• The separation of concerns (SoC) principle
• The DRY principle
• The KISS principle
• The YAGNI principle
• The SOLID principles

We also **revise** the following notions:
• Covariance
• Contravariance
• Interfaces


## Don’t repeat yourself (DRY)

it is imperative to regroup duplicated logic **by concern**, not only by the similarities of the
code


## The SOLID principles

It is crucial to remember that these are just **guiding principles, not rules** that you must follow no matter what.


### Single responsibility principle (SRP)

”There should never be more than one reason for a class to change.”
— Robert C. Martin, originator of the SRP

> Nothing is purely black or white — most things are a shade of gray. The same applies to software design: always do your best, learn from your mistakes, and stay humble (a.k.a. continuous improvement). You will not succeed at everything, and it’s OK. Remember that behind each failure is an opportunity to learn.

It is tough to define one hard rule that defines “one reason” or “a single responsibility.” However, as a
rule of thumb, aim at packing a cohesive set of functionalities in a single class that revolves around
its responsibility. You should strip out any excess logic and add missing pieces.

**Project – Single Responsibility: ** ProductRepository for both public and private products


### Open/closed principle (OCP)

”Software entities (classes, modules, functions, and so on) should be open for extension
but closed for modification.”

the first appearance of the OCP in 1988 referred to inheritance, and OOP has evolved
a lot since then ... opt for composition over inheritance

### Liskov substitution principle (LSP)

The LSP states that in a program, if we replace an instance of a superclass (supertype) with an instance
of a subclass (subtype), the program should not break or behave unexpectedly.

It is also similar to _Design by Contract_, by Bertrand Meyer.

(see book for complete explanation of LSP)

OK, at this point, you would be right to feel that this is rather complex. Yet, **rest assured that this is the less important of the SOLID principles because we are moving as far as we can from inheritance, so the LSP should not apply often.**

We can summarize the LSP as: **In your subtypes, add new behaviors and states; don’t change existing ones.**

An excellent way of enforcing those behavioral constraints is automated testing. You can
write a test suite and run it against all subclasses of a specific supertype to enforce the
preservation of behaviors

Covariance and contravariance (see book)

The key idea of the LSP is that the consumer of a supertype should remain unaware of whether it’s
interacting with an instance of a supertype or an instance of a subtype.

We could also name this principle the backward-compatibility principle because everything that
worked in a way before must still work at least the same after the substitution, which is why this
principle is essential.

The more we are progressing in the book and with our engineering skills, the more we are moving away
from inheritance, and the less we need to worry about this principle.


### Interface segregation principle (ISP)

”Many client-specific interfaces are better than one general-purpose interface.” --- Robert C. Martin

In practice, since C# 8, we can create default implementation in interfaces, which could be helpful to limit
breaking changes in a library (such as adding a method to an interface without breaking any
class implementing that interface).

The main takeaway is to only depend on the interfaces that you consume.

### Dependency inversion principle (DIP)

”depend upon abstractions, not concretions.” --- Robert C. Martin

(skipped for now)