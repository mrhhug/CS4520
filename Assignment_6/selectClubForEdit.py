#! /usr/bin/python2
print "Content-Type: text/html;charset=utf-8\n\n"

from Michael_Hug_Assignment3_4520fa13 import clubclass

import sqlite3
import sys
dbfile='clubs.db'
conn = sqlite3.connect(dbfile)
cur = conn.cursor()
cur.execute('select * from club')
x=cur.fetchall()
conn.close()

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
        <h1>Select a Club to Display</h1>
<form action="index.html" method="GET">
<select name="ident">
        '''
for i in x:
        yeahithinkimslick= clubclass(str(i[0]))
        print "<option value=",yeahithinkimslick.ident(),">",yeahithinkimslick.clubName(),"</option>"

print '''
</select>
<br><br>
<option type="button" name="submit" value="Display" />
</form>
	</body>
</html>
	'''
