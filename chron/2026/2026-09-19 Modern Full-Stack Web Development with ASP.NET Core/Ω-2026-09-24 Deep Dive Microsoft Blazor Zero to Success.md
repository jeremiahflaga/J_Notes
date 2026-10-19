---
v-1.0.0: 2026-09-24 | and 25, 26, Oct 11
---

# Deep Dive: Microsoft Blazor Zero to Success | Visual Studio Live! Las Vegas 2026

https://www.youtube.com/watch?v=qgkM6-ftwSA


9,660 views  Apr 21, 2026  #VisualStudio #dotnet #csharp
Want to build modern, interactive web apps with C# and .NET instead of relying on JavaScript frameworks? In this @VisualStudioLive session from Visual Studio Live! Las Vegas 2026, Rocky Lhotka walks through how Blazor works, when to use it, and how to build real applications across web, desktop, and mobile using a unified .NET stack.

🔑 What You’ll Learn
• What Blazor is and how it compares to Angular, React, WPF, and Windows Forms
• Differences between Blazor Server, WebAssembly, Auto, and Hybrid render modes
• How to choose the right hosting model for performance and scalability
• Creating a Blazor app in Visual Studio 2026 and understanding project structure
• Routing, layouts, components, and render modes in real applications
• Building forms, validation, and interactive UI with Razor components
• Data access with dependency injection and real-world patterns
• Authentication and authorization with cookies, claims, and Entra ID
• Styling with CSS isolation, Bootstrap, and Sass
• Extending Blazor to PWAs and native apps with .NET MAUI Hybrid

⏱️ Chapters
Part 1: Blazor Basics
02:31 What Blazor is and where it runs
04:18 History of Microsoft UI frameworks (WinForms, WPF, ASP.NET, Silverlight)  
11:15 WebAssembly explained and the origin of Blazor  
14:54 Blazor hosting models: Server, WebAssembly, Auto, and Hybrid
22:47 Stateful vs stateless apps and Blazor architecture 
30:30 How Blazor Server works (SignalR and real-time UI updates)  
34:19 Creating a new Blazor Web App in Visual Studio and understanding project structure  
45:00 Razor components, routing, and layouts  
58:08 Interactive pages, code-behind, and component behavior
1:05:27 How Blazor rendering works and performance implications

Part 2: Going Deeper
1:17:01 Data access and dependency injection patterns  
1:29:30 Forms, validation, and reusable input components
1:35:37 ASP.NET Core authentication and authorization in Blazor
2:02:39 Entra ID login and Microsoft Graph integration
2:05:24 Styling with CSS isolation, Bootstrap, and Sass
2:11:19 Blazor Hybrid, PWAs, and native app scenarios

👤 Speaker
Rocky Lhotka
Principal Consultant, Xebia

🔗 Links
• Download Visual Studio 2026: http://visualstudio.com/download
• Explore more VS Live! Las Vegas sessions: https://aka.ms/VSLiveLV26
• Join upcoming VS Live! events: https://aka.ms/VSLiveEvents

#blazor #csharp #dotnet #VisualStudio2026 #VisualStudio #vslive


==============================

2:15

In speakers opinion, it is by far the best UI Framework that has been created by Microsoft since 1991.

11:10

Mozilla created WASM

14:00

SignalR

When Blazor was released, it as a server-side technology with experimental WebAssembly stuff.

Now roll forward... Blazor 8, two years ago, merged the two .. Blazor 10 today.



22:40

## Different ways that we can host Blazor


![](_attachments/20260925003406%20Blazor%20Hosting%20Models.png)


23:00

### Blazor Server, or Server Interactive Mode

Advantages: 
- all code running on web server
- startup time - short

Drawbacks:
- can't run offline

It scales to several hundred concurrent users without any problem.

Scale to thousands of concurrent users - needs specialized on how to make Azure work - complicated and expensive.

When Blazor is running on the server, it is **stateful**, not stateless.

A lot of the world still use stateful - (credit card systems, plane flight seat reservation)


### Blazor WebAssembly, WASM

