#! /usr/bin/python2
'''
Michael Hug
CS 4520
Midterm exam
fa2012
'''
alist = [('able', 17), ('baker', 2345), ('charlie', 5), ('dog', 77359)]
plate = "{0:10}{1:8}"
for x in alist:
    print plate.format(*x)


