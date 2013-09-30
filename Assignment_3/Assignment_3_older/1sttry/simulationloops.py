#!/usr/bin/python2
'''
@author: Michael Hug hmichae4@students.kennesaw.edu
Created for Dr Setzer's Fall 2013 3530 Operating Systems Class
Assignment_3
9 September 2013
'''
import sys
import os
import threading

'''
class MyThread ( threading.Thread ):
	def __init__ (self,str):
		self.str = str
		threading.Thread.__init__ ( self )

	def run (self):
		os.system(self.str)
'''

os.system("rm ./traces/*")
for _ in range(1,16):
    for INTER_ARRIVAL_TIME_MEAN in range(1,4):
        for SERVICE_TIME_MEAN in range(1,4):
            for NUMBER_OF_COMPUTERS in range(1,4):
						os.system("java -jar ./dist/Assignment_3.jar 80000 "+str(5**INTER_ARRIVAL_TIME_MEAN)+" "+str(10**SERVICE_TIME_MEAN)+" 100 100 "+str(10**NUMBER_OF_COMPUTERS)+" 1")
						os.system("java -jar ./dist/Assignment_3.jar 80000 "+str(5**INTER_ARRIVAL_TIME_MEAN)+" "+str(10**SERVICE_TIME_MEAN)+" 100 100 "+str(10**NUMBER_OF_COMPUTERS)+" 2")
						os.system("java -jar ./dist/Assignment_3.jar 80000 "+str(5**INTER_ARRIVAL_TIME_MEAN)+" "+str(10**SERVICE_TIME_MEAN)+" 100 100 "+str(10**NUMBER_OF_COMPUTERS)+" 3")

                                    
    #SIMULATION_LENGTH
    #INTER_ARRIVAL_TIME_MEAN
    #SERVICE_TIME_MEAN
    #MEMORY_INSTALLED
    #MAX_QUEUE_SIZE
    #NUMBER_OF_COMPUTERS
    #COMPUTER_SELECTION_STRATEGY
    #os.system("java -jar ./dist/Assignment_3.jar 50000000 100 "+str(ten)+" 100 100 2 1")
    
print "simulation loop finished"
os.system("cat ./traces/* | sed 's/\"//g' > ./traces/output.csv")
