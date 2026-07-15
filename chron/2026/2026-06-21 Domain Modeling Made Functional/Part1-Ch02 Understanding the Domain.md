---
v-1.0.0: 2026-07-07 | July 9, 11
---

# CHAPTER 2: Understanding the Domain


The output of a workflow should always be the events that it generates, the
things that trigger actions in other bounded contexts. In our case, the output
of the workflow would be something like an “OrderPlaced” event, which is then
sent to the shipping and billing contexts.


## Documenting the Domain

Later in this book we’ll see how to create an accurate domain model in code,
but for now, let’s just create a simple text-based language that we can use to
capture the domain model:
• For workflows, we’ll document the inputs and outputs and then just use
some simple pseudocode for the business logic.
• For data structures, we’ll use AND to mean that both parts are required,
such as in Name AND Address. And we’ll use OR to mean that either part is
required, such as in Email OR PhoneNumber.

Using this mini-language, then, we can document the Place Order workflow
like this:

```
Bounded context: Order-Taking

Workflow: "Place order"
  triggered by:
    "Order form received" event (when Quote is not checked)
  primary input:
    An order form
  other input:
    Product catalog
  output events:
   "Order Placed" event
  side-effects:
    An acknowledgment is sent to the customer, along with the placed order
```

And we can document the data structures associated with the workflow
like this:

```
bounded context: Order-Taking

data Order =
  CustomerInfo
  AND ShippingAddress
  AND BillingAddress
  AND list of OrderLines
  AND AmountToBill

data OrderLine =
  Product
  AND Quantity
  AND Price

data CustomerInfo = ??? // don't know yet
data BillingAddress = ??? // don't know yet
```


## Diving Deeper into the Order-Taking Workflow

As developers, we tend to focus on technical issues and treat all requirements
as equal. Businesses do not think that way. Making money (or saving money)
is almost always the driver behind a development project. If you are in doubt
as to what the most important priority is, follow the money!


## Representing Complexity in Our Domain Model

### Representing Constraints

```
context: Order-Taking

data WidgetCode = string starting with "W" then 4 digits
data GizmoCode = string starting with "G" then 3 digits
data ProductCode = WidgetCode OR GizmoCode
```

The right answer depends on the context, as always. Generally though, it’s
important to capture the design from the domain expert’s point of view.

Now, what about documenting the requirements for the quantities? Here’s
the proposed design:

```
data OrderQuantity = UnitQuantity OR KilogramQuantity
data UnitQuantity = integer between 1 and ?
data KilogramQuantity = decimal between ? and ?
```

```
data UnitQuantity = integer between 1 and 1000
data KilogramQuantity = decimal between 0.05 and 100.00
```

### Representing the Life Cycle of an Order

In our earlier design sketch, we had a simple
definition for Order:

But now it’s clear that this design is too simplistic and doesn’t capture how
Ollie thinks of orders. In Ollie’s mental model, orders have a life cycle. They
start off as unvalidated (straight from the mail), then they get “validated,” and
then they get “priced.”

The easiest way to do that is by creating new names for each phase: Unvalidated-
Order, ValidatedOrder, and so on.

```
data UnvalidatedOrder =
  UnvalidatedCustomerInfo
  AND UnvalidatedShippingAddress
  AND UnvalidatedBillingAddress
  AND list of UnvalidatedOrderLine

data UnvalidatedOrderLine =
  UnvalidatedProductCode
  AND UnvalidatedOrderQuantity
```

```
data ValidatedOrder =
  ValidatedCustomerInfo
  AND ValidatedShippingAddress
  AND ValidatedBillingAddress
  AND list of ValidatedOrderLine

data ValidatedOrderLine =
  ValidatedProductCode
  AND ValidatedOrderQuantity
```

```
data PricedOrder =
  ValidatedCustomerInfo
  AND ValidatedShippingAddress
  AND ValidatedBillingAddress
  AND list of PricedOrderLine   // different from ValidatedOrderLine
  AND AmountToBill              // new

data PricedOrderLine =
  ValidatedOrderLine
  AND LinePrice                 // new
```

```
data PlacedOrderAcknowledgment =
  PricedOrder
  AND AcknowledgmentLetter
```

### Fleshing out the Steps in the Workflow

```
workflow "Place Order" =
  input: OrderForm
  output:
    OrderPlaced event (put on a pile to send to other teams)
    OR InvalidOrder (put on appropriate pile)

  // step 1
  do ValidateOrder

  ...

  // step 2
  do PriceOrder

  // step 3
  do SendAcknowledgmentToCustomer

  // step 4
  return OrderPlaced event (if no errors)

```
```
substep "ValidateOrder" =
  input: UnvalidatedOrder
  output: ValidatedOrder OR ValidationError
  dependencies: CheckProductCodeExists, CheckAddressExists

  ...
```

```
substep "PriceOrder" =
  input: ValidatedOrder
  output: PricedOrder
  dependencies: GetProductPrice

  ...
```