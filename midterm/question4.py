#! /usr/bin/python2
'''
Michael Hug
Midterm Exam
Fa2013
CS4520
'''
class Measurement:
    def __init__(self, st, intt):
        self.location =st
        self.value = intt

    '''created my own constructer instead of useing default constructor to satisfy possible ambiguity of question 4'''
    def constructor(self , st, intt):
         self.location = st
         self.value = intt

    def __str__(self):
        return "["+self.location + " @ " +str(self.value) + "]"

m = Measurement("wherever",256)
print m
