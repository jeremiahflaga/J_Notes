---
v-1.0.0: 2025-05-02 | 
---

# Chapter 4: Exploring MVVM and Data Binding

\[In\] The MVC pattern... The model has no dependency on the view or the controller so it can be implemented and tested separately.

in MVVM, the view model is used to replace the controller

In both MVC and MVVM, the model can be tested separately. In MVVM, it is possible to design unit tests for the ViewModel as well.

## Data binding

in MVVM: Model – Item (access through interface IDataStore)

The data binding target has to be a child of `BindableObject`. 

QueryPropertyAttribute attribute - This is used to pass parameters during page navigation, and it will be introduced in the next chapter.

the binding expression: `<object property="{Binding bindProp1=value1[,bindPropN=valueN]*}" ... />`

 - example: `<Label Text="{Binding Path=Description}" FontSize="Small"/>`

 - The Path property is the default property

 - The `Source` property can be set to override `BindingContext`

When we set data binding to the target, we can use the following two members of the target class: 
• The BindingContext property gives us the source object 
• The SetBinding method specifies the target property and source property 

``` csharp
public ItemDetailPage()
{
    InitializeComponent();
    BindingContext = new ItemDetailViewModel();
    labelText.SetBinding(Label.TextProperty, "Text");
}
```

**Binding mode:**
- OneWay
- TwoWay
- OneWayToSource
- OneTime: It is a simpler form of the OneWay binding mode with
better performance.

`IsRefreshing="{Binding IsBusy, Mode=OneWay}"`

in the data binding setup, both the data binding target and source also need to implement the `INotifyPropertyChanged` interface so that when the property changes, a PropertyChanged event is raised to notify the change.

In an MVVM pattern, the viewmodel is usually the data binding source and we need to implement the `ç` interface in our viewmodels.

We need to create boilerplate code to define a property with change notification support. To simplify the code and autogenerate boilerplate code behind the scenes, we can use the MVVM Toolkit. 

{: .sidenote }
----- 
### MVVM Toolkit and INotifyPropertyChanged, from Google AI Gemini

The MVVM Toolkit (CommunityToolkit.Mvvm) simplifies INotifyPropertyChanged by using source generators to automatically create boilerplate code, eliminating manual property change notifications. By using the [ObservableProperty] attribute on private fields and inheriting from ObservableObject in a partial class, the toolkit generates public properties that automatically notify the UI of changes.

``` csharp
public partial class MyViewModel : ObservableObject
{
    [ObservableProperty]
    private string? _username; // Generates "Username" property
}
```

see https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm-community-toolkit-features

-----

### KPCLib

KPCLib is KeePassLib rebuilt as a .NET Standard 2.0 library

NuGet: https://www.nuget.org/packages/KPCLib/

GitHub: https://github.com/passxyz/KPCLib