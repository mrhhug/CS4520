'''
Created on Sep 9, 2013

Query the clubs database using sqlite3
@author: jim
'''

import sqlite3

conn = sqlite3.connect('clubs.db')
cur = conn.cursor()

cmd = 'select * from person'
cur.execute(cmd)

for row in cur:
    print row
    
x = cur.fetchone()
print x # there is no data left

cmd = 'select ident, description, name from `group`'
cur.execute(cmd)

x = cur.fetchone()
print x
x = cur.fetchone()
print x
x = cur.fetchone()
print x

# get the club with ID 108
ident =108
cmd = 'select name from club where ident='+str(ident)
cur.execute(cmd)
x = cur.fetchone()
print x

print "----------------"

# get clubs with description containing string 'Die'
substring = 'Die%'
cmd = "select name from club where description like '" + substring + "'"
cur.execute(cmd)
for row in cur :
    print row

cmd = "select name,ident from club where description like ?"
substring = "Die%"
# cur.execute(cmd,substring) #bad and will error
cur.execute(cmd,(substring,))
for row in cur:
    print row
    
print "----------------"