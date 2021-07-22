import os
import sys
import socket

host = input("Host: ")
port = int(input("Port: "))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((host,port))
except:
    print("Couldn't connect on %s:%d" % (host,port))
packet = input("Send: ")
s.send(packet)
print("Sent packet to %s:%d" % (host,port))
print(s.recv(4096))
