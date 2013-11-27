#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
save.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass
import cgi
from reoccuringhtml import nullcheck,cgiheader,htmlhead,htmltail
cgiheader()
htmlhead()

fldstor = cgi.FieldStorage()
classinstance= clubclass(fldstor.getvalue('ident'))
clubname = fldstor.getvalue('clubname')
description = fldstor.getvalue('description')

if nullcheck(clubname,"clubname") == 0 and nullcheck(description,"description")== 0:
    changeflag=False
    print "<h1>Saving Edits for",classinstance.clubName(),"</h1><br>"
    if clubname != classinstance.clubName():
        changeflag=True
        oldname = classinstance.clubName()
        classinstance.query('UPDATE club SET name="'+clubname+'" WHERE ident='+classinstance.ident())
        print "A change in the clubname from '"+oldname+"' to '"+classinstance.clubName()+"' completed succesfully<br>"
	        
    if description != classinstance.clubDescription():
	    changeflag=True
	    oldname = classinstance.clubDescription()
	    classinstance.query('UPDATE club SET description="'+description+'" WHERE ident='+classinstance.ident())
	    print "A change in the description from '"+oldname+"' to '"+classinstance.clubDescription()+"' completed succesfully<br>"

    if fldstor.getvalue('prez') != classinstance.clubPresident():
        changeflag=True
        oldname = classinstance.clubPresident()
        classinstance.query('UPDATE club SET president_id="'+str(classinstance.personIdent(fldstor.getvalue('prez')))+'" WHERE ident='+classinstance.ident())
        print "A change in the president from '"+oldname+"' to '"+classinstance.clubPresident()+"' completed succesfully<br>"
	
    if "International" in classinstance.listofGroups():
	    if not fldstor.getvalue('international'):
		    changeflag=True
		    classinstance.query('DELETE FROM belong_to WHERE club_id="'+str(classinstance.ident())+'" AND group_id="110"')
		    print "The International group was removed<br>"
    else:
	    if fldstor.getvalue('international'):
		    changeflag=True
		    classinstance.query('INSERT INTO belong_to(group_id, club_id) VALUES(110,'+str(classinstance.ident())+')')
		    print "The International group was added<br>"
		
    if "Sports" in classinstance.listofGroups():
	    if not fldstor.getvalue('sports'):
		    changeflag=True
		    classinstance.query('DELETE FROM belong_to WHERE club_id="'+str(classinstance.ident())+'" AND group_id="111"')
		    print "The Sports group was removed<br>"
    else:
	    if fldstor.getvalue('sports'):
		    changeflag=True
		    classinstance.query('INSERT INTO belong_to(group_id, club_id) VALUES(111,'+str(classinstance.ident())+')')
		    print "The Sports group was added<br>"
    if not changeflag:
            print "You did not mak any changes<br>"
    print "<a href=selectClubForEdit.py>Choose another club to edit</a><br>"
htmltail()
