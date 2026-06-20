---
v-1.0.0: 2026-06-14 | "Project – BFF" and ff sections on next day, June 15, and on June 17; "Revisiting the CQRS pattern" and ff section on June 19
---

# Chapter 19: Introduction to Microservices Architecture


## What are microservices?

### Cohesive unit of business

A microservice should have a single business responsibility.

If you know Domain-Driven
Design (DDD), a microservice will most likely represent a Bounded Context, which in turn is what I
call a cohesive unit of business. Basically, a cohesive unit of business (or bounded context) is a self-contained
part of the domain with limited interactions with other parts.

### Ownership of data

Each microservice should be the source of truth of its cohesive unit of business. A microservice should
share its data through an API (a web API/HTTP, for example) or another mechanism (integration
events, for example).

### Microservice independence


## An introduction to Event-Driven Architecture


## Getting started with message queues

A message queue is nothing more than a queue we leverage to send ordered messages. A queue works
on a First In, First Out (FIFO) basis.

If you need to process messages in order and want each message to be delivered to a single recipient
at a time, a **message queue** seems like the right choice. Otherwise, the **Publish-Subscribe** pattern
could be a better fit for you.


## Overview of the Publish-Subscribe pattern

instead of sending one message to one
handler (or enqueuing a message), we publish (send) a message (event) to zero or more subscribers
(handlers). Moreover, the publisher is unaware of the subscribers; it only sends messages out, hoping
for the best (also known as **fire and forget**).

We can use the **Pub-Sub pattern** in-process or in a distributed system through a **message broker**.

To receive messages, subscribers must subscribe to topics (or the equivalent of a topic):

The second part of the Pub-Sub pattern is to publish messages


## Overview of the Event Sourcing pattern

(skim reading only; need to re-read)



## Introducing Gateway patterns

Gateways can help us achieve the following:
• Hide complexity by routing requests to the appropriate services
• Hide complexity by aggregating responses and translating one external request into many
internal ones
• Hide complexity by exposing only the subset of features that a client needs
• Translate a request into another protocol

A gateway can also centralize different processes, such as logging and caching requests, authenticating
and authorizing users and clients, enforcing request rate limits, and other similar policies.

You can see gateways as **facades**, but instead of being a class in a program, it is a program of its own,
shielding other programs. There are multiple variants of the Gateway pattern, and we explore many
of them here.

We can see a gateway as a **reverse proxy** that offers advanced functionalities.


### Overview of the Gateway Routing pattern

hide the complexity of our system by having the gateway
route requests to the appropriate services

this brings some possible issues to the table as the gateway becomes a single point of failure --- consider using a load balancer

We should also ensure the gateway supports failure by implementing different resiliency patterns,
such as Retry and Circuit Breaker.


### Overview of the Gateway Aggregation pattern

Aggregating multiple requests into one makes it easier for consumers of a microservices system to
interact with it; clients need to know about one endpoint instead of multiple.


### Overview of the Backend for Frontend pattern

With BFF, instead of building a general-purpose gateway, we build a gateway per user interface (for each application that interacts with the system), lowering the complexity.


### Mixing and matching gateways

For example, a gateway can be built for a single client (BFF), perform simple routing, and aggregate
results.
We can also mix gateways as different applications, for example, by putting multiple BFF gateways in
front of a more generic gateway to simplify their development and maintenance.


### Conclusion

A gateway is a facade that shields or simplifies access to one or more other services.


## Project – BFF

### Using Docker Compose to run the projects

#### Configuring HTTPS

First, we must generate a development certificate. In a PowerShell terminal, run the following commands

``` terminal
dotnet dev-certs https -ep "$env:APPDATA\ASP.NET\Https\adpg-net8-chapter-19. pfx" -p devpassword
dotnet dev-certs https --trust
```

The preceding commands create a pfx file with the password devpassword (you must provide a password,
or it won’t work), and then tell .NET to trust the dev certificates.

From there, the `ASPNETCORE_Kestrel__Certificates__Default__Path` and `ASPNETCORE_Kestrel__Certificates__Default__Password` environment variables are configured in the docker-compose.override.yml file and will use the development certificate.


### Creating typed HTTP clients using Refit

The concept is simple: we create one interface per service and translate its operation into methods.

We leverage Refit, an open-source library, to implement the interfaces automatically.

I used the out-of-the-box IHttpClientFactory functionalities in the past, so if you want to
reduce the number of dependencies in your project, you can also use that instead. Here’s
a link to help you get started: https://adpg.link/HCj7


### Creating a service that serves the current customer

To keep the project simple, we are not using any authentication or authorization middleware, yet we
want our BFF to be realistic and to handle who’s querying the downstream APIs.


