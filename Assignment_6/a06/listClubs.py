#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
listClubs.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass
from reoccuringhtml import cgiheader,htmlhead,htmltail,readcheck
cgiheader()
htmlhead()

if readcheck()<1:
	x = clubclass(None).fetch('select * from club')
	print "<ul>"
	for i in x:
		    classinstance=clubclass(str(i[0]))
		    print "<li>",classinstance.clubName()
		    print "<ul>"
		    print "<li>ident:",classinstance.ident(),"</li>"
		    print "<li>description:",classinstance.clubDescription(),"</li>"
		    print "<li>President:",classinstance.clubPresident(),"</li>"
		    print "<li>Club has these members:</li>"
		    print "<ul>"
		    for j in classinstance.listofMembers():
		            print "<li>",j,"</li>"
		    print "</ul>"
                    listmem = classinstance.listofGroups()
                    if len(listmem)==1:
                        print "<li>club belongs to this group:</li><ul>"
                        print "<li>",listmem[0],"</li>"
                    else:
                        print "<li>club belongs to these groups:</li><ul>"
			for j in listmem:
			        print "<li>",j,"</li>"
		    print "</ul></ul></li>"    
	print "</ul>"
htmltail()
