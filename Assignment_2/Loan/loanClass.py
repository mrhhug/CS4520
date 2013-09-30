'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
Assignment 2
9 September 2013
'''
import math

class Loanclass(object):
    
    def __init__(self,numMonths,Balance,APR,monthlyPayment=-1):
        self.numMonths=numMonths
        self.Balance=Balance
        self.APR=APR
        self.monthlyPayment=monthlyPayment
        if (monthlyPayment<0): # if the class does not get a legal monthly payment, calculate a best fit
            self.monthlyPayment = self.computeMonthlyPayment()
            
    def computeMonthlyPayment(self):
        return ((self.APR/1200)+(self.APR/1200)/(math.pow((1+(self.APR/1200)),self.numMonths)-1))*self.Balance
    
    def interestAccrued(self,month):
        return self.APR/1200*self.remainingBalance(month)
    
    def remainingBalance(self,month):
        if month is 1:
            return self.Balance
        month -= 1
        return self.remainingBalance(month)+self.interestAccrued(month)-self.computeMonthlyPayment()

    def __str__(self):
            return str(self.numMonths) + " " + str(self.Balance) + " " + str(self.APR) + " " + str(self.monthlyPayment)
            
            