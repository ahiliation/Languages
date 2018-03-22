import socket
import sys

toolbar_width = 40

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['                                                                       
# file = open("Linux-Voice-Issue-003.pdf", 'w')


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.linuxvoice.com', 80))
mysock.send('GET http://www.linuxvoice.com/issues/003/Linux-Voice-Issue-003.pdf  HTTP/1.0\n\n')


while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
    sys.stdout.write("-")
    sys.stdout.flush()

mysock.close()
sys.stdout.write("\n")
