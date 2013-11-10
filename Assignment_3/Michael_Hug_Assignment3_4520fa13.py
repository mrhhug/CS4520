#!/usr/bin/python2
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
Assignment 3
23 September 2013
This script uses Sqlite
'''
import sqlite3
import sys

''' change the following string to match the db filename '''
dbfile = 'clubs.db'

#function to do all the database fetches, defaults to fetchall
def fetch(query, num=-1):
	conn = sqlite3.connect(dbfile)
	cur = conn.cursor()
	cur.execute(query)
        if (num ==1):
            x=cur.fetchone()
        else:
            x=cur.fetchall()
	conn.close()
	return x

#function to do inital arg check, checks to be sure there is exactly one argument and ensures that argument can be converted to int, nonzero returns are bad
def initialArgCheck():
	if (len(sys.argv)<2):
		return 1
	if (len(sys.argv)>2):
		return 2
	try:
		int(sys.argv[1])
	except ValueError:
		return 3
	return 0
		
#function to check that database file exist and checks to see if file contains a sqlite3 hex header, nonzero returns are bad
def dbFileCheck():
	try:
		with open(dbfile):
			pass
	except IOError:
		return 4 
	f = open(dbfile, "rx")
	header = f.read(16).encode('hex')
	f.close()
	#see http://www.sqlite.org/fileformat.html#database_header magic header string
	if header != "53514c69746520666f726d6174203300": 
		return 5 
	return 0

#This check should be called 3rd, after we are sure there is exactly one int argument and that we are using a sqlite3 file; Querys the database and checks to make sure the argument is within the possible range, and then if that club_id actually exists, nonzero returns are bad
def finalArgCheck():
	x= fetch('SELECT ident FROM club order by ident asc;')
	if not (int(sys.argv[1])>=int(x[0][0])):
		return 6 
	if not (int(sys.argv[1])<=int(x[len(x)-1][0])):
		return 7 
        x=fetch('select name from club where ident='+sys.argv[1],1)
        if (x==None):
                return 8
	return 0

#function returns the name of a person when personid is the function argument
def personName(personid):
        return fetch('select name from person where ident='+str(personid),1)[0]

#function returns the name of a group when the group_id is the function argument
def groupName(group_id):
        return fetch('select name from clubgroup where ident='+str(group_id),1)[0]

#returns the club name based on the script argument
def clubName():
	return str(fetch('select name from club where ident='+sys.argv[1],1)[0])
	
#returns the club description based on the script argument
def clubDescription():
	return str(fetch('select description from club where ident='+sys.argv[1],1)[0])

#returns the list of groups based on script argument(group_id)
def listofGroups():
	x=fetch('select group_id from belong_to where club_id='+sys.argv[1])
        List = [i[0] for i in x]
        for i in range (0,len(List)):
            List[i] = str(groupName(List[i]))
	return List

#returns the list of members based on the script argument(group_id)
def listofMembers():
        x=fetch('select personid from member_of where clubid='+sys.argv[1])
        List = [i[0] for i in x]
        for i in range (0,len(List)):
            if str(personName(List[i]))==clubPresident():
                List[i] = str(personName(List[i]))+'*'
            else:   
                List[i] = str(personName(List[i]))
        return List

#returns the club president based on the script argument(group_id)
def clubPresident():
	x=fetch('select president from club where ident='+sys.argv[1],1)
	return personName(str(x[0]))

#prints error message and exits with nonzero exit status
def printErrors(error):
	if (error == 1):
		print "Missing parameter on the command line. Please enter the id of a club as the argument."
	elif (error == 2):
		print "Too many arguments on the command line. Please enter the id of a club as the argument."
	elif (error == 3):
		print "NaN argument on the command line. Please enter the id of a club as the argument."
	elif (error == 4):
		print dbfile+" database file does not exist! Please put "+dbfile+" in the execute directory"
	elif (error == 5):
		print dbfile+" does not contain a SQLite format 3 header. Please ensure that "+dbfile+" is a SqLite3 db"
	elif (error == 6):
		print "Argument supplied is too small. Please enter the id of a club in the argument" 
	elif (error == 7):
		print "Argument supplied is too large. Please enter the id of a club in the argument"
        elif (error == 8):
		print "Argument supplied is not a club_id in the club table. Please enter the id of a club in the argument"
        else:
            print "You have errors"
	sys.exit(error)

#check for initial script argument errors	
if (initialArgCheck()!=0):
        printErrors(initialArgCheck())

#check for dbfile errors
if (dbFileCheck()!=0):
        printErrors(dbFileCheck())

#check arguments against db
if (finalArgCheck()!= 0):
	printErrors(finalArgCheck())

#print the data
print 'The name of club '+sys.argv[1]+' is '+clubName()
print 'The description of the '+clubName()+' club is '+clubDescription()
print 'The list of group(s) to which the '+clubName()+' club belongs are '+str(listofGroups())
print 'The list of member(s) of the '+clubName()+' is '+str(listofMembers())
print 'The President of the '+clubName()+' club is '+clubPresident()

#the column 'description' from table 'clubgroup' was not used in assignmnet 3
