---
v-1.0.0: 2026-08-05 | 
---

# CHAPTER 6: Optimizing for Optimistic Scenarios

## Insertion Sort

## Insertion Sort in Action

### Code Implementation: Insertion Sort

(skim reading)

## The Efficiency of Insertion Sort

1 + 2 + 3 + … + (N - 1) comparisons.

When examining this pattern, it emerges that for an array containing N elements,
there are approximately $N^2 / 2$ comparisons.


approximately $N^2 / 2$ comparisons

When an array
is sorted in reverse order, there will be as many shifts as there are comparisons

there are N - 1 removals and N - 1 insertions

total: $N^2 + 2N - 2$ steps

You’ve already learned one major rule of Big O: that Big O ignores constants.
With this rule in mind, we’d—at first glance—simplify this to $O(N^2 + N)$.

However, I’ll now reveal another major rule of Big O:

Big O notation **only takes into account the highest order of N** when we have
multiple orders added together.


## The Average Case

Indeed, in a worst-case scenario, Selection Sort is faster than Insertion Sort.
However, it’s critical we also take into account the **average-case scenario**.

Why?

By definition, the cases that **occur most frequently** are average scenarios.

So which is better: Selection Sort or Insertion Sort? The answer is, well, it
depends.


## A Practical Example

`intersection` function

Is there any way we can improve this algorithm?

With the addition of the break, we can cut the inner loop short and save steps
(and therefore time).

(short-circuit)