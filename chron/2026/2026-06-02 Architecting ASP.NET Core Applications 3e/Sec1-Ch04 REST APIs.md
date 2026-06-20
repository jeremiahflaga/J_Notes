---
v-1.0.0: 2026-06-04 | skipped for now, except for Versioning section
---

# Chapter 4: REST APIs


(skipped for now, except for Versioning section)


## Versioning

**Default versioning strategy:** What happens when no version is specified?

1. API returns an error if no version is specified
2. always to return the first version
3. always to return the latest version
4. pick any version as the default baseline for the API

**Versioning strategy**

1. URL patterns to define and include the API version, like https://localhost/v2/some-entities
   - (debatably) violates REST key principle of one endpoint pointing to a unique resource
2. use HTTP headers
   - use a custom header like api-version or Accept-version, for example, or the standard Accept header