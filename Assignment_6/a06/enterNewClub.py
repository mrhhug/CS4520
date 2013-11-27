#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
enterNewClub.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass
from reoccuringhtml import cgiheader,htmlhead,htmltail,readwritecheck
cgiheader()
htmlhead()

if readwritecheck()==0:
    print "<h1>Enter Data for a New Club</h1>"
    print "<form action=saveNewClub.py method=post>"
    print "<div class=data-grid>"
    print "<table>"
    print "<tr><td>Name: </td><td><input name=clubname type=text></td></tr>"
    print "<tr><td>Description: </td><td wide><input name=description size=35 type=text></td></tr>"
    print "</table>"
    print "<h2>Select Groups</h2>"
    print "<input type=checkbox name=international>International<br>"
    print "<input type=checkbox name=sports>Sports<br><br>"
    print "<button type=submit value=Submit>Save Changes</button>"
    print "<button type=reset value=Reset>Cancel</button>"
    print "<br>"
htmltail()
