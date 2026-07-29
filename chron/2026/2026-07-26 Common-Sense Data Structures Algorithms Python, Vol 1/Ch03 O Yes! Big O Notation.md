---
v-1.0.0: 2026-07-29 | 
---

# CHAPTER 3: O Yes! Big O Notation

To help ease communication regarding **time complexity**, computer scientists
have borrowed a concept from the world of mathematics to describe a concise
and consistent language around the efficiency of data structures and algorithms.
Known as **Big O notation**, this formalized expression of these concepts
allows us to easily **categorize** the efficiency of a given algorithm and convey
it to others.


## Big O: How Many Steps Relative to N Elements?

$$
O(N)
$$

Some pronounce this as “Big Oh of N.” Others call it “Order of N.” My personal
preference, however, is “Oh of N.”

Here’s what the notation means. It expresses the answer to what we’ll call
the **key question**. The key question is this: **if there are N data elements, how many steps will the algorithm take?** Go ahead and read that sentence again.
Then, emblazon it on your forehead, as this is the **definition** of Big O notation
that we’ll be using throughout the rest of this book.

The answer to the key question lies within the **parentheses** of our Big O
expression. $O(N)$ says that the answer to the key question is that **the algorithm will take N steps**.

(N - "ing-ani ka daghan", or "pipila")

an algorithm that is $O(N)$ is also known as having **linear time**

an $O(1)$ algorithm can also be referred to as having constant time


(formal definition of Big O)

one way of describing Big
O is that it describes the upper bound of the growth rate of a function, or that if a
function g(x) grows no faster than a function f(x), then g is said to be a member of
O(f)

 - Justin Abrahms also
provides a pretty good definition in his article: https://justin.abrah.ms/computer-science/understanding-
big-o-formal-definition.html.


## The Soul of Big O

While Big O is an expression of the number of an algorithm’s steps relative
to N data elements, that alone misses the deeper **why** behind Big O, what I
dub the “soul of Big O.”

The soul of Big O is what Big O is truly concerned about: how will an algorithm’s
performance **change as the data increases**?

This is the soul of Big O. Big O doesn’t want to simply tell you how many
steps an algorithm takes. It wants to tell you the story of how the number of
steps increases as the data **changes**.

### Deeper into the Soul of Big O

Say we
had an algorithm of constant time that always took 100 steps no matter how
much data there was.

 - compare that with O(N)

... one million steps

### Same Algorithm, Different Scenarios

If we were to describe the
efficiency of linear search in its totality, we’d say that linear search is O(1) in
a **best-case scenario** and O(N) in a **worst-case scenario**.

Big O notation generally refers to the worst-case scenario
unless specified otherwise

a **“pessimistic” approach** can be a useful tool: knowing
exactly how inefficient an algorithm can get in a worst-case scenario prepares
us for the worst and may have a strong impact on our choices


## An Algorithm of the Third Kind

In Big O terms, we describe binary search as having a time complexity of: 
$O(log N)$

This type of algorithm is also known as
having a time complexity of **log time**.



## Logarithms

Logarithms are the inverse of exponents.

Another way of explaining $\log_{2} 8$ is this: if we kept dividing 8 by 2 until we
ended up with 1, how many 2s would we have in our equation?

8 / 2 / 2 / 2 = 1

In other words, how many times do we need to halve 8 until we end up with
1? In this example, it takes us three times.


## O(log N) Explained

In computer science, whenever we
say O(log N), it’s actually shorthand for saying O($\log_{2} N$). We just omit that
small 2 for convenience.

Said simply: O(log N) means the algorithm takes as many steps as it takes to
keep halving the data elements until we remain with 1.