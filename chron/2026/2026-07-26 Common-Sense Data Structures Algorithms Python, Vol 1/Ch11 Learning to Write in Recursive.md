---
v-1.0.0: 2026-11-16 | and Nov 17
---

# CHAPTER 11: Learning to Write in Recursive

Recursion can actually have a terribly negative impact on the time complexity
of an algorithm, but this is the subject of the next chapter.


## Recursive Category: Repeatedly Execute

Over the course of tackling various recursive problems, I began to find that
there are various **categories** of problems.

### Recursive Trick: Passing Extra Parameters


## Recursive Category: Calculations

a second general category: performing a calculation based on a **subproblem**.

A subproblem is a version of the very same problem applied to a smaller input.

example: factorial(6) is equivalent to: 6 * factorial(5).

we call factorial(5) a subproblem of factorial(6)

### Two Approaches to Calculations

build the solution from the **“bottom-up**,” or we can attack the problem going “**top-down**”

bottom-up - using classic loop

top-down - using recursion

``` python
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
```

we can also use recursion to implement the bottom-up strategy:

``` python
def factorial(n, i=1, product=1):
    if i > n:
        return product

    return factorial(n, i + 1, product * i)
```

`product` is
the variable in which we store the calculation as we keep multiplying each
successive number

recursion is the **only** way to achieve a top-down strategy



## Top-Down Recursion: A New Way of Thinking

going top-down offers a new **mental strategy** for tackling a problem

We can free our mind from some of the nitty-gritty details we normally
have to think about when going bottom-up.

### The Top-Down Thought Process

when tackling a top-down
problem, it helps to think the following three thoughts:

1. Imagine the function you’re writing has already been implemented by
someone else.
2. Identify the subproblem of the problem.
3. See what happens when you call the function on the subproblem and go
from there.

### Array Sum

To solve our problem of finding the sum of [1, 2, 3, 4, 5] then, we can just add
the first number, 1, to the result of sum([2, 3, 4, 5]).

_primary_ base case

### String Reversal

### Counting X


( what about `return count_x(string[0]) + count_x(string[1:])` (?) )



## The Staircase Problem

``` python
def number_of_paths(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    return (number_of_paths(n - 1)
            + number_of_paths(n - 2)
            + number_of_paths(n - 3))
```

(walay duplicates??)

(walay duplicates. Take n=4 for example, then n=5)



## Anagram Generation

``` python
def anagrams_of(string):
    if len(string) == 1:
        return [string[0]]

    collection = []

    substring_anagrams = anagrams_of(string[1:])

    for substring_anagram in substring_anagrams:
        for index in range(len(substring_anagram) + 1):
            new_string = (substring_anagram[:index]
                          + string[0]
                          + substring_anagram[index:])
            collection.append(new_string)

    return collection
```

it’s worth noting at this point that we are using a combination
of loops and recursion together

```
"abcd" # inserted 'a' at index 0
"bacd" # inserted 'a' at index 1
"bcad" # inserted 'a' at index 2
"bcda" # inserted 'a' at index 3
```

### The Efficiency of Anagram Generation

O(N!). This is also known as **factorial time**.

O(N!) is the slowest category of Big O we’ll encounter in this book.


