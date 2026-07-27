---
v-1.0.0: 2026-07-26 | 
---

# CHAPTER 1: Why Data Structures Matter

**quality** of their code

code **maintainability** - readability, organization, and modularity

code **efficiency** - runs faster than the other

This book is about writing efficient code.

The first step in writing fast code is to understand what data structures are and
how different data structures can **affect** the speed of our code.



## Data Structures

Data structures refer to how data is **organized**. You’re going to learn how the
same data can be organized in a variety of ways.

organization of data ... can significantly **impact how fast your code runs**



## The Array: The Foundational Data Structure

(In Python, the built-in array-like data structure is called a list, but I’ll refer to
them as arrays, keeping in line with the more general computer science term.)

### Data Structure Operations

Read

Search

Insert

Delete



## Measuring Speed

If you take away just one thing from this book, let it be this: when we measure
how “fast” an operation is, we do not refer to how fast the operation takes in
terms of pure **time**, but instead in how many **steps** it takes.

Measuring the speed of an operation is also known as measuring its time
complexity. Throughout this book, I’ll use the terms speed, time complexity,
efficiency, performance, and runtime interchangeably. They all refer to the
number of steps a given operation takes.


## Reading

A computer’s memory can be viewed as a giant collection of cells.


## Searching

linear search

Another way of saying this is that for N cells in an array, linear search would
take a maximum of N steps. In this context, N is just a variable that can be
replaced by any number.


## Insertion

The worst-case scenario

We can say that insertion in a worst-case scenario can take N + 1 steps for
an array containing N elements.


## Deletion

We can say then, that for an array containing N elements, the maximum
number of steps that deletion would take is N steps.


## Sets: How a Single Rule Can Affect Efficiency

Sets are of different types, but for this discussion, I’ll talk about an **array-based set**.

So, every insertion into a set first requires a search.

insertion into the end of a set will take up to N + 1 steps for N elements

In the worst-case scenario, where we’re inserting a value at the beginning of
a set ... That’s a total of 2N + 1 steps.
Contrast this to insertion into the beginning of a regular array, which only
takes N + 1 steps.


## Wrapping Up

Now that you’ve begun to learn how to think about the time complexity of data
structures, we can use the same analysis to **compare competing algorithms (even within the same data structure)** to ensure the ultimate speed and performance
of our code. And that’s exactly what the next chapter is about.