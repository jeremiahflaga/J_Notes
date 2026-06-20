---
v-1.0.0: 2026-06-05 |
---

# Chapter 10: Logging Patterns

(mostly skim reading or inspectional reading)

The logging system is **provider-based**, meaning we must register one or more ILoggerProvider instances
if we want our log entries to be recorded somewhere, like in stdout or a file. **By default**, when calling
WebApplication.CreateBuilder(args), it registers the Console, Debug, EventSource, and EventLog
(Windows only) providers, but we can modify this list.

As a rule of thumb, I recommend using the `ILogger<T>` interface by default because it is the simplest
way; it removes the need to manage the category name manually, and it lowers the chances of making
a mistake while naming the category.

Based on our findings, I recommend using log message templates for Trace, Debug, and Information
messages. This approach is preferred over string interpolation (e.g., _logger.LogTrace($"Some:
{variable}")) and other methods like string.Format.

``` csharp
_logger.LogTrace("Some: {variable}", variable);
// Or
_logger.LogTrace("Some: {0}", variable);
```

As shown in the preceding code, log message templates allow the logging framework to delay the
processing of the message template and arguments until it’s sure it must log the message.

## Logging providers

built-in logging providers: 
 - Console
 - Debug
 - EventSource
 - EventLog
 - ApplicationInsights

third-party logging providers:
 - elmah.io
 - Gelf
 - JSNLog
 - KissLog.net
 - Log4Net
 - NLog
 - PLogger
 - Sentry
 - Serilog
 - Stackdriver

 ## Configuring logging

 ``` json
 {
   "Logging": {
      "LogLevel": {
         "Default": "Information",
         "Microsoft": "Warning"
   }
   }
}
```

`Logging:LogLevel:Microsoft`: representing base namespaces
 - every item part of the `Microsoft` or `Microsoft.*` namespaces have a minimum level of Warning

 We can also filter what we want to log on a provider basis, using configuration or code.

 ``` json
 {
    "Logging":
    {
        "LogLevel":
        {
            "Default": "Information",
            "Microsoft": "Warning"
        },
        "Console":
        {
            "LogLevel":
            {
                "Default": "Trace"
            }
        }
    }
}
```

Instead of configurations, we can use the AddFilter extension methods

``` csharp
using Microsoft.Extensions.Logging.Console;
// ...
builder.Logging.AddFilter<ConsoleLoggerProvider>(
   level => level >= LogLevel.Debug
);
```