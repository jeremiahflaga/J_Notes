= Chapter 1: Getting Started with .NET MAUI

:v-1.0.0: 2025-11-07 | Chapters 1, 2, and 1/3 of Chapter 3 only
:v-1.0.1: 2026-04-23 | 


In 2019, Apple announced a new framework, SwiftUI. Using SwiftUI, developers can build user interfaces using the Swift language in a declarative way directly.

.NET MAUI app can target the following platforms: 
 - Android 5.0 (API 21) or higher 
 - iOS 10 or higher 
 - macOS 10.13 or higher, using Mac Catalyst 
 - Windows 11 and Windows 10 version 1809 or higher, using Windows UI Library (WinUI) 3 

.NET MAUI Blazor apps use the platform-specific WebView control, so they have the following additional requirements: 
 - Android 7.0 (API 24) or higher 
 - iOS 14 or higher 
 - macOS 11 or higher, using Mac Catalyst 



== Misc: Get Started With .NET MAUI for Mobile Development in Mac

https://medium.com/@thushfdo/get-started-with-net-maui-for-mobile-development-in-mac-61f3aa1b45ee

by Thushantha Fernando

Mar 29, 2025

Step 01 — Install .NET SDK

Step 02 — Install Visual Studio Code

Step 03 — Install Extensions on VSCode
 - ".NET MAUI" (This also installs dependencies like "C# Dev Kit" and ".NET Install Tool")

Step 04 — .NET MAUI workload
 - `sudo dotnet workload install maui`
 - `dotnet workload list`

Step 05 — Install Xcode (from App Store)
 - Then, install Xcode command-line tools with `xcode-select --install`