Note: In a project that uses authentication, you can inject the `IHttpContextAccessor` interface into a class to access the current `HttpContext` object that contains a `User` property, enabling access to the current user’s `ClaimsPrincipal` object, which should include the current user’s `CustomerId`. Of course, you must ensure the authentication server returns such a claim. You must register the accessor using the following method before using it: `builder.Services.AddHttpContextAccessor()`.

### Features

#### Fetching the catalog

``` csharp
app.MapGet(
  "api/catalog",
  (IWebClient client, CancellationToken cancellationToken)
    => client.Catalog.FetchProductsAsync(cancellationToken)
);
```

#### Fetching the shopping cart

`Parallel.ForEachAsync()` used

``` csharp
var result = new ConcurrentBag<BasketProduct>();
await Parallel.ForEachAsync(basket, cancellationToken, async (item, cancellationToken) =>
{
  var product = await client.Catalog.FetchProductAsync(new(item.ProductId), cancellationToken);
  result.Add(new BasketProduct(product.Id, ...);
});
return result;
```

The `Parallel` class allows us to execute multiple operations in parallel, in this case, multiple HTTP
calls. There are many ways of achieving a similar result using .NET, and this is one of them.

Since the requests to the Products service are sent in parallel, we cannot predict the order they will
complete.


## Revisiting the CQRS pattern

Instead of simply creating a clear separation
between commands and queries, we can divide them even more using multiple microservices and
data sources to enhance scalability and flexibility. This approach allows each component to be scaled
independently based on demand, improving system performance and resource efficiency.

**CQS** is a principle stating that a method should either return data or mutate data, but not both. On
the other hand, **CQRS** suggests using one model to read the data and one model to mutate the data.

Figure 19.31: Microservices that apply CQRS to divide the reads and writes of a device’s location:
``` mermaid
graph LR
    %% Nodes for the Read Flow (Top)
    Actor((Actor))
    WebApp{{Web App}}
    ReadService{{Read Location Service}}
    ReadDB[(Read DB)]

    %% Nodes for the Write Flow (Bottom)
    Mobile{{Mobile App}}
    WriteService{{Write Location Service}}
    WriteDB[(Write DB)]

    %% Connections
    Actor --> WebApp
    
    WebApp --> ReadService
    ReadService --> ReadDB

    Mobile --> WriteService
    WriteService --> WriteDB

    %% Sync Connection
    WriteDB -- Update View --> ReadDB
```

Figure 19.32: Using Azure services to manage a CQRS implementation
``` mermaid
graph LR
    Actor((Actor)) --> WebApp{{Web App}}
    WebApp --> ReadService{{Read Location Service}}
    ReadService --> ReadDB[(Read DB)]

    MobileApp{{Mobile Device}} -- POST --> AF1{{Azure Function 1}}
    AF1 --> Publish[Publish LocationAdded]
    Publish --> Broker{{Message Broker & Event Store}}
    Broker -- When LocationAdded --> AF2{{Azure Function 2}}
    AF2 -- Update last known location --> ReadDB
```

The message broker is also the event store in the preceding diagram, but we could store events elsewhere,
such as in an Azure Storage Table, a time-series database, or an Apache Kafka cluster. Azure-wise,
the data store could also be CosmosDB.

SignalR mentioned on page 704

Note: Starting in ASP.NET Core 3.0, the ASP.NET Core team improved **distributed tracing**. Distributed
tracing is necessary to find failures and bottlenecks related to an event that flows
from one program to another (such as microservices). If something bugs out, it is important
to trace what the user did to isolate the error, reproduce it, and then fix it. The more
independent pieces there are, the harder it can become to make that trace possible. This
is outside the scope of this book, but it is something to consider if you plan to leverage
microservices.


## Overview of the Microservice Adapter pattern

The Microservice Adapter pattern allows us to add missing features, adapt one system to another, or
migrate an existing application to an event-driven architecture model, to name a few possibilities.

Here are the examples we cover next and the possible usages of this pattern:

### Adapting an existing system to another

### Decommissioning a legacy application

Doing this creates more complexity and is a temporary state.

With this new architecture in place, we can start migrating existing features away from the legacy
application into the new application without impacting the dependencies; we broke tight coupling.

From this point forward, we are applying the **Strangler Fig** pattern to migrate the legacy
system piece by piece to our new architecture.

In the preceding diagram, we can see that the new modern application has appeared. Each time we
deploy a new feature to the new application, we can remove it from the adapter, leading to a graceful
transition between the two models. At the same time, we are keeping the legacy application in place
to continue to provide the capabilities that are not yet migrated.

### Adapting an event broker to another

This pattern can be very useful for an IoT system where your microservices leverage Apache Kafka
internally for its full-featured suite of event-streaming capabilities, but they use MQTT to communicate
with the low-powered IoT devices that connect to the system. An adapter can solve this problem
by translating the messages from one protocol to the other.

