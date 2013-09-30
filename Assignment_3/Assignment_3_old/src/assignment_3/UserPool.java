/*
 * @author: Michael Hug hmichae4@students.kennesaw.edu
 * Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
 * Assignment 3
 * 14 September 2013
 */

package assignment_3;

import psimjava.Erand;
import psimjava.Process;
import psimjava.Urand;

public class UserPool extends Process {

	private Erand arrivalTimeGen;
	private Erand serviceTimeGen;
	private Urand memoryNeededGen;
	//private Computer comp;
	
	private int jobNumber = 0;
	
        //Michael's declarations for CS3530 assignment
        private Computer[] computerArray;
        private String computer_selection_strategy;
        
	protected UserPool(String processName,
			double meanInterArrivalTime,
			double meanServiceTime,
			double minMemoryNeeded,
			double maxMemoryNeeded,
			Computer[] computerArray,
                        String computer_selection_strategy) {
		super(processName);
		arrivalTimeGen = new Erand(meanInterArrivalTime);
		serviceTimeGen = new Erand(meanServiceTime);
		memoryNeededGen = new Urand(minMemoryNeeded, maxMemoryNeeded);
		this.computerArray = computerArray;
	}

	@Override
	protected void Main_body() {
		//while(SimulationMain.isSimulationRunning()) {
		while(SimulationMain.areJobsStillBeingSubmitted()) {
			double arr = arrivalTimeGen.fdraw();
			delay(arr);
			double serv = serviceTimeGen.fdraw();
			double mem = memoryNeededGen.fdraw();
			jobNumber++;
			Job jb = new Job(jobNumber, SelectComputer(), serv, mem);
			jb.start();
			//Thread.yield();
		}
		terminate();
	}
        
        protected Computer SelectComputer()
        {
            if("1".equals(computer_selection_strategy))
            {
                return Selection_Strategy_1();
            }
            if("2".equals(computer_selection_strategy))
            {
                return Selection_Strategy_2();
            }
            if("3".equals(computer_selection_strategy))
            {
                return Selection_Strategy_3();
            }
            //defautl value
            return Selection_Strategy_3();
        }
        
        protected Computer Selection_Strategy_1()
        {
            computer_selection_strategy="Pick the first computer always";
            return computerArray[0];
        }
        
        protected Computer Selection_Strategy_2()
        {
            computer_selection_strategy="Pick a computer with an empty batch queue. If no computer has an empty queue, use the first computer";
            for (int i =0;i<computerArray.length;i++)
            {
                if(computerArray[i].getQueueSize()==0)
                {
                    return computerArray[i];
                }
            }
            return computerArray[0];
        }
        
        protected Computer Selection_Strategy_3()
        {
            computer_selection_strategy="Pick the computer with the shortest queue";
            int shortestQueue = SimulationMain.MAX_QUEUE_SIZE()+1;
            int shortestQueseIndex = computerArray.length+1;
            for (int i =0;i<computerArray.length;i++)
            {
                if(computerArray[i].getQueueSize()==0)
                {
                    return computerArray[i];
                }
                if (computerArray[i].getQueueSize()<shortestQueue)
                {
                    shortestQueue=computerArray[i].getQueueSize();
                    shortestQueseIndex = i;
                }
            }
            return computerArray[shortestQueseIndex];
        }
        public String getcomputer_selection_strategy()
        {
            return computer_selection_strategy;
        }

}

