#!/usr/bin/python2
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
Assignment 2
9 September 2013
'''
import loan
import sys

loan=loan.Loan(int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]),0)
loan.computeMonthlyPayment()

head = "{:11s}{:18s}{:17s}{:12s}{}"
body = "{:5d}{:16.2f}{:16.2f}{:16.2f}{:16.2f}"
print head.format("Month","Balance In","Interest","Payment","Balance Out")

for i in range(1, int(sys.argv[3])+1):
    ii=i+1
    formatted = body.format(i,loan.remainingBalance(i),loan.interestAccrued(i),loan.monthlyPayment,loan.remainingBalance(ii))
    print formatted