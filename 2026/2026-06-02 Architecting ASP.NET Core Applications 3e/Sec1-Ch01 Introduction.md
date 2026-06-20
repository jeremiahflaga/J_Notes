---
v-1.0.0: 2026-06-02 |
---

# Chapter 1: Introduction

> "The people who never fail are the ones who never do anything." --- Roosevelt

## What is a design pattern?

"A design pattern is a proven technique that we can use to solve a specific problem."

(don't overuse design patterns)

aim to write the least amount of readable code that solves your issue or automates your process.


## Anti-patterns and code smells

Some anti-patterns started as legitimate design patterns and were
labeled anti-patterns later. Sometimes, it is a matter of opinion, and sometimes the classification can be influenced by the programming language or technologies.


Remember that a code smell indicates that there _might_ be a problem,
not that there necessarily is one — **apply common sense**.


## Understanding the web: request/response

HTTP is **stateless**

There are mechanisms for creating a sense of persistence between requests for the server to be “aware” of its clients. The most well-known of these is **cookies**.

An **idempotent** request is a request that always yields the same result, whether it is sent once or multiple times. Ex. DELETE request

(Internet and networking overview on pages 10 & 11: OSI model, HTTP, TCP, IP, packet,  MTU)

If you find HTTP interesting, HTTP/2 is an excellent place to start digging deeper, as well as the HTTP/3 proposed standard that uses the QUIC transport protocol instead of HTTP (RFC 9114). ASP.NET Core 7.0+ supports HTTP/3, which is enabled by default in ASP.NET Core 8.0.


## Getting started with .NET

After years of improvements and two major versions in parallel (Core and Framework), Microsoft reunified most .NET technologies into .NET 5+ and the promise of a shared Base Class Library (BCL). **With .NET 5, .NET Core simply became .NET** while ASP.NET Core remained ASP.NET Core. There is no .NET “Core” 4, to avoid any potential confusion with .NET Framework 4.X.

### .NET 5+ versus .NET Standard

.NET Standard came into play to bridge the compatibility gap between .NET Core and .NET Framework, which eased the transition.

With .NET 5 unifying all the platforms and becoming the future of the unified .NET ecosystem, .NET Standard is no longer needed. Moreover, app and library authors should target the base **Target Framework Moniker (TFM)**, for example, net8.0. A TFM is a way to identify and target a certain version of .NET (net8.0 targets .NET 8 while net8.0-ios targets .NET 8 for IOS devices). You can also target netstandard2.0 or netstandard2.1 when needed, for example, to share code with .NET Framework. Microsoft also introduced OS-specific TFMs with .NET 5+, allowing code to use OS-specific APIs like net8.0-android and net8.0-tvos, which give access to OS-specific APIs. You can also target multiple
TFMs when needed.



