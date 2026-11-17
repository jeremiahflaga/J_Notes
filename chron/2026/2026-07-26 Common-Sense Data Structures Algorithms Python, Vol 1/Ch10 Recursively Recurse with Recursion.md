---
v-1.0.0: 2026-11-15 | and Nov 16
---

# CHAPTER 10: Recursively Recurse with Recursion


**Recursion** is the term for a function calling itself.


## Recurse Instead of Loop

In almost any case in which you can use a loop, you can also use recursion.


## The Base Case


## Reading Recursive Code


## Recursion in the Eyes of the Computer

### The Call Stack

### Stack Overflow


## Filesystem Traversal

``` python
import os

def print_subdirectories(directory_name):
	for filename in os.listdir(directory_name):
		path = os.path.join(directory_name, filename)
		if os.path.isdir(path):
			print(path)
			print_subdirectories(path)
```

Depth-First Search, on page 336
