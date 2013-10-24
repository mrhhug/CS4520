#!/usr/bin/python2
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
Assignment 5
23 October 2013
'''
import math
import cgi

#Loan class from assignment 2
class Loan(object):
    
    def __init__(self,Balance,APR,numMonths,monthlyPayment): # monthly payment can be left None and calculated later
        self.numMonths=numMonths
        self.Balance=Balance
        self.APR=APR
        self.monthlyPayment=monthlyPayment
                 
    def remainingBalance(self,month): # defined recursively
        if month is 1: # base case
            return self.Balance
        month -= 1 # decrement
        return self.remainingBalance(month)+self.interestAccrued(month)-self.monthlyPayment # function calls itself
        
    def interestAccrued(self,month): # depends on remainingBalance function
        return self.APR/1200*self.remainingBalance(month)
    
    def computeMonthlyPayment(self): # optional method to calculate best fit payment
        self.monthlyPayment = ((self.APR/1200)+(self.APR/1200)/(math.pow((1+(self.APR/1200)),self.numMonths)-1))*self.Balance  
    
    def __str__(self): # your output may be another's input
            return str(self.Balance) + " " + str(self.APR) + " " + str(self.numMonths) + " " + str(self.monthlyPayment)

#take input from form in webpage
fld=cgi.FieldStorage()
AIR=float(fld.getfirst("AIR"))
month=int(fld.getfirst("month"))
amount=int(fld.getfirst("amount"))

#call the Loan class with form data, we already did an assignment on user input checking - this assignment omits user input checking
loan=Loan(amount,AIR,month,0)
loan.computeMonthlyPayment()

#use <pre> so that script online matches script on PC
head = "{:11s}{:18s}{:17s}{:12s}{}"
body = "{:5d}{:16.2f}{:16.2f}{:16.2f}{:16.2f}"

#begin html
print "Content-Type: text/html;charset=utf-8"
print
print '''
<html>
	<head>
		<meta charset="utf-8">
		<title>
			CS 4520&mdash;Fall 2013 - Assignment 5 submitted by Michael Hug &trade;
		</title>
		<!-- this will break eventually start-->
		<link rel="stylesheet" type="text/css" href="http://science.kennesaw.edu/~bsetzer/4520fa13/nanoc/output/assignments/supplement/style1-assignment05.css" media="screen">
		<!-- this will break eventually end-->
	</head>
	<body>
		<pre align="center">
'''

#pause html for some python
print head.format("Month","Balance In","Interest","Payment","Balance Out")
print "<hr>"
for i in range(1, loan.numMonths+1):
	ii=i+1
	formatted = body.format(i,loan.remainingBalance(i),loan.interestAccrued(i),loan.monthlyPayment,loan.remainingBalance(ii))
	print formatted

#resume html
print '''
		</pre>
	</body>
</html>
'''
