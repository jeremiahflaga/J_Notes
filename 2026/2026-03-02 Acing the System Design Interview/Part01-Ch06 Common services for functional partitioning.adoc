= Chapter 6: Common services for functional partitioning

:v-1.0.0: 2026-04-18 | 


Developers should declare REST resources as cacheable whenever possible, a practice which carries advantages...

Use the Expires, Cache-Control, ETag, and Last-Modified HTTP headers for
caching.

We should be cautious when using GraphQL for external APIs. It is similar to exposing a database and allowing clients to make SQL queries.