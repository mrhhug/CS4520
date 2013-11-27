#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
saveNewClub.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass
import cgi
from reoccuringhtml import cgiheader,htmlhead,htmltail,nullcheck
cgiheader()
htmlhead()

fldstor = cgi.FieldStorage()
clubname = fldstor.getvalue('clubname')
description = fldstor.getvalue('description')

if nullcheck(clubname,"clubname") == 0 and nullcheck(description,"description")== 0:
    classinstance= clubclass(None)
    newident=classinstance.fetch("SELECT MAX(ident) FROM club")[0][0]+1
    print "<h1>Saving New",clubname,"Club</h1><br>"
    print "Description is:",description,"<br>"
    classinstance.query('INSERT INTO club(ident,name,description) VALUES("'+str(newident)+'","'+clubname+'","'+description+'")')
    if fldstor.getvalue('international') == 'on':
        classinstance.query('INSERT INTO "belong_to" VALUES('+str(newident)+',110)')
        print "A member of the International club<br>"
    if fldstor.getvalue('sports') == 'on':
        classinstance.query('INSERT INTO "belong_to" VALUES('+str(newident)+',111)')
        print "A member of the Sports club<br>"
    print '<a href="../../index.html">Home</a><br>'
htmltail()
