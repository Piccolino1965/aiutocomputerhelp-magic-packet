# aiutocomputerhelp-magic-packet

https://www.aiutocomputerhelp.it/wake-on-lan-come-funziona-il-magic-packet-python-software/

This Python script implements the Wake-on-LAN (WoL) functionality, a protocol that allows turning on or waking up a computer on a network by sending it a Magic Packet via UDP

What does the code do?
Accepts a MAC address as input and cleans it from any separators (: or -).
Validates the MAC address by ensuring it has exactly 12 hexadecimal characters.
Constructs the Magic Packet, which consists of:
6 bytes of 0xFF (fixed prefix for WoL packets).
16 repetitions of the MAC address (48 bytes in total).
Sends the packet in broadcast via UDP on port 9, the standard port for WoL.
The script runs when executed directly and sends a Magic Packet to a device with the MAC 00:11:22:33:44:55.
