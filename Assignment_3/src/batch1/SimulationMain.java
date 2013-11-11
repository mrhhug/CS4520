package batch1;

import psimjava.Process;
import psimjava.Simulation;

public class SimulationMain extends Process {

	private static final int SIMULATION_LENGTH = 1000;
	private static SimulationMain theMain;
	
	
	private static final double INTER_ARRIVAL_TIME_MEAN = 20;
	private static final double SERVICE_TIME_MEAN = 20;
	private static final int MEMORY_INSTALLED = 100;
	private static final double MEMORY_NEEDED_MAX = MEMORY_INSTALLED;
	private static final double MEMORY_NEEDED_MIN = MEMORY_INSTALLED/3;
	private static final int MAX_QUEUE_SIZE = 100;
	
	private static Simulation sim;
	
	
	protected SimulationMain() {
		super("Simulation Main Process");
		
	}

	@Override
	protected void Main_body() {
		
	}

	public static void main(String[] args) {
		
	}
	
	

}
