#! /usr/bin/python2
'''
Michael Hug
for Setzer's 4520fa13
reoccuringhtml.py
'''
from Michael_Hug_Assignment3_4520fa13_NOWACLASS import clubclass

def cgiheader():
	print "Content-Type: text/html"

def htmlhead():
	print '''
	<html>
		<head>
			<meta charset="utf-8">
			<title>
				CS 4520&mdash;Fall 2013 - Assignment 6 submitted by Michael Hug &copy;
			</title>
			<link rel="stylesheet" type="text/css" href="http://science.kennesaw.edu/~bsetzer/4520fa13/nanoc/output/assignments/assignment06/clubStyle.css" media="screen">
		</head>
		<body id=content>
		'''
		
def htmltail():
	print '''
		</body>
	</html>
	'''

def error(errorlevel):
	x= clubclass(None)
	print "<div class=error>"
        x.printErrors(errorlevel)
        print "</div>"
	
def readcheck():
    x= clubclass(None)
    errorlevel = x.dbFileCheck()
    if errorlevel>0:
        error(errorlevel)
        return 1
    else:
        return 0
        
def writecheck():
    x= clubclass(None)
    errorlevel = x.dbWriteCheck()
    if errorlevel>0:
        error(errorlevel)
        return 1
    else:
        return 0
           
def readwritecheck():
    if readcheck() == 0 and writecheck() == 0:
        return 0
    else:
        return 1

def nullcheck(arg,which):
    if not arg or arg.isspace():
        print "<div class=error>Please supply a value for ",which,"</div>"
        return 1
    return 0
