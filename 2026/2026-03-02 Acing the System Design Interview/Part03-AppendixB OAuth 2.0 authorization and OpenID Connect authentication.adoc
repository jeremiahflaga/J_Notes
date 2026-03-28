= Appendix B: OAuth 2.0 authorization and OpenID Connect authentication

:v-1.0.0: 2026-03-28 |

== Quotes

OAuth Flows

1. authorization code flow (involves both back channel and front
channel)
2. implicit flow (front channel only)
3. resource owner password credentials (back channel only), not recommended for new applications
4. client credentials (back channel only)
5. Authorization code flow with PKCE (Proof Key for Code Exchange), used in Native mobile apps

So, the only technical difference between OAuth 2.0 and OpenID Connect is that
OpenID Connect returns both an access code and ID token, and OpenID Connect
provides a user info endpoint. A client can request the authorization server for an
OpenID scope in addition to its desired OAuth 2.0 scopes and obtain both an access
code and ID token.

[sidebar]
(see also "CHAPTER 7 API Authentication and Authorization" of "Mastering API Architecture: Design, Operate, and Evolve API-Based Systems")

== Recall / Retrieval

