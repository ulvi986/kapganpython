import scapy.all as scapy
from scapy.all import *

#from scapy.all import *



print(sniff(count=4)) #sniff - koklanmis paketler hakkinda bazi, yani onun TCP,UDP veya diger bir protokol oldugunu bize gosterir.
print(sniff(count=4, prn = lambda x : x.summary())) #.summary() ile paket cevaplarinin kisa metnini gorek icin kullanilir.
print(sniff(count=4, prn = lambda x : x.show() )) #.show ile biz protokol hakkinda tam olaraq bilgi alabiliriz






