package cs3530.batch3;

import psimjava.Process;
import psimjava.Simulation;

public class SimulationMain extends Process {

	private static final int SIMULATION_LENGTH = 10000;
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
		Computer comp = new Computer("The computer", MAX_QUEUE_SIZE, MEMORY_INSTALLED);
		UserPool up = new UserPool("User Pool", INTER_ARRIVAL_TIME_MEAN, SERVICE_TIME_MEAN, MEMORY_NEEDED_MIN, MEMORY_NEEDED_MAX, comp);
		comp.start();
		up.start();
		//Thread.yield();
		sim.start_sim(SIMULATION_LENGTH);
		
		System.out.println("Simulation done: " + get_clock());
		System.exit(0);
	}

	public static void main(String[] args) {
		sim = new Simulation("The simulation manager");
		
		theMain = new SimulationMain();
		theMain.start();
	}
	
	
	
	
	public static boolean isSimulationRunning() {
		return theMain.get_clock() <= SIMULATION_LENGTH;
	}

}
