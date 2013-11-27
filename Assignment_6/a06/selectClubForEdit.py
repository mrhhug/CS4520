#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
selectClubforEdit.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass
from reoccuringhtml import *
cgiheader()
htmlhead()

if readwritecheck()==0:
    x=clubclass(None).fetch('select * from club')             
    print '''
            <h1>Select a Club to Display</h1>
    <form action="editData.py" method="get">
    <select name="ident">
            '''
    for i in x:
            classinstance= clubclass(str(i[0]))
            print "<option value=",classinstance.ident(),">",classinstance.clubName(),"</option>"

    print '''
    </select>
    <br><br>
     <input type="submit" value="Display">
     </form>
        '''
htmltail()
