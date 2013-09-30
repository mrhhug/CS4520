package computerarrayStrategy3;

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
        private int COMPUTER_SELECTION_STRATEGY;
	
	protected UserPool(String processName,
			double meanInterArrivalTime,
			double meanServiceTime,
			double minMemoryNeeded,
			double maxMemoryNeeded,
			Computer[] computerArray,
                        int COMPUTER_SELECTION_STRATEGY) {
		super(processName);
		arrivalTimeGen = new Erand(meanInterArrivalTime);
		serviceTimeGen = new Erand(meanServiceTime);
		memoryNeededGen = new Urand(minMemoryNeeded, maxMemoryNeeded);
		this.computerArray = computerArray;
                this.COMPUTER_SELECTION_STRATEGY = COMPUTER_SELECTION_STRATEGY;
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
			Job jb = new Job(jobNumber, SelectComputer(COMPUTER_SELECTION_STRATEGY), serv, mem);
			jb.start();
			//Thread.yield();
		}
		terminate();
	}
        protected Computer SelectComputer(int strategy)
        {
            if(strategy==1)
            {
                return Selection_Strategy_1();
            }
            if(strategy==2)
            {
                return Selection_Strategy_2();
            }
            if(strategy==3)
            {
                return Selection_Strategy_3();
            }
            //defautl value
            return null;
        }
        
        protected Computer Selection_Strategy_1()
        {
            return computerArray[0];
        }
        
        protected Computer Selection_Strategy_2()
        {
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
        
        public int getQueueSize(){
            int size =0;
            for (Computer comp : computerArray)
                size += comp.getQueueSize();
            return size;
        }

}
