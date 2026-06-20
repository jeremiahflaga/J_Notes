---
v-1.0.0: 2025-11-07 | Chapters 1, 2, and 1/3 of Chapter 3 only
v-1.0.1: 2026-04-28 | 
---

# Chapter 3: User Interface Design with XAML

In the constructor of the App class, the `InitializeComponent()` method is called to load the XAML and parse it. UI elements defined in the XAML file are created at this point. We can access these UI elements by the name defined with the `x:Name` attribute,

``` csharp
public partial class App : Application
{
    public App()
    {
        InitializeComponent();
        
        ...

    }
}
```