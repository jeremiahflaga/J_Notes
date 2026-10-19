---
v-1.0.0: 2026-09-20 | and Sept 23
---

# Chapter 6: Advanced Blazor Development

In this chapter, we will learn how to develop advanced Blazor components, gaining a deeper understanding of their architecture and lifecycle. We will explore event handling in Blazor, a crucial aspect of creating responsive and dynamic user interfaces. Additionally, we will cover state management techniques that ensure your applications run smoothly and efficiently, maintaining a consistent state across different components and user interactions.


## Exploring Blazor components and lifecycle

### Component parameters

``` csharp
<GrandChildComponent
    @bind-Title="Title"
    OnTitleChanged="OnGrandChildComponentEvent">
</GrandChildComponent>
```

The `@bind-Title="Title"` attribute binds the
Title property of GrandChildComponent to the Title property of the current component.
This means that any changes to the Title property in either component will automatically update the other.



{: .sidenote }
----- 

why does the title input box change back to original "title" text after clicking on the  Update Title button?


The issue is in `ParentComponent.razor`:
```razor
<GrandChildComponent Title="Title" OnTitleChanged="OnGrandChildComponentEvent"></GrandChildComponent>
```

`Title="Title"` passes the **literal string `"Title"`** as the parameter — it's not bound to `ParentComponent`'s own `Title` property (`@Title`). So every time `ParentComponent` re-renders (which happens after `OnGrandChildComponentEvent` runs and calls `StateHasChanged` implicitly via the event chain), Blazor re-assigns `GrandChildComponent.Title` back to the hard-coded `"Title"` string, overwriting whatever the user typed in the `<input @bind="Title" />`.

**Fix:** bind it to the parent's actual `Title` field using `@`:
 1. Modifying ParentComponent.razor
Now `GrandChildComponent.Title` is properly bound to `ParentComponent.Title`, so on re-render it reflects the actual current value instead of being reset to the literal string `"Title"` every time.

Summary: In `ParentComponent.razor`, `Title="Title"` was passing the literal text `"Title"` (not the `@Title` field) as a parameter to `GrandChildComponent`. Each re-render re-applied this hardcoded value, wiping out what you typed into the input. Changed it to `Title="@Title"` to correctly bind the parameter.

-----


### Lifecycle methods

Understanding the lifecycle methods of Blazor components is crucial for managing initialization, state
changes, and clean-up tasks. The key lifecycle methods include `OnInitialized`, `OnParametersSet`,
and `OnAfterRender`.

`OnAfterRenderAsync(bool firstRender)`

`Dispose`:


### Enabling component communication

Component communication is essential for building complex applications where different components
need to interact. You can achieve this through **event callbacks** and **shared services**.