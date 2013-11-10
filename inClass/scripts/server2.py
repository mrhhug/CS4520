'''
Created on Aug 14, 2013

Reverses string and sends back to the client

@author: Ben
'''

import socket

s = socket.socket()
s.bind(('',4444))
s.listen(1)

flag = ""

while flag != "END":
    (r,addr) = s.accept()
    print "connected to " + str(addr)
    flag = r.recv(1024)
    print "flag received " + flag
    rflag = flag[::-1]
    r.sendall(rflag)
    r.close()


s.close()


#if __name__ == '__main__':
#    pass