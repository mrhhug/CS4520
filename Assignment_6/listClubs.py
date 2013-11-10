#! /usr/bin/python2
print "Content-Type: text/html;charset=utf-8\n\n"

from Michael_Hug_Assignment3_4520fa13 import clubclass

print '''
	<html>
		<head>
			<meta charset="utf-8">
			<title>
				CS 4520&mdash;Fall 2013 - Assignment 6 submitted by Michael Hug &trade;
			</title>
			<!-- this will break eventually start-->
			<link rel="stylesheet" type="text/css" href="http://science.kennesaw.edu/~bsetzer/4520fa13/nanoc/output/assignments/assignment06/clubStyle.css" media="screen">
			<!-- this will break eventually end-->
		</head>
		<body>
        <h1>List of Clubs</h1>
        '''
import sqlite3
import sys
dbfile='clubs.db'
conn = sqlite3.connect(dbfile)
cur = conn.cursor()
cur.execute('select * from club')
x=cur.fetchall()
conn.close()

print "<ul>"
for i in x:
        yeahithinkimslick= clubclass(str(i[0]))
        print "<li>",yeahithinkimslick.clubName()
        print "<ul>"
        print "<li>ident:",yeahithinkimslick.ident(),"</li>"
        print "<li>description:",yeahithinkimslick.clubDescription(),"</li>"
        print "<li>President:",yeahithinkimslick.clubPresident(),"</li>"
        print "<li>Club has these members:</li>"
        print "<ul>"
        for j in yeahithinkimslick.listofMembers():
                print "<li>",j,"</li>"
        print "</ul>"
        print "<li>club belong(belongs) to</li>"
        print "<ul><li>missing clubgrouptable</li>"
        
        ''' missing clubgrouptable
        for j in yeahithinkimslick.listofMembers():
                print "<li>",j,"</li>"
        print "</ul>"
        groups= yeahithinkimslick.listofGroups()
        '''
        
        print "</ul>"
        print "</ul>"
        print "</li>"
        
print "</ul>"
print '''
	</body>
</html>
	'''
