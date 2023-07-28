""""
Overall Explanation:
These commands use Scapy, a Python library for network packet manipulation, to perform an ARP (Address Resolution Protocol) scan. 
The code creates an ARP request packet for the "10.0.2.1/24" subnet, combines it with an Ethernet broadcast packet, 
sends the combined packet over the network, and captures the responses. 
The answered_list variable stores the devices that responded to the ARP request, and unanswered_list stores the devices that did not respond. 
The answered_list.summary() displays a summary of the responses, providing the MAC addresses of devices with 
IP addresses in the "10.0.2.1/24" subnet. This can be helpful for network scanning and analysis purposes.
"""

import scapy.all as scapy

#1- arp request
#2- broadcast
#3- response


arp_request_pacjet = scapy.ARP(pdst="10.0.2.1/24")
#scapy.ls(scapy.ARP())

broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
scapy.ls(scapy.Ether())

# scapy dilinde 2 paketimi al tek paket haline getir demek
combined_packet = broadcast_packet/arp_request_pacjet

(answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
answered_list.summary()
