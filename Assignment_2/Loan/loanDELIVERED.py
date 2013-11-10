'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
Assignment 2
9 September 2013
'''
import math

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
