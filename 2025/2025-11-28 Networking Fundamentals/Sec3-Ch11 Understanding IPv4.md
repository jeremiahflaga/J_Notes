---
v-1.0.0: 2025-11-28 | Preface, First part of Chapter 11
v-1.0.1: 2026-05-13 | up t0 2026-05-14, Rereading Chapter 11
---

# Chapter 11: Understanding IPv4

IP addresses provide a hierarchical means of identifying devices on networks. Hierarchical in this context means that we can identify which network an IP address resides on through the use of the IP address and it's subnet mask.

An IPv4 address itself represents **two elements**: the network element and the host element. The **network element** tells us which network the IP address resides on, while the **host element** identifies the host on that particular network. The demarcation between the two is dependent on which **subnet mask** is being used.

Each IPv4 address has to be **unique** in its own network, and if it is a public IP address, it has to be **unique** in the World to prevent issues. To ensure that public IP addresses are unique, the **Internet Assigned Numbers Authority (IANA)** issues blocks of IP addresses to **regional registrars** for further dissemination. Each of these registrars is responsible for issuing blocks of IP addresses to **ISPs**, who may in turn issue IP addresses to **lower-level ISPs** who then issue them to the **public** or **organizations**.

While private IP addresses don't have to be unique in the World, they have to be unique within their own subnet.

## Understanding classful networks

A classful network always has a predefined number of bits allocated to the network element of the IP address, and therefore a predefined subnet mask.

In terms of classful networks, there are five classes: A, B, C, D, and E. Classes A, B, and C
have their own IP address ranges, default subnet masks, a maximum number of hosts, and
private address ranges. Classes D and E have their own IP address ranges but do not
require the other attributes.


|  | Class A: | Class B: | Class C: |
| :--- | :--- | :--- | :--- |
| **Address range:** | 0.0.0.0 - 127.255.255.255 | 128.0.0.0 - 192.255.255.255 | 192.0.0.0 - 223.255.255.255 |
| **Default subnet mask:** | 255.0.0.0 or /8 | 255.255.0.0 or /16 | 255.255.255.0 or /24 |
| **IP addresses available:** | 16,777,216 or 2^24 | 65,536 or 2^16 | 256 or 2^8 |
| **Maximum number of hosts:** | 16,777,214 | 65,534 | 254 |
| **Private address range:** | 10.0.0.0 - 10.255.255.255 | 172.16.0.0 - 172.31.255.255 | 192.168.0.0 - 192.168.255.255 |


in a Class A network, if 8 bits
are for the network, then that leaves 24 bits for the host element (32 - 8 = 24); ... The
number of bits for the host element tells us **how many IP addresses we can have per network**. The calculation is 2^n, where n is the number of bits available for the host
element. I have included this in the preceding attributes.

Note that the maximum number of hosts is always 2 fewer than the number of IP addresses
available. This is because, in each network, the first and last IP address have a special
purpose and cannot be issued to hosts. The first IP address in any network is referred to as
the **Network ID (or address)** and the last IP address in a network is referred to as the
**broadcast ID (or address)**. We tend to see the **Network ID** being used in conjunction with a
subnet mask in the routing table of any device with an IP address. This is usually to tell the
router that the traffic that's destined for the specified network needs to go through a
specified interface in the routing table.

the Network ID is also used on Windows hosts for routing purposes (see image in book)

The **broadcast ID** is an IP address that is used to communicate to all the devices on that
particular network. Rather than listing all the individual IP addresses on a network, or
sending out individual transmissions to all the devices on the network, I can use the
broadcast IP address to communicate with them all in one go.


**Class D** compromises a range of IP addresses that are set aside for multicast transmission
purposes, and cannot be assigned specifically to an individual host. The range is
224.0.0.0 – 239.255.255.255.

**Class E** is set aside for mainly experimental purposes, and like Class D it cannot be
assigned to an individual host. The range is 240.0.0.0 – 255.255.255.255. An
important IP address to note is 255.255.255.255. This specific address is used to send
broadcast communications to all the devices in network without them having to know any
specifics about the IP address range of that network.


## Understanding subnet masks

A subnet is a smaller network within a larger network.

A **subnet mask** tells you which part of the IP address is a **network element** and which part is the **host element**.

