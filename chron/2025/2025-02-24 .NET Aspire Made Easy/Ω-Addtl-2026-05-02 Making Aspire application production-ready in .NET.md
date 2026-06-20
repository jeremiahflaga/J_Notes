
# Making Aspire application production-ready in .NET

https://fiodar.substack.com/p/making-aspire-application-production-ready-in-dotnet

by Fiodar Sazanavets

May 02, 2026


An open-source Aspire production readiness blueprint repo on GitHub: [Orion Aspire Starter](https://github.com/Orion-AI-Engineering/dotnet-aspire-enterprise-starter-blueprint)

`Directory.Packages.props`

`Directory.Build.props`

`global.json`


For a Postgres resource provisioned by Aspire, use `AddDatabase()`:

``` csharp
var postgres = builder.AddPostgres("postgresdb").WithPgAdmin();
var appDb = postgres.AddDatabase("appDb");
```

For connecting to existing legacy database, use `AddConnectionString()`

``` csharp
var postgres = builder.AddPostgres("postgresdb").WithPgAdmin();
var appDb = postgres.AddConnectionString("appDb");
```

`if (builder.ExecutionContext.IsRunMode)`

`if (builder.ExecutionContext.IsPublishMode)`