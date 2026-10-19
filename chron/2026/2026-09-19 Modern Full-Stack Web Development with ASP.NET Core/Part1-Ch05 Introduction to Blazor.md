---
v-1.0.0: 2026-09-19 | and Sept 20, need to review Blazor; will be reading chapters on Blazor only
---

# Chapter 5: Introduction to Blazor




### Blazor hosting models

In the **WebAssembly hosting model**, the Blazor application is executed directly in the browser
using WebAssembly.

The **server-side hosting model** uses a constant SignalR connection between the server and the client
to update the state of UI components.


## Key features of Blazor

### Component-based architecture

#### Creating a simple component

``` csharp
<button @onclick="OnClick">@ButtonText</button>

@code {
    [Parameter] public string ButtonText { get; set; }
    [Parameter] public EventCallback OnClick { get; set; }
}
```

Let’s look at this SimpleButton component:
- The ButtonText parameter allows the button text to be set by the parent component
- The OnClick parameter is EventCallback that enables the parent component to specify what happens when the button is clicked

#### Using the SimpleButton component

``` csharp
@page "/parent-simple-button";
<h3>ParentComponentSimpleButton</h3>

<SimpleButton
    ButtonText="Click me" OnClick="ShowMessage"
/>

<p>@Message</p>

@code {
    private string Message;

    private void ShowMessage()
    {
        Message = "Button clicked";
    }
}
```

#### Nested components and parameter cascading

`[CascadingParameter]`

`<CascadingValue Value="sharedData">`


#### Lifecycle methods


#### Component communication'

Components can communicate with each other through parameters and events.



### Data binding

One-way data binding

Two-way data binding

Advanced example – contact form with validation


#### Component interaction



### Routing

Blazor uses the Router component to manage routing. The Router component is typically defined
in the App.razor file

(see book for example, and explanation)

Blazor also supports **parameterized routes**, allowing data to be passed through the URL,

``` csharp
@page "/product/{id:int}"

...

@code {
    [Parameter] public int Id { get; set; }
}
```

The Id property in the @code block is decorated with the [Parameter] attribute to bind the
route parameter.

Additionally, you can define **optional parameters** in routes

``` csharp
@page "/user/{name?}"

...

@code {
    [Parameter] public string Name { get; set; } = "Guest";
}
```

Furthermore, you can work with **catch-all parameters** to capture the remainder of the URL

``` csharp
@page "/search/{*query}"

...

@code {
    [Parameter] public string Query { get; set; }
}
```

Route constraints

Navigation and navigation with state - `NavigationManager` service

Handling navigation events and nested routing

Nested routing





