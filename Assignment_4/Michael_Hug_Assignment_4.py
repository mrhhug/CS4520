#!/usr/bin/python2
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 3530 Operating Systems
Assignment 4
27 October 2013
'''

import csv

class schedualing(object):
	datalist = []

	def __init__(self):
		with open('data.csv') as csvfile:
			read = csv.reader(csvfile, delimiter=',')
			for next in read:
				self.datalist.append(next)

	def __str__(self):
		return str(self.datalist)


sched = schedualing()
print sched
