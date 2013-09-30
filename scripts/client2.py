'''
Created on Aug 14, 2013

@author: Ben
'''

import socket
import sys

s = socket.socket()

s.connect(('localhost',4444))
if len(sys.argv) > 1:
    flag = sys.argv[1]
else:
    flag = "default flag"
s.send(flag)
print s.recv(1024)
s.close()
