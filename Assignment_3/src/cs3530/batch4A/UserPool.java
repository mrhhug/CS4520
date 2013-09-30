package cs3530.batch4A;

import psimjava.Erand;
import psimjava.Process;
import psimjava.Urand;

public class UserPool extends Process {

	private Erand arrivalTimeGen;
	private Erand serviceTimeGen;
	private Urand memoryNeededGen;
	private Computer comp;
	
	
	
	private int jobNumber = 0;
	
	protected UserPool(String processName,
			double meanInterArrivalTime,
			double meanServiceTime,
			double minMemoryNeeded,
			double maxMemoryNeeded,
			Computer comp) {
		super(processName);
		arrivalTimeGen = new Erand(meanInterArrivalTime);
		serviceTimeGen = new Erand(meanServiceTime);
		memoryNeededGen = new Urand(minMemoryNeeded, maxMemoryNeeded);
		this.comp = comp;
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
			Job jb = new Job(jobNumber,  comp, serv, mem);
			jb.start();
			//Thread.yield();
		}
		terminate();
	}

}
