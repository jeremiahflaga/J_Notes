---
v-1.0.0: 2026-06-22 | up to June 24
---


# CHAPTER 1: Introducing Domain-Driven Design

---
## Questions to Answer

1. Is a developer's job to write code?

1. What is this **design approach** focused on clear communication and shared domain knowledge?

1. What are the **three approaches** to ensure that developers understand the problem?

1. What are the four guidelines for creating a shared model of a domain.

1. The first guideline says to focus on business events rather than data structures. Why is that?

1. What technique can we use to be able to know these business events?

1. The terms “workflows,” “scenarios,” “use cases,” “business processes,” are often used interchangeably. But in this book these terms have precise. Can you state the precise meanings of those terms?

1. In DDD what do we call these requests which makes Domain Events to happen?



---


**A developer’s job** is to solve a problem through software, and coding
is just one aspect of software development. Good design and communication
are just as important, if not more so.

“garbage in, garbage out” rule

Domain-driven design is not appropriate for all software development, of
course. There are many types of software (systems software, games, and so
on) that can be built using other approaches. However, it is particularly useful
for business and enterprise software, where developers have to collaborate
with other nontechnical teams, and that kind of software will be the focus of
this book.


## The Importance of a Shared Model

So how can we ensure that we, as developers, do understand the problem?

(1) Some software development processes address this by using written specifications
or requirements documents to try to capture all the details of a
problem. Unfortunately, this approach often creates distance between the
people who understand the problem best and the people who will implement
the solution.

(2) A much better solution is to eliminate the intermediaries and encourage the
domain experts to be intimately involved with the development process, 
... This kind of iterative process is at the core of “agile” development processes.
However, even this approach has its problems. The developer acts as a
translator, translating the domain expert’s **mental model** into code.

(3) But there is a third approach. What if the domain experts, the development
team, other stakeholders, and (most importantly) the source code itself all
**share the same model**? In this case, there is no translation from the domain
expert’s requirements to the code. Rather, the code is designed to reflect the
shared **mental model** directly.

And that is the **goal of domain-driven design**.

So we need to create a shared model. How can we do this? The domain-driven
design community has developed some guidelines to help us here. They are as follows:

1. Focus on business events and workflows rather than data structures.
2. Partition the problem domain into smaller subdomains.
3. Create a model of each subdomain in the solution.
4. Develop a common language (known as the “Ubiquitous Language”) that is shared between everyone involved in the project and is used everywhere in the code.

## Understanding the Domain Through Business Events

a business doesn’t just **have** data, it **transforms** it somehow. That is,
you can think of a typical business process as a series of data or document
transformations. **The value of the business is created in this process of transformation**, so it is critically important to understand how these transformations
work and how they relate to each other.

We call these things **Domain Events**.

Domain Events are the starting point for almost all of the business processes
we want to model. For example, “new order form received” is a Domain Event
that will kick off the order-taking process.

### Using Event Storming to Discover the Domain

### Discovering the Domain: An Order-Taking System

After a while, we might have list of posted events like this:
• Order form received
• Order placed
• Order shipped
• Order change requested
• Order cancellation requested
• Return requested
• Quote form received
• Quote provided
• New customer request received
• New customer registered

Some of the events have business workflows posted next to them, such as
“Place order” and “Ship order,” and we’re beginning to see how the events
connect up into larger workflows.

### Expanding the Events to the Edges

**Workflows, Scenarios, and Use Cases**

We have many different words to describe business activities: “workflows,” “scenarios,”
“use cases,” “processes,” and so on. They’re often used interchangeably; but in this
book, we’ll try to be a bit more **precise**.

• A **scenario** describes a goal that a customer (or other user) wants to achieve,
such as placing an order. It is similar to a “story” in agile development. 
A **use case** is a more detailed version of a scenario, which describes in general terms
the user interactions and other steps that the user needs to take to accomplish
a goal. Both **scenario** and **use case** are user-centric concepts, focused on how
interactions appear from the user’s point of view.

• A **business process** describes a goal that the business (rather than an individual
user) wants to achieve. It’s similar to a scenario but has a business-centric focus
rather than a user-centric focus.

