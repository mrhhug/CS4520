'''
Created on Aug 14, 2013

@author: Ben
'''

import socket

s = socket.socket()	#create a plain sock
s.bind(('',4444))	# bind a port: now its a listener
s.listen(1)		# become a listener: wait queue of size 1

flag = ""

while flag != "END":
	#wait for a connectio
	#r is a connected socket
	#addr is the other host
    (r,addr) = s.accept()
    print "connected to " + str(addr)
    flag = r.recv(1024)
    print "flag received " + flag
    r.close()


s.close()


#if __name__ == '__main__':
#    pass
