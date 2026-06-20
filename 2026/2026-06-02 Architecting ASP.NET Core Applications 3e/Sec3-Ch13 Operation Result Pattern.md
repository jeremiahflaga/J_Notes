---
v-1.0.0: 2026-06-06 |
---

# Chapter 13: Operation Result Pattern

An operation result aims to communicate the success or failure of an operation to its caller. It
also allows that operation to return both a value and one or more messages to the caller.

also known as the Result Object pattern

Imagine any system where you want to display user-friendly error messages, achieve some small
speed gain by returning an object instead of throwing an exception, or even handle failure easily and
explicitly. The Operation Result design pattern can help you achieve these goals.

NOTE: Always focus on your **needs first**, then use your imagination and knowledge to find the best solution. Software engineering is not only about applying techniques that others tell you to. It’s an art! The difference is that you are crafting software instead of painting or woodworking, and most people won’t see any of that art (code) or get it even if they do.

## Project – Implementing different Operation Result patterns

The simplest form of the Operation Result pattern • 438
A single error message • 440
Adding a return value • 442

``` csharp
namespace OperationResult.SingleErrorWithValue;
public record class OperationResult
{
  public bool Succeeded => string.IsNullOrWhiteSpace(ErrorMessage);
  public string? ErrorMessage { get; init; }
  public int? Value { get; init; }
}
```

Multiple error messages • 443

``` csharp
namespace OperationResult.MultipleErrorsWithValue;

public record class OperationResult
{
  public OperationResult()
  {
    Errors = ImmutableList<string>.Empty;
  }
  public OperationResult(params string[] errors)
  {
    Errors = errors.ToImmutableList();
  }
  public bool Succeeded => !HasErrors();
  public int? Value { get; init; }
  public IReadOnlyCollection<string> Errors { get; init; }
  public bool HasErrors()
  {
    return Errors?.Count > 0;
  }
}
```

Adding message severity • 445
(see book)

Sub-classes and factories • 450
(see book)


## Project – Registration Application

``` csharp
using System.Diagnostics.CodeAnalysis;
namespace RegistrationApp;

public record class ConcertRegistrationResult
{
  [MemberNotNullWhen(false, nameof(ErrorMessage))]
  [MemberNotNullWhen(true, nameof(ConfirmationNumber))]
  public bool RegistrationSucceeded { get; init; }

  public User User { get; init; } = null!;
  public Concert Concert { get; init; } = null!;
  public string? ConfirmationNumber { get; init; }
  public string? ErrorMessage { get; init; }
  
  private ConcertRegistrationResult() { }

  public static ConcertRegistrationResult CreateSuccess(User user, Concert
  concert, string confirmationNumber)
  {
    return new()
    {
      RegistrationSucceeded = true,
      User = user,
      Concert = concert,
      ConfirmationNumber = confirmationNumber,
    };
  }

  public static ConcertRegistrationResult CreateFailure(User user, Concert
  concert, string errorMessage)
  {
    return new()
    {
      RegistrationSucceeded = false,
      User = user,
      Concert = concert,
      ErrorMessage = errorMessage,
    };
  }
}
```

guaranteeing that a confirmation number is provided when registration succeeds and an error
message is present when it fails. The **`MemberNotNullWhen`** attributes allow the compiler to know that
when consuming the code

``` csharp
builder.Services.Configure<JsonOptions>(o => {
  o.SerializerOptions.DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull;
});
```

tells the IoC container to configure the JsonOptions class so that the ASP.NET Core serializer omits the null properties, leading to a clean output.

Now, let’s look at the consumer of the Operation

``` csharp
app.MapPost(
  "/concerts/{concertId}/register",
  async Task<Results<Ok<ConcertRegistrationResult>, BadRequest<ConcertRegistrationResult>>> (
    int concertId, ConcertRegistrationService service) =>
{
  // Simulate fetching objects
  var user = GetCurrentUser();
  var concert = GetConcert(concertId);

  // Execute the operation
  var result = await service.RegisterAsync(user, concert);

  // Handle the operation result
  if (result.RegistrationSucceeded)
  {
    return TypedResults.Ok(result);
  }
  else
  {
    await LogErrorMessageAsync(result.ErrorMessage);
    return TypedResults.BadRequest(result);
  }
});
```

Have you noticed that the LogErrorMessageAsync method takes a string as a parameter,
but the ErrorMessage property is a nullable string (string?)? If you look at the code in Visual
Studio, you’ll realize that the compiler does not complain about this, which is a result of
using the MemberNotNullWhen attribute that I added to the ConcertRegistrationResult
class. Without the attribute, the compiler would warn you with the following error message:

CS8604: Possible null reference argument for parameter 'message' in 'Task
LogErrorMessageAsync(string message)'.

## Advantages and disadvantages