• A **workflow** is a detailed description of part of a business process. That is, it lists
the exact steps that an employee (or software component) needs to do to
accomplish a business goal or subgoal. We’ll limit a workflow to what a single
person or team can do, so that when a business process is spread over multiple
teams (as the ordering process is), we can divide the overall business process
into a series of smaller workflows, which are then coordinated in some way.

## Documenting Commands

if the command does succeed, it will initiate a workflow
that in turn will create corresponding Domain Events. Here are some
examples:
• If the command was “Make X happen,” then, if the workflow made X
happen, the corresponding Domain Event would be “X happened.”
• Command: “Place an order”; Domain Event: “Order placed.”

In fact, we will try to model most business processes in this way. **An event triggers a command, which initiates some business workflow.** The output of the workflow is some **more events**. And then, of course, those events can
trigger **further commands**.

not all events need be associated with a command. Some events
might be triggered by a scheduler or monitoring system, such as MonthEndClose
for an accounting system or OutOfStock for a warehouse system.



## Partitioning the Domain into Subdomains

It’s clear that various aspects of the “order-taking process” can
be separated: the order taking, the shipping, the billing, and so on. As we
know, the business already has separate departments for these areas, and
that’s a pretty strong hint that we can follow that same separation in our
design. We will call each of these areas a **domain**.

we can define a “domain” as “an area of coherent knowledge.”

here’s an alternative
definition of a domain: a “domain” is just that which a “domain expert” is
expert in! This is much more convenient in practice

The domains overlap a little bit.



## Creating a Solution Using Bounded Contexts

The solution can’t possibly represent **all** the information in the original domain,

We should only capture the information that is relevant
to solving a particular problem.

We therefore need to create a distinction between a “**problem space**” and a
“**solution space**,” and they must be treated as two different things. To build
the solution we will create a **model** of the problem domain, extracting only
the aspects of the domain that are relevant and then re-creating them in our
solution space as shown in the figure on page 17.

``` mermaid
venn-beta
  title "Problem space (real world)"
  set Order
  set Shipping
  set Billing
  union Order,Shipping
  union Shipping,Billing
  union Order,Billing
```
<div>
<center>
<span style="font-size:60px;text-align:center;">&darr;</span> design process
</center>
</div>

``` mermaid
C4Context
  title "Solution space (domain model)"
    
  System(billing, "Order-taking context")
  System(order, "Shipping context")    
  System(shipping, "Billing context")   
```

the domains and subdomains in the
problem space are mapped to what DDD terminology calls **bounded contexts** — a 
kind of subsystem in our implementation. **Each bounded context is a mini domain model** in its own right. 
We use the phrase _bounded context_ instead
of something like _subsystem_ because it helps us stay focused on what’s
important when we design a solution: being aware of the **context** and being
aware of the **boundaries**.

(Remember "Why I don't need a bounded context" by Herman Peeren: **"bounded context" == "context boundary" == "the model itself"**; ubiquitous language == model language)

Why context?

just as in the real world, information
**taken out of context** can be confusing or unusable.

Why bounded?

A domain in the problem space does not always have a one-to-one relationship
to a context in the solution space. Sometimes, for various reasons, a single
domain is broken into multiple bounded contexts—or more likely—multiple
domains in the problem space are modeled by only one bounded context in
the solution space.

However you partition the domain, it’s important that each bounded context
have a clear responsibility, because when we come to implement the model,
a bounded context will correspond exactly to some kind of software component.
The component could be implemented as a separate DLL, or as a standalone
service, or just as a simple namespace.

### Getting the Contexts Right

(guidelines; see book)

### Creating Context Maps

... We say informally that the shipping context is **downstream** and the order-taking
context is **upstream**... (see book)

### Focusing on the Most Important Bounded Contexts

core domains — the ones that provide a business advantage, the ones that bring in the money

supportive domains

generic domains



## Creating a Ubiquitous Language




## Summarizing the Concepts of Domain-Driven Design

(summary of concepts and terminologies: good to memorize too)



## Wrapping Up

### The Ubiquitous Language

To help maintain a shared
understanding, it would be a good idea to create a living document or wiki
page that lists these terms and their definitions. This will help keep everyone
aligned and help new team members get up to speed quickly.