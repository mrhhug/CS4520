package cs3530.batch4A;

import cs3530.tracer.ConsoleTracer;
import cs3530.tracer.CsvFileTracer;
import cs3530.tracer.CsvTracer;
import cs3530.tracer.NullTracer;
import cs3530.tracer.SplitTracer;
import cs3530.tracer.Tracer;
import psimjava.Process;
import psimjava.Simulation;

public class SimulationMain extends Process {

	private static final int SIMULATION_LENGTH = 10000;
	private static SimulationMain theMain;
	
	
	private static final double INTER_ARRIVAL_TIME_MEAN = 5;
	private static final double SERVICE_TIME_MEAN = 10;
	private static final double JOB_SUBMISSION_CUTOFF = SIMULATION_LENGTH*7/8;
	private static final int MEMORY_INSTALLED = 100;
	private static final double MEMORY_NEEDED_MAX = MEMORY_INSTALLED;
	private static final double MEMORY_NEEDED_MIN = MEMORY_INSTALLED/3;
	private static final int MAX_QUEUE_SIZE = 100;
	
	// collect data only for jobs that start and end between the two specified times
	private static final double DATA_COLLECTION_START_TIME = SIMULATION_LENGTH/8;
        private static final double DATA_COLLECTION_END_TIME = SIMULATION_LENGTH;
	//private static final double DATA_COLLECTION_END_TIME = 7*SIMULATION_LENGTH/8;
	
	private static Simulation sim;
	
	public static final Tracer tracer;
	static {
		
		//tracer  = ConsoleTracer.get();
		//tracer = new CsvTracer(System.out);
		//Tracer t1  = new CsvFileTracer();
		//Tracer t2 = ConsoleTracer.get();
		//tracer = new SplitTracer(t1, t2);
		tracer = new NullTracer();
	}
	public static final Tracer summary;
	static {
		
		//summary  = ConsoleTracer.get();
		//summary = new CsvTracer(System.out);
		Tracer t1  = new CsvFileTracer();
		Tracer t2 = ConsoleTracer.get();
		summary = new SplitTracer(t1, t2);
		//summary = new NullTracer();
	}
	
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
		
//		summary.write("Simulation done: ",get_clock());
//		summary.write("Job summary totals");
//		summary.write("number  execute wait", Job.getNumberFinished(), Job.getTotalExecuteTime(), Job.getTotalWaitTime());
//		summary.write("average wait time", Job.getTotalWaitTime()/Job.getNumberFinished());
//		summary.write("average execute time", Job.getTotalExecuteTime()/Job.getNumberFinished());
//		summary.write("Number of jobs in queue", comp.getQueueSize());
                summary.write(get_clock()+","+Job.getNumberFinished()+","+Job.getTotalExecuteTime()+","+Job.getTotalWaitTime()+","+comp.getQueueSize());
		tracer.close();
		summary.close();
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
	
	public static boolean areJobsStillBeingSubmitted() {
		return theMain.get_clock() <= JOB_SUBMISSION_CUTOFF;
	}

	public static double getDataCollectionStartTime() {
		return DATA_COLLECTION_START_TIME;
	}

	public static double getDataCollectionEndTime() {
		return DATA_COLLECTION_END_TIME;
	}
	
	
	

}