At a basic level, when your computer wants to communicate with a remote device, it uses
its own subnet mask and IP address to identify its own network element. It runs a similar
comparison using its own subnet mask and the destination IP address to identify what it
**presumes** to be the network element of the destination device. If the two network elements
match, then it assumes they are on the same network and they will communicate directly. If
they do not match, then it assumes they are not on the same network and all the
communication is sent via the **default gateway**.

Subnet masks will only contain the values **128, 192, 224, 240, 248, 252, 254, or 255**. If you see any other values in octets, then assume it is
incorrect. If you are wondering why this is the case, think back to the
binary tables we used. Since a subnet mask in binary format consists of
continuous 1s starting from the left, it restricts us to these values.

### Classful/default subnet masks

To identify the **network element** of a classful IP address, we compare it to its subnet mask. If an octet in the subnet mask has a 255 in it, then its respective octet in the IP address is part of the network element.

## Understanding CIDR

CIDR provides us with the means of escaping from default subnet masks, thus allowing us
to be more flexible in sizing our networks. Do you only want two hosts? Not a problem –
we can create a subnet mask for that. CIDR is a key component in **Variable Length Subnet Masks (VLSMs)**. VLSMs offer you the ability to break your network down into smaller
networks of various sizes (as opposed to having multiple smaller networks all of the same
size).

I'm going to use the `13.45.89.1` IP address and the `255.255.255.192` subnet mask for
this example.


| Host IP | 13 | 45 | 89 | 1 |
| :--- | :---: | :---: | :---: | :---: |
| Subnet | 255 | 255 | 255 | 192 |
| Host (Binary) | 0 0 0 0 1 1 0 1 | 0 0 1 0 1 1 0 1 | 0 1 0 1 1 0 0 1 | 0 0 0 0 0 0 0 1 |
| Subnet (Binary) | 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 | 1 1 0 0 0 0 0 0 |
| Network ID (Binary) | 0 0 0 0 1 1 0 1 | 0 0 1 0 1 1 0 1 | 0 1 0 1 1 0 0 1 | 1 1 0 0 0 0 0 0 |
| **Network ID** | 13 | 45 | 89 | 192 |

Using the subnet from the preceding example, 255.255.255.192, this translates into a `/26` CIDR notation.

the Network ID is always the first IP address in a network
and that the broadcast address is the last IP address in a network



to find the broadcast ID... we flip the [rightmost] zeroes [of the Network ID] into ones.


| Host IP | 13 | 45 | 89 | 1 |
| :--- | :---: | :---: | :---: | :---: |
| Subnet | 255 | 255 | 255 | 192 |
| Host (Binary) | 0 0 0 0 1 1 0 1 | 0 0 1 0 1 1 0 1 | 0 1 0 1 1 0 0 1 | 0 0 0 0 0 0 0 1 |
| Subnet (Binary) | 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 | 1 1 0 0 0 0 0 0 |
| Network ID (Binary) | 0 0 0 0 1 1 0 1 | 0 0 1 0 1 1 0 1 | 0 1 0 1 1 0 0 1 | 1 1 1 1 1 1 1 1 |
| **Broadcast Address** | 13 | 45 | 89 | 255 |


## Assigning IP addresses to hosts


An IP address can either be assigned manually by an administrator or dynamically through
Dynamic Host Configuration Protocol (DHCP). We will talk about DHCP in more detail in
Chapter 14, Network Services.

Manually assigning an IP address to a Windows computer involves adjusting the IPv4
properties of the NIC itself. Since a device can have more than one NIC, ensure you are
configuring the right one. Let's walk through configuring an IP address manually: (see book on page 308)

(Note: Latest Windows 11 version has different steps to configuring IP address manually than waht is presented in the book.)

By default, your adapter will be set to obtain an IP address automatically. Note
that not only is it getting the IP address automatically but it will also be given a
default gateway and DNS settings automatically:

You may have noticed that, while you were obtaining an IP address, there was an
Alternate Configuration tab.

- This tab details what the computer should do if it cannot obtain an IP address
automatically. By default, it will be provided with an Automatic Private IP
Addressing (APIPA) address, which always starts with 169.254.x.x.



Sometimes, you may find that you have problems with the IP address that's been issued by
DHCP. You can ask your computer to either release the IP address or renew the IP address
from the command line using ipconfig /release and ipconfig /renew, respectively.
Release gives up the IP address and doesn't attempt to get a new IP address; renew also
releases the IP address but attempts to obtain an IP address again.