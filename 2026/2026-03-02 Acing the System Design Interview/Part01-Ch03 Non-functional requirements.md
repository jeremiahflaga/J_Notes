= Chapter 3: Non-functional requirements

:v-1.0.0: 2026-03-21 | (up to 2026-03-28)

== Quotes

Functional requirements describe the inputs and outputs of the system. You can represent them as a rough API specification and endpoints.

[sidebar]
(Reread "Chapter 2: Writing Great Feature Specifications" of the book "Software Test Design" by Simon Amey)


Consistency has different meanings in ACID and CAP (from the CAP theorem). ACID consistency focuses on data relationships like foreign keys and uniqueness. As stated in Martin Kleppmann's Designing Data-Intensive Applications (O'Reilly, 2017), CAP consistency is actually linearizability, defined as all nodes containing the same data at a moment in time, and changes in data must be linear; that is, nodes must start serving the changes at the same time.

... tradeoffs between linearizability vs. eventual consistency

[sidebar]
(is linearizability an alternative term to strong consistency / immediate consistency)



---
On CAP Theorem, see:

The CAP Theorem. The Bad, the Bad, & the Ugly - https://www.dtornow.com/blog/the-cap-theorem/

Please stop calling databases CP or AP
Published by Martin Kleppmann on 11 May 2015.

Designing Data-Intensive Applications by Martin Kleppmann
---