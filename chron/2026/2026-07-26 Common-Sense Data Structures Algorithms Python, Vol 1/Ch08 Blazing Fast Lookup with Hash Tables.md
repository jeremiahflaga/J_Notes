---
v-1.0.0: 2026-08-21 | 
---

# CHAPTER 8: Blazing Fast Lookup with Hash Tables

## Hash Tables

In Python they’re
called **dictionaries**, and other languages call them hashes, maps, hash maps,
dictionaries, or associative arrays. We’ll refer to them as **hash tables**, since
that’s a common universal way to refer to this data structure.

## Hashing with Hash Functions

## Building a Thesaurus for Fun and Profit, but Mainly Profit

## Hash Table Lookups

O(1)

### One-Directional Lookups


## Dealing with Collisions

## Making an Efficient Hash Table

Ultimately, a hash table’s efficiency depends on three factors:
• How much data we’re storing in the hash table
• How many cells are available in the hash table
• Which hash function we’re using

### The Great Balancing Act

A good hash table
strikes a balance of avoiding collisions while not consuming lots of memory.

To accomplish this, computer scientists have developed the following rule of
thumb: for every seven data elements stored in a hash table, it should have ten
cells.

This ratio of data to cells is called the **load factor**. Using this terminology, we’d
say that the ideal load factor is 0.7 (7 elements / 10 cells).

Again, most of the internals of a hash table are managed by the computer
language you’re using. It decides how big the hash table needs to be, what
hash function to use, and when it’s time to expand the hash table.


## Hash Tables for Organization


## Hash Tables for Speed

### Array Subset

One way we can do this is by using nested loops.

- O(N * M)

Now, let’s harness the power of a hash table to dramatically improve the efficiency
of our algorithm.

- O(N)