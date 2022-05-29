# "Cyber Threats and Attack Vectors" Course on Coursera
## WEEK 1: Authentication based attacks

There are four common factors used for authentication:

    Something you know (such as a password)

    Something you have (such as a smart card)

    Something you are (such as a fingerprint or other biometric method)

    Something you do (such as voice pattern, handwriting)
 
![Authentication based attacks Coursera](https://github.com/emreYbs/Picus-Security-Bootcamp/blob/main/Week%202/Coursera/Cyber%20Threats%20and%20Attack%20Vectors/Screenshot%202022-05-29%20at%2013-57-06%20Authentication%20based%20attacks%20Coursera.png)

There are some extra files in this Week 1 Module of the course and if needed, download via: <br>
lecture slides are available at:
https://academics.uccs.edu/greg/Coursera/Practical_Computer_Security/Course2/

https://www.coursera.org/learn/cyber-threats-attack-vectors/supplement/cIIW1/lecture-slides)

## WEEK 2: Network and system based attacks

- Watch on Youtube: https://www.youtube.com/watch?v=aeA7rDq4CnM

![Week 2 Network based attacks Coursera](https://github.com/emreYbs/Picus-Security-Bootcamp/blob/main/Week%202/Coursera/Cyber%20Threats%20and%20Attack%20Vectors/Week%202%20Network%20based%20attacks%20Coursera.png)

There's really two different kinds of attacks.There's active attacks and there's passive attacks.
**Active attacks** are _much more common_, because we're trying to get information real time. 

Passive attacks are when an attacker can read the data
from an active attack and use the information obtained for other purposes.
In active attacks we see this in sniffing, eavesdropping,
spoofing and denial of service attacks,
whereas passive attacks, what is seen there is more compromised data.
So password manipulation for example.
Let's dive into each one of these.

**Denial of Service attacks are very hard to mitigate.**

Our first active attack is going to be sniffing.
Sniffing is the most common type of active attack.
It is reading, monitoring or capturing the full packets from a network device.
So that could be from a computer,
that could be from a switch or a router or other,
well, it could be from a webcam.

Segmenting your network is one of the simplest ways that you can use to protect yourself,
because then we're only sniffing a small segment of information.
Protecting your network physically is also something that you need to do.
If we have physical access to a piece of equipment,
we may be able to break-in via console cable or something like that and guess
the username and password
for that piece of networking equipment and use that against somebody.

If you were a small business or an individual that cannot
afford to purchase enterprise grade hardware,
understand who is on your network.
Understand who is using your network.
Don't allow outsiders to connect to your private networks.
This is especially the case in wireless networks. 

## Mobile Based Attacks

The following video will help explain mobile based attacks and the damage that they are currently doing.

Rise of Mobile Threats | Gagan Singh | TEDxHongKongSalon - https://www.youtube.com/watch?v=zXgUUWmuoLw 


## Lecture Slides

The course lecture slides can also be found at:
https://academics.uccs.edu/greg/Coursera/Practical_Computer_Security/Course2/ 

## Wireless Attacks

- Some terms to know:

**SSID**:which is short for Service Set Identifier. 

**Wireless security** is the prevention of unauthorized access or damage to computers or data using wireless networks, which include Wi-Fi networks. The term may also refer to the protection of the wireless network itself from adversaries seeking to damage the confidentiality, integrity, or availability of the network. The most common type is Wi-Fi security, which includes Wired Equivalent Privacy (WEP) and Wi-Fi Protected Access (WPA). WEP is an old IEEE 802.11 standard from 1997.

A **replay attack** _(also known as a repeat attack or playback attack)_ is a form of network attack in which valid data transmission is maliciously or fraudulently repeated or delayed. This is carried out either by the originator or by an adversary who intercepts the data and re-transmits it, possibly as part of a spoofing attack by IP packet substitution. This is one of the lower-tier versions of a man-in-the-middle attack. **Replay attacks are usually passive in nature.** ✔️ 

Suppose Alice wants to prove her identity to Bob. Bob requests her password as proof of identity, which Alice dutifully provides (possibly after some transformation like hashing, or even salting, the password); meanwhile, Eve is eavesdropping on the conversation and keeps the password (or the hash). After the interchange is over, Eve (acting as Alice) connects to Bob; when asked for proof of identity, Eve sends Alice's password (or hash) read from the last session which Bob accepts, thus granting Eve access.

## **Prevention of Replay Attacks**

Replay attacks can be prevented by tagging each encrypted component with a session ID and a component number. This combination of solutions does not use anything that is interdependent on one another. Due to the fact that there is no interdependency, there are fewer vulnerabilities. This works because a unique, random session ID is created for each run of the program; thus, a previous run becomes more difficult to replicate. In this case, an attacker would be unable to perform the replay because on a new run the session ID would have changed.

Session IDs, also known as session tokens, are one mechanism that can be used to help avoid replay attacks. The way of generating a session ID works as follows.

    Bob sends a one-time token to Alice, which Alice uses to transform the password and send the result to Bob. For example, she would use the token to compute a hash function of the session token and append it to the password to be used.
    On his side Bob performs the same computation with the session token.
    If and only if both Alice’s and Bob’s values match, the login is successful.
    Now suppose an attacker Eve has captured this value and tries to use it on another session. Bob would send a different session token, and when Eve replies with her captured value it will be different from Bob's computation so he will know it is not Alice.

Session tokens should be chosen by a random process (usually, pseudorandom processes are used). Otherwise, Eve may be able to pose as Bob, presenting some predicted future token, and convince Alice to use that token in her transformation. Eve can then replay her reply at a later time (when the previously predicted token is actually presented by Bob), and Bob will accept the authentication.

One-time passwords are similar to session tokens in that the password expires after it has been used or after a very short amount of time. They can be used to authenticate individual transactions in addition to sessions. These can also be used during the authentication process to help establish trust between the two parties that are communicating with each other.

Bob can also send nonces but should then include a message authentication code (MAC), which Alice should check.

Timestamping is another way of preventing a replay attack.[3] Synchronization should be achieved using a secure protocol. For example, Bob periodically broadcasts the time on his clock together with a MAC. When Alice wants to send Bob a message, she includes her best estimate of the time on his clock in her message, which is also authenticated. Bob only accepts messages for which the timestamp is within a reasonable tolerance. Timestamps are also implemented during mutual authentication, when both Bob and Alice authenticate each other with unique session IDs, in order to prevent the replay attacks. The advantages of this scheme are that Bob does not need to generate (pseudo-) random numbers and that Alice doesn't need to ask Bob for a random number. In networks that are unidirectional or near unidirectional, it can be an advantage. The trade-off being that replay attacks, if they are performed quickly enough i.e. within that 'reasonable' limit, could succeed. 

**Real World Replay Attack Example** : _In the folk tale Ali Baba and the Forty Thieves, the thieves' captain used the passphrase "Open, Simsim" to open the door to their loot depot. This was overheared by Ali Baba who later reused the passphrase to get access and collect as much of the loot as he could carry._

https://en.wikipedia.org/wiki/Replay_attack

## Defenses

- Wireless security is just an aspect of computer security; however, organizations may be particularly vulnerable to security breaches caused by rogue access points.

If an employee (trusted entity) brings in a wireless router and plugs it into an unsecured switchport, the entire network can be exposed to anyone within range of the signals. Similarly, if an employee adds a wireless interface to a networked computer using an open USB port, they may create a breach in network security that would allow access to confidential materials. However, there are effective countermeasures (like disabling open switchports during switch configuration and VLAN configuration to limit network access) that are available to protect both the network and the information it contains, but such countermeasures must be applied uniformly to all network devices. 

- use trusted networks.
- Don't necessarily use your local coffee shop's network or use a VPN.
Secured SSIDs or secure SSIDs are using well known and secure protocols.
So WPA2, for example, that is using AS encryption would be the best security that you could have
on a non-commercial based access point. 

Ad hoc networks can pose a security threat. Ad hoc networks are defined as [peer to peer] networks between wireless computers that do not have an access point in between them. While these types of networks usually have little protection, encryption methods can be used to provide security.

The security hole provided by Ad hoc networking is not the Ad hoc network itself but the bridge it provides into other networks, usually in the corporate environment, and the unfortunate default settings in most versions of Microsoft Windows to have this feature turned on unless explicitly disabled. Thus the user may not even know they have an unsecured Ad hoc network in operation on their computer. If they are also using a wired or wireless infrastructure network at the same time, they are providing a bridge to the secured organizational network through the unsecured Ad hoc connection. 

Identity theft (or MAC spoofing) occurs when a hacker is able to listen in on network traffic and identify the MAC address of a computer with network privileges. Most wireless systems allow some kind of MAC filtering to allow only authorized computers with specific MAC IDs to gain access and utilize the network. However, programs exist that have network “sniffing” capabilities. Combine these programs with other software that allow a computer to pretend it has any MAC address that the hacker desires, and the hacker can easily get around that hurdle.

MAC filtering is effective only for small residential (SOHO) networks, since it provides protection only when the wireless device is "off the air". Any 802.11 device "on the air" freely transmits its unencrypted MAC address in its 802.11 headers, and it requires no special equipment or software to detect it. Anyone with an 802.11 receiver (laptop and wireless adapter) and a freeware wireless packet analyzer can obtain the MAC address of any transmitting 802.11 within range. In an organizational environment, where most wireless devices are "on the air" throughout the active working shift, MAC filtering provides only a false sense of security since it prevents only "casual" or unintended connections to the organizational infrastructure and does nothing to prevent a directed attack. 

A man-in-the-middle attacker entices computers to log into a computer which is set up as a soft AP (Access Point). Once this is done, the hacker connects to a real access point through another wireless card offering a steady flow of traffic through the transparent hacking computer to the real network. The hacker can then sniff the traffic. One type of man-in-the-middle attack relies on security faults in challenge and handshake protocols to execute a “de-authentication attack”. This attack forces AP-connected computers to drop their connections and reconnect with the hacker's soft AP (disconnects the user from the modem so they have to connect again using their password which one can extract from the recording of the event). Man-in-the-middle attacks are enhanced by software such as LANjack and AirJack which automate multiple steps of the process, meaning what once required some skill can now be done by script kiddies. Hotspots are particularly vulnerable to any attack since there is little to no security on these networks. 

The Caffe Latte attack is another way to defeat WEP. It is not necessary for the attacker to be in the area of the network using this exploit. By using a process that targets the Windows wireless stack, it is possible to obtain the WEP key from a remote client. By sending a flood of encrypted ARP requests, the assailant takes advantage of the shared key authentication and the message modification flaws in 802.11 WEP. The attacker uses the ARP responses to obtain the WEP key in less than 6 minutes

Source I used: https://en.wikipedia.org/wiki/Wireless_security

