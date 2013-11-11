package batch2;

import psimjava.Erand;
import psimjava.Process;
import psimjava.Urand;

public class UserPool extends Process {

	private Erand arrivalTimeGen;
	private Erand serviceTimeGen;
	private Urand memoryNeededGen;
	private Computer comp;
	
	private int customerNumber = 0;
	
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
		
	}

}
