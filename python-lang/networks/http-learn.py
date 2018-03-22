import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.jeffrin.in',80))
s.send("GET /robots.txt HTTP/1.0\n\n")
print s.recv(1024)
s.close()
