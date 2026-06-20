# A Brief Networking Primer

from Heavy Wizardry 101, Early Access edition, 3/25/26
by David Martínez Oliveira, aka Pico

<small>eBook, PDF | purchased April 18, 2026 | HumbleBundle - Linux, the Good Stuff by No Starch | $1 ($3 for these 3 ebooks)</small>


## Types of Network Connections

1. Connection-oriented 
   - Implies that some kind of link is established between the two ends of the communication.
   - client and server

2. Datagram-oriented
   - A much simpler scheme where no consistent, exclusive connection is established between the two ends. Instead, whenever a program needs to send some data, it has to specify the intended recipient. Similarly, when a program receives data, it must determine who sent it.
   - Also called *connectionless* communication, this method blurs the line between client and server.

While these types of connection work differently, from a systems programming standpoint they both revolve around the same concept: **sockets**.

## Sockets

**Connection-oriented communication** requires the establishment of a
dedicated logical connection between two machines. The client creates a
socket when connecting to the server and associates the server’s address and
port with that socket. From that point on, it uses that **same socket** to send all
data to and receive all data from **that server**. There’s no need to specify the
destination for each message, because all messages are going to or coming
from the same server. By contrast, in **datagram-oriented communication**,
the destination of each message must be specified. This means the **same socket** can be used to exchange data with **different servers**.

## The Network and Transport Layers

network layer - Internet Protocol (IP)

The transport layer sits on top of the network layer and is in charge of ensuring
that the information flows between two machines in a network.

For internet communication, the transport layer primarily
uses two main protocols: the **Transmission Control Protocol (TCP)** and **User Datagram Protocol (UDP)**. **TCP is connection-oriented.** It takes measures to
ensure the data gets to the other end of the link, and it makes sure the data
arrives in the proper order. **UDP is datagram-oriented** and much simpler, as
it doesn’t care if packets arrive out of order, or if they even arrive at all. Each
protocol has its pros and cons, so which you use depends on what you need:
For example, TCP is more reliable, whereas UDP is faster.

The transport layer also introduces **port numbers**, which give us access to
different services on the same computer. There are no port numbers on any
level below this layer.

... In this analogy, an IP address is like the street name and building number.
It uniquely identifies a building, which here represents a machine. The
apartment number, identifying a specific apartment in that building, is like
a port. A given machine may have multiple ports. The applications running
on the machine are like the tenants in the apartments. If you want to send
data to a given application on a given machine, you need to know its IP address
(the street and building number) and its port (the apartment number).
Whenever there’s a tenant in the apartment that can open the door when
somebody rings the bell, the port is open. If there’s nobody in the apartment,
the port is closed.

For completeness, let’s also say there’s a guard at the door to the building
who doesn’t let unknown people visit specific apartments. That guard is
the **firewall**, and the inaccessible ports are **filtered**.

TCP -  long tube from one apartment to another
UDP - there’s no dedicated tube; you have to pay someone to take your data from one apartment to another, and each time you send something you have to tell the messenger the address of the apartment you want to send your stuff to.

-----
8.8.8.8 - a widely used, free public DNS (Domain Name System) server operated by Google. It is designed to be a fast, secure, and reliable alternative to the DNS servers provided by your Internet Service Provider (ISP).
-----
