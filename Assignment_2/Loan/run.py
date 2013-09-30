#!/usr/bin/python2
import pdb
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
Assignment 2
9 September 2013
'''
import loanClass
import sys

if (len(sys.argv)==4):
    loan=loanClass.Loanclass(int(float(sys.argv[1])),float(sys.argv[2]),float(sys.argv[3]))
elif (len(sys.argv)==5):
    loan=loanClass.Loanclass(int(float(sys.argv[1])),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
loan=loanClass.Loanclass(int(float(20)),float(10000),float(10))

#print loan.interestAccrued(8)
print loan.remainingBalance(8)

sys.exit(0)
