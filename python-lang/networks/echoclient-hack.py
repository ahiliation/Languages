#!/usr/bin/env python

import socket

host = 'localhost'
port = ['25','22','21']
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,21))
s.send("USER J"+"\r\n")
data = s.recv(size)
s.close()
print 'Received:', data
