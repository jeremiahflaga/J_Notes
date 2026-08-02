---
v-1.0.0: 2026-07-30 | and Aug 1 & 2, 2026
---

# CHAPTER 4: Speeding Up Your Code with Big O

If you find that Big O labels your algorithm as a slow one, you can now take
a step back and try to figure out if there’s a way to optimize it by trying to get
it to fall under a faster category of Big O. This may not always be possible, of
course, but it’s certainly worth thinking about.


## Bubble Sort

We keep on executing these pass-throughs until we have a passthrough
in which we did not perform any swaps.



## Bubble Sort in Action

This is actually the reason why this algorithm is called **Bubble** Sort: in each
pass-through, the highest unsorted value “bubbles” up to its correct position.

Because we made at least one swap during this pass-through, we need to
conduct another pass-through.

Since we made at least one swap during this pass-through, we need to perform
another one.

### Code Implementation: Bubble Sort

(skim reading)

We also change `sorted` to `False` if we have to make a swap



## The Efficiency of Bubble Sort

Notice the inefficiency here. As the number of elements increases, the number
of steps grows **exponentially**. (In technical math terms, we’d actually say that
it grows quadratically.)

Because for N values, Bubble Sort takes $N^2$ steps, in Big O we say that Bubble
Sort has an efficiency of $O(N^2)$.

$O(N^2)$ is also referred to as quadratic time.


## A Quadratic Problem

Very often (but not always), when an algorithm nests one loop inside another,
the algorithm is $O(N^2)$.


## A Linear Solution

(One disadvantage with this new implementation is that this approach will
consume more memory than the first approach. Don’t worry about this for
now; we’ll discuss this at length in Chapter 19, Dealing with Space Constraints,
on page 385.)

