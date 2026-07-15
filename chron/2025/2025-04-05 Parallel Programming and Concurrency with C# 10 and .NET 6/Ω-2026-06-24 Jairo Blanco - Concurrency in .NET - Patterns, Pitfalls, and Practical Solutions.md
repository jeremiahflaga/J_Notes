---
v-1.0.0: 2025-06-24 | and following day/s
---


# "Concurrency in .NET: Patterns, Pitfalls, and Practical Solutions" by Jairo Blanco

from https://dev.to/arthus15/concurrency-in-net-patterns-pitfalls-and-practical-solutions-8dm

## Introduction

## Understanding Concurrency

## Concurrency vs Parallelism

## The Most Common Concurrency Problems

Race Conditions

Deadlocks

Lost Updates

Double Processing


## Thread Safety in .NET

Using lock

Using Interlocked

Async Concurrency and SemaphoreSlim

Optimistic Concurrency with Entity Framework

Handling DbUpdateConcurrencyException


## Distributed Concurrency Problems

Distributed Locks

Idempotency: The Secret Weapon

The Outbox Pattern

Retry Policies and Concurrency


## Common Interview Scenario

Problem: 
Two users edit the same customer record.

## Common Production Scenario

Problem:
A scheduled job runs every minute.

## Common API Scenario

Problem:
Customers double-click the "Place Order" button.

Two requests arrive.

Two orders are created.


## Performance Considerations

Not every concurrency problem should be solved with locking.

Excessive locking can create:

 - Thread contention
 - Reduced throughput
 - Poor scalability
 - Preferred order:

1. Immutable data
1. Thread-safe collections
1. Atomic operations
1. Optimistic concurrency
1. Locks
1. Distributed locks

The further down the list, the higher the complexity.

## Practical Rules of Thumb

When building .NET applications:

 - Prefer async over blocking threads.
 - Avoid shared mutable state.
 - Use ConcurrentDictionary for shared caches.
 - Use Interlocked for counters.
 - Use SemaphoreSlim for async synchronization.
 - Use EF Core optimistic concurrency for CRUD operations.
 - Make APIs idempotent.
 - Use distributed locks sparingly.
 - Design for retries.
 - Assume operations can execute twice.


## Conclusion

Concurrency is not merely a multithreading concern—it is a data consistency concern.

As systems scale, concurrency challenges evolve:

```
Single Thread
    ↓
Multiple Threads
    ↓
Multiple Requests
    ↓
Multiple Processes
    ↓
Multiple Servers
```

The techniques evolve as well:

```
lock
    ↓
SemaphoreSlim
    ↓
Optimistic Concurrency
    ↓
Idempotency
    ↓
Distributed Locks
    ↓
Event-Driven Patterns
```

The most successful .NET systems do not attempt to eliminate concurrency. Instead, they embrace it while ensuring that concurrent operations remain safe, predictable, and recoverable.