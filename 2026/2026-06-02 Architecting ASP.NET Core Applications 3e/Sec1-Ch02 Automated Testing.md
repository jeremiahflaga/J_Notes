---
v-1.0.0: 2026-06-03 |
---

# Chapter 2: Automated Testing

The **testing diamond** redistributes the test ratio to focus more on integration. It is a great strategy for
integration-heavy systems, like REST APIs and microservices... The testing diamond is the strategy we employ the most in the book, especially in Section 4, Application Patterns.

Why are we talking about tests in an architectural book? Because testability is a sign of a good design.

**End-to-end** tests focus on application-wide behaviors, such as what happens when a user clicks on a
specific button, navigates to a particular page, posts a form, or sends a PUT request to some web API
endpoint. E2E tests usually run on infrastructure to test your application and deployment.

Other types of tests: load testing, performance testing, regression testing, contract testing, penetration testing, functional testing, smoke testing, and more; UI tests

When it is an option, I recommend evaluating the possibility of writing fewer meaningful integration
tests that assert the correctness of a use case over a suite of mock-heavy unit tests. Remember to
always keep the execution speed in mind.

## Managing technical debt

**Technical debt** refers to the cost of additional rework

The most crucial point is understanding that you cannot avoid technical debt altogether, so it’s better
to embrace that fact and learn to live with it instead of fighting it.

pioneer


## Testing approaches

test-driven development (TDD), acceptance test-driven development (ATDD), and behavior-driven development (BDD)

### BDD

Practitioners of BDD often leverage the User Story Template and the given–when–then grammar to
formalize their test cases, making them readable by non-developers. BDD test output must also be
readable by non-developers to allow stakeholders to consult and understand the artifacts.

The **User Story Template** — _As a… I want to… So That…_ — is a framework used in Agile development for
articulating user stories, focusing on user requirements and their value... (see book for an example)

The **given–when–then template** defines the way to describe the behavior of a user story or acceptance
test... (see book for an example)

For the sake of simplicity, we stick to unit testing, integration testing, and a bit of TDD in the book.


## Testing techniques

White-box testing, Black-box testing, Gray-box testing


## Test case creation

Multiple ways exist to break down and create test cases to help find software defects with a minimal
test count. Here are some techniques to help minimize the number of tests while maximizing the
test coverage:
• Equivalence partitioning
• Boundary value analysis
• Decision table testing
• State transition testing
• Use case testing

(see also book on testing: Software Test Design )


## xUnit

**TheoryAttribute**

For more complex test cases, we can use theories. A theory contains two parts:
• A [Theory] attribute that marks the method as a theory
• At least one data attribute that allows passing data to the test method: [InlineData],
[MemberData], or [ClassData]

**Fixture**

On top of the FactAttribute, TheoryAttribute, and assertions, xUnit offers other mechanisms that
allow developers to inject dependencies into their test classes and share state between test cases.

Fixtures allow dependencies to be reused by all test methods of a test class
by implementing the IClassFixture<T> interface. Fixtures are very helpful for costly dependencies,
like creating an in-memory database. **With fixtures, you can create the dependency once and use it multiple times.**

You can also share the dependency provided by the fixture between multiple test classes by using
ICollectionFixture<T>, [Collection], and [CollectionDefinition] instead.


## Organizing your tests

I typically set up a unit test project for each project within the solution, along with one or more dedicated integration test projects.

### Unit tests

Test code inside the test class

``` csharp
namespace MyApp.IntegrationTests.Controllers;

public class ValuesControllerTest
{
  public class Get : ValuesControllerTest
  {
    [Fact]
    public void Should_return_the_expected_strings()
    {
      // Arrange
      var sut = new ValuesController();

      // Act
      var result = sut.Get();

      // Assert
      Assert.Collection(result.Value,
        x => Assert.Equal("value1", x),
        x => Assert.Equal("value2", x)
      );
    }
  }
}
```

Don’t go too hard on reusability inside your test classes, as it can make tests harder to read
from an external eye, such as a reviewer or another developer who needs to play there.


### Integration tests

Name the test classes in a way that mimics
your requirements, organize those into sub-folders (maybe a category or group of requirements), and
code test cases as methods.

``` csharp
[Route("")]
[ApiController]
public class HelloWorldController : ControllerBase
{
  [HttpGet]
  public string Hello()
  {
    return "Hello World!";
  }
}
```

test code:

``` csharp
using Microsoft.AspNetCore.Mvc.Testing;
using System.Net;
using Xunit;
namespace MyApp.IntegrationTests.Controllers;

public class HelloWorldControllerTest : IClassFixture<WebApplicationFactory<Startup>>
{
  private readonly HttpClient _httpClient;
  public HelloWorldControllerTest(WebApplicationFactory<Startup> webApplicationFactory)
  {
    _httpClient = webApplicationFactory.CreateClient();
  }

  public class Hello : HelloWorldControllerTest
  {
    public Hello(WebApplicationFactory<Startup> webApplicationFactory)
      : base(webApplicationFactory) { }

    [Fact]
    public async Task Should_respond_a_status_200_OK()
    {
      // Act
      var result = await _httpClient.GetAsync("/");

      // Assert
      Assert.Equal(HttpStatusCode.OK, result.StatusCode);
    }

    [Fact]
    public async Task Should_respond_hello_world()
    {
      // Act
      var result = await _httpClient.GetAsync("/");
      
      // Assert
      var contentText = await result.Content.ReadAsStringAsync();
      Assert.Equal("Hello World!", contentText);
    }
  }
}
```

We inject a WebApplicationFactory<Startup> object into
the constructor by implementing the IClassFixture<T> interface.

#### Alternative to using fixtures

instead of injecting the instance using the IClassFixture interface, we instantiate the factory
manually. To ensure we dispose of the WebApplicationFactory instance, we can also implement
the IAsyncDisposable interface.

``` csharp
namespace MyMinimalApiApp;
public class ProgramTestWithoutFixture : IAsyncDisposable
{
  private readonly WebApplicationFactory<Program> _webApplicationFactory;
  private readonly HttpClient _httpClient;

  public ProgramTestWithoutFixture()
  {
    _webApplicationFactory = new WebApplicationFactory<Program>();
    _httpClient = _webApplicationFactory.CreateClient();
  }

  public ValueTask DisposeAsync()
  {
    return ((IAsyncDisposable)_webApplicationFactory)
    .DisposeAsync();
  }

  // Omitted nested Get class
}
```

#### Creating a reusable test application

``` csharp
namespace MyMinimalApiApp;
public class MyTestApplication : WebApplicationFactory<Program> {}
```


### Important testing principles

One essential thing to remember when writing tests is to test use cases, not the code itself; we are
testing features’ correctness, not code correctness.

To help with that, test requirements should revolve around inputs and outputs.

Another concept is to divide those units as a query or a command.

what if a unit must perform multiple operations, such as reading
from a database, and then send multiple commands? You can create and test multiple smaller units
(individual operations) and another unit that orchestrates those building blocks, allowing you to test
each piece in isolation. We explore how to achieve this throughout the book.
