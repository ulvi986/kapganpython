from scapy.all import *

# Paket yakalama işlevi
def packet_handler(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"IP paketi tespit edildi - Kaynak IP: {ip_src}, Hedef IP: {ip_dst}")
    if packet.haslayer(ICMP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"ICMP paketi tespit edildi - Kaynak IP: {ip_src}, Hedef IP: {ip_dst}")
    if packet.haslayer(TCP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"TCP paketi tespit edildi - Kaynak IP: {ip_src}, Hedef IP: {ip_dst}")
    if packet.haslayer(UDP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"UDP paketi tespit edildi - Kaynak IP: {ip_src}, Hedef IP: {ip_dst}")

# Paket yakalama başlatma
sniff(prn=packet_handler)