Pure client-side app. The reason you have a server at all is to deploy the code.

DLLs get downloaded (WebAssembly binaries, not Windows binaries)

Advantage:
- scales almost infinitely because all of your code is running in the client device

Drawback:
- startup cost


### Auto Mode

Came in Blazor 8

Needs a little bit of knowledge and work that you and I have to have to make this possible. But a lot of the heavy lifting is actually done by Blazor itself.


### Hybrid

Creating a native app using Blazor - Windows, Mac, iOS, Android


### Flowchart for choosing between modes

![](_attachments/20260925010046%20Flowchart%20for%20choosing%20between%20modes.png)



32:00

## N-Tier Blazor Architecture

- Server-Rendered
- Blazor Server
- Blazor WebAssembly
- Blazor Hybrid
- (Client-side Only Apps)



34:00

## Sample

Visual Studio 2026 Blazor Templates - shown in video


45:00

`.AddAdditionalAssemblies(typeof(BlazorApp13.Client._Imports).Assem...`

- this is where it finds all your Razor pages
- figuring out the navigation routes


46:30

App.razor

<head> tag

Routes.razor


Weather.razor

@attribute [StreamRendering]

 - Loading... message at the start of the video


57:00

Don't put business logic in razor files.



58:00

## Lifecycle

OnInitializeAsync()
- get data from db


1:01:30

consistency within a codbase always wins
 - this was on the issue on (or not) having separate code behind razor.cs files


1:03:00

@rendermode InteractiveAuto / InteractiveServer / InteractiveWebAssembly

 - needed if you want interactivity
 - one of the common early bugs that everybody encounters with Blazor


StateHasChanged();

override ShouldRender()



1:10:00

You can know at runtime the current render mode

Auto render mode (starting in Blazor 8) - non-interactive at first, then switches to interactive mode.

``` csharp
@if (RendererInfor.IsInteractive)
{

}
```

You also have the option of turning off what is called server pre-rendering, in which case the user just sees a blank page until it flops into interactive.


1:17:40

Blazor is the first UI framework that is absolutely built on top of dependency injection. You can't do Blazor without DI.

Every prior UI Framework, even ASP.NET Core, which integrates DI tightly, you can actually technically use ASP.NET Core without DI.

Every request to the server in ASP.NET Core gets a scope. (Scoped vs Transient vs Singleton)

Singleton - one per process.

1:26:00

(the time where he compares/contrasts the server project with the .Client project, where he mentioned something about class library DLL being downloaded referring to the DLL for .Client)

1:39:00

Authentication, Authorization

`<CascadingAuthenticationState>` in Routes.razor
- now gets access to the current user authentication state.

`<AuthorizeRouteView>` - 404 (not 402, for security reasons)

`<AuthorizeView>`, `<Authorized>`, `<NotAuthorized>`

1:42:00

Login page (Login.razor)
- no render mode, because it's going to use HttpContext. In order to safely use HttpContext, you must be in a non-interactive page. As a general rule, it's not safe to use HttpContext in interactive pages.

`<EditForm>` works differently in non-interactive pages

`ClaimsIdentity` - this is the only identity thing that works in ASP.NET Core and Blazor

Claims - allows you to say "this data is available only to people in Europe", or "only available to admins that are in Georgia, or in US West region"


1:52:00

`AuthenticationStateProvider`


1:56:00

When the page is rendering or running in the browser, how does it get at the user identity?


2:02:00

Sample project `BlazorEntraId` (Entra ID)

`AddMsalAuthentication(...)`

All modern authentication is a two-step process:
1. Verify your credentials - prove the user is who they say they are
2. Go get the user profile - get roles, profile, etc.



2:05:00

Styling, CSS, SCSS,

DartSassBuilder nuget package


2:11:20

Blazor being used to create a native app.

PWA - Progressive Web App
 - Created by Google
 - Chromebooks - run Google Sheets offline
 - Manifest file


Blazor app wrapped in MAUI (MAUI Hybrid)
 - Native apps
 - App Store, Play Store









