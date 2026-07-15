---
v-1.0.0: 2026-07-11 | July 14, 
---

# CHAPTER 3: A Functional Architecture

Software architecture is a domain in its own right, of course, so let’s follow
our own advice and use a “ubiquitous language” when talking about it. We’ll
use the terminology from Simon Brown’s **“C4”** approach...

One of the goals of a good architecture is to define the various boundaries
between containers, components, and modules, such that when new
requirements arise, as they will, the “cost of change” is minimized.


## Bounded Contexts as Autonomous Software Components

The translation from the logical design to the deployable equivalent
is not critical, as long as we ensure that the bounded contexts stay decoupled
and autonomous.

We stressed earlier that it’s important to get the boundaries right, but of
course, this is hard to do at the beginning of a project, and we should expect
that the boundaries will change as we learn more about the domain. It’s a lot
easier to refactor a monolith, so a good practice is to build the system as a
monolith initially and refactor to decoupled containers only as needed. There’s
no need to jump straight to microservices and pay the “microservice premium”2

2. https://www.martinfowler.com/bliki/MicroservicePremium.html


## Communicating Between Bounded Contexts

Queues ... 
In a monolithic system, we can use the same queuing approach
internally, or just use a simple direct linkage between the upstream component
and the downstream component via a function call.

### Transferring Data Between Bounded Contexts

Data Transfer Objects or DTOs

### Trust Boundaries and Validation

add “gates” at the beginning and end of the workflow that act as intermediaries
between the trusted domain and the untrusted outside world

input gate

output gate


## Contracts Between Bounded Contexts

A Shared Kernel relationship

A Customer/Supplier or Consumer Driven Contract

A Conformist relationship - opposite of consumer-driven.

### Anti-Corruption Layers

“ACL”

the “input gate” often plays the role of the ACL—it prevents the internal, pure
domain model from being “corrupted” by knowledge of the outside world

That is, the Anti-Corruption Layer is not primarily about performing validation
or preventing data corruption, but instead acts as a translator between two
different languages

### A Context Map with Relationships


“inverse Conway maneuver”

(
From Google AI: The Inverse Conway Maneuver (or Reverse Conway Maneuver) is an organizational design strategy stating that to build an effective software system, you must intentionally restructure your teams to mirror your desired architecture, rather than letting existing team communication patterns dictate the software's design.

Coined by ThoughtWorks practitioners in 2010, the maneuver is a direct response to Conway's Law—which states that systems often mirror the communication structures of the organizations that build them. If your organization has rigid, siloed teams, your software will likely become a rigid, tightly coupled monolith.
)


## Workflows Within a Bounded Context

A workflow is always contained within a single bounded context

### Workflow Inputs and Outputs

a workflow function does
not “publish” Domain Events—it simply returns them. How they get published
is a separate concern.

### Avoid Domain Events Within a Bounded Context

In a functional design ... if we need a “listener” for an event, we just
append it to the end of workflow

(Question: can we make this same approach in an object-oriented language, like C#)



## Code Structure Within a Bounded Context

“code that changes together belongs together.”

A better way is to switch to “vertical” slices

### The Onion Architecture

all dependencies must point inward

Hexagonal Architecture

Clean Architecture

In order to ensure that all dependencies point inward, we will have to use the
**functional equivalent of dependency injection**, which is discussed in Implementation:
Composing a Pipeline.

### Keep I/O at the Edges



## What’s Next

we need to understand what **type** means to functional
programmers and how it is different from **class** in object-oriented design.


