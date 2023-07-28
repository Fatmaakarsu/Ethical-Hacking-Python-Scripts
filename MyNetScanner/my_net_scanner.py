""""

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