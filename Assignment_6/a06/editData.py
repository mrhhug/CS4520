#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
editdata.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass
import cgi
from reoccuringhtml import error,cgiheader,htmlhead,htmltail
cgiheader()
htmlhead()

classinstance= clubclass(cgi.FieldStorage().getvalue('ident'))
if cgi.FieldStorage().getvalue('ident') == None:
	print error(1)
if classinstance.finalArgCheck():
	print error(classinstance.finalArgCheck())
else:
	print "<h1>Edit ",classinstance.clubName(),"Club</h1>"
	print "<form action=saveEdits.py method=post>"
	print "<div class=data-grid>"
	print "<table>"
	print "<tr><td>Id: </td><td><input name=ident type=text value=",classinstance.ident()," readonly></td></tr>"
	print "<tr><td>Name: </td><td><input name=clubname type=text value=",classinstance.clubName(),"></td></tr>"
	print "<tr><td>Description: </td><td><input name=description size=35 type=text value='"+classinstance.clubDescription()+"'></td></tr>"
	print "</table>"
	print "<h2>Choose the Club President</h2>"
	print "The current president, if there is one, is pre-selected<br><br>"
	members=classinstance.listofMembers()
	if members == []:
		print "<i>this club has no members, and this site has no way to add one</i>"
	else:
		print "<select name=prez>"
		print "<option value=",classinstance.clubPresident(),">",classinstance.clubPresident(),"</option>"
		for j in members:
			if j != classinstance.clubPresident():
				print "<option value=",j,">",j,"</option>"
		print "</select>"
	groups = classinstance.listofGroups()
	print "<h2>Select Groups</h2>"
	print "<input type=checkbox name=international value=True "
	if 'International' in groups:
		print "checked"
	print ">International<br>"
	print "<input type=checkbox name=sports value=True "
	if 'Sports' in groups:
		print "checked"
	print ">Sports<br><br>"
	print "<button type=submit value=Submit>Save Changes</button>"
	print "<button type=reset value=Reset>Cancel</button><br>"
htmltail()
