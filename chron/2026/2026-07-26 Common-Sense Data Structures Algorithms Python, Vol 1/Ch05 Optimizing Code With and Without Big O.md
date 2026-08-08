---
v-1.0.0: 2026-08-05 | 
---

# CHAPTER 5: Optimizing Code With and Without Big O


## Selection Sort

## Selection Sort in Action

(skim reading)

### Code Implementation: Selection Sort

(skim reading)

## The Efficiency of Selection Sort

for N elements, we make

(N - 1) + (N - 2) + (N - 3) … + 1 comparisons.




From this comparison, it’s clear Selection Sort takes about half the number
of steps Bubble Sort does, indicating that **Selection Sort is twice as fast**.


## Ignoring Constants

But here’s the funny thing: in the world of Big O notation, Selection Sort and
Bubble Sort are described in exactly the same way.



$N^2 / 2$

Big O notation ignores constants.


## Big O Categories

Big O notation only concerns
itself with **general categories** of algorithm speeds.

Big O notation doesn’t care merely
about the number of steps an algorithm takes. It cares about the long-term
trajectory of the algorithm’s steps as the data increases.

So while Big O is perfect for contrasting algorithms that fall under **different**
classifications of Big O, when two algorithms fall under the **same** classification,
further analysis is required to determine which algorithm is faster.

### A Practical Example

### Significant Steps

The answer is that **all** steps are significant. It’s just that when we express the
steps in Big O terms, we drop the constants and thereby simplify the expression.