#!/usr/bin/python2
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 3530 Operating Systems Class
Assignment_3
23 September 2013
'''
import sys
import os
import csv
import decimal

def RMshifteighttraces():
	os.system("rm ./traces/*")

def simulationLoop(name):
	str = "java -jar ./runables/"
	str += name
	str += ".jar"
	for _ in range(1,16):
		os.system(str)

def concatenateCSV(name):
	str = "cat ./traces/T* | sed 's/\"//g' > ./traces/"
	str +=name
	str +=".csv"
	os.system(str)
	os.system("rm ./traces/T*")
	
def CSVparse(name):
	str = "./traces/"
	str += name
	str += ".csv"
	filename = csv.reader(open(str,"rb"))
	numJobs = 0
	waitTime = 0
	for row in filename:  
		numJobs += decimal.Decimal(row[1])
		waitTime += decimal.Decimal(row[3])
		if int(row[4])!=0:
			print "Error, re-run script. All jobs did not finish."
			exit(1)
	with open("./traces/"+name+".txt", "w") as text_file:
		text_file.write("{}".format(waitTime/numJobs))
	
RMshifteighttraces()
for name in ("unmodified","computerarrayStrategy1","computerarrayStrategy2","computerarrayStrategy3"):
	simulationLoop(name)
	concatenateCSV(name)
	CSVparse(name)

