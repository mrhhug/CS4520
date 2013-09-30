/*
 * @author: Michael Hug hmichae4@students.kennesaw.edu
 * Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
 * Assignment 3
 * 14 September 2013
 */

package assignment_3;

import cs3530.tracer.ConsoleTracer;
import cs3530.tracer.CsvFileTracer;
import cs3530.tracer.CsvTracer;
import cs3530.tracer.NullTracer;
import cs3530.tracer.SplitTracer;
import cs3530.tracer.Tracer;
import psimjava.Process;
import psimjava.Simulation;

public class SimulationMain extends Process {

	private static int SIMULATION_LENGTH = 8000;
	private static SimulationMain theMain;
		
	private static double INTER_ARRIVAL_TIME_MEAN = 5;
	private static double SERVICE_TIME_MEAN = 10;
	private static final double JOB_SUBMISSION_CUTOFF = SIMULATION_LENGTH*7/8;
	private static int MEMORY_INSTALLED = 100;
	private static final double MEMORY_NEEDED_MAX = MEMORY_INSTALLED;
	private static final double MEMORY_NEEDED_MIN = MEMORY_INSTALLED/3;
	private static int MAX_QUEUE_SIZE = 100;
	
	// collect data only for jobs that start and end between the two specified times
	private static final double DATA_COLLECTION_START_TIME = SIMULATION_LENGTH/8;
	private static final double DATA_COLLECTION_END_TIME = 7*SIMULATION_LENGTH/8;
	
	private static Simulation sim;
        
        //Michael's declarations for CS3530 assignment 3
        private static int NUMBER_OF_COMPUTERS = 2;
        private static String COMPUTER_SELECTION_STRATEGY="1";
	
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
            
            Computer[] computerArray = new Computer[NUMBER_OF_COMPUTERS];
            for (int i =0;i<NUMBER_OF_COMPUTERS;i++)
            {
                Computer comp = new Computer("A computer", MAX_QUEUE_SIZE, MEMORY_INSTALLED);
                comp.start();
                computerArray[i]=comp;
            }
            UserPool up = new UserPool("User Pool", INTER_ARRIVAL_TIME_MEAN, SERVICE_TIME_MEAN, MEMORY_NEEDED_MIN, MEMORY_NEEDED_MAX, computerArray,COMPUTER_SELECTION_STRATEGY);
            up.start();
            //Thread.yield();
            sim.start_sim(SIMULATION_LENGTH);

//            summary.write("Simulation length: " + get_clock());
//            summary.write("Job summary totals");
//            summary.write("number of computers : "+ NUMBER_OF_COMPUTERS);
//            summary.write("computer selection strategy : " + up.getcomputer_selection_strategy());
//            summary.write("number of jobs finished : " + Job.getNumberFinished());
//            summary.write("total execution time : " + Job.getTotalExecuteTime());
//            summary.write("total wait time : " + Job.getTotalWaitTime());
//            summary.write("average wait time : " + Job.getTotalWaitTime()/Job.getNumberFinished());
//            summary.write("average execute time : " + Job.getTotalExecuteTime()/Job.getNumberFinished());
            summary.write("Simulation length," + get_clock()
                    +",INTER_ARRIVAL_TIME_MEAN,"+INTER_ARRIVAL_TIME_MEAN
                    +",SERVICE_TIME_MEAN,"+SERVICE_TIME_MEAN
                    +",NUMBER_OF_COMPUTERS,"+ NUMBER_OF_COMPUTERS
                    +",MEMORY_INSTALLED,"+MEMORY_INSTALLED
                    +",MAX_QUEUE_SIZE,"+MAX_QUEUE_SIZE
                    +",NUMBER_OF_COMPUTERS,"+NUMBER_OF_COMPUTERS
                    +",COMPUTER_SELECTION_STRATEGY," + up.getcomputer_selection_strategy()+COMPUTER_SELECTION_STRATEGY
                    +",number of jobs finished," + Job.getNumberFinished()
                    +",total execution time," + Job.getTotalExecuteTime()
                    +",total wait time," + Job.getTotalWaitTime()
                    +",average wait time," + Job.getTotalWaitTime()/Job.getNumberFinished()
                    +",average execute time," + Job.getTotalExecuteTime()/Job.getNumberFinished()+"\"   ");
            //summary.write("Number of jobs in queue", comp.getQueueSize());
            tracer.close();
            summary.close();
            System.exit(0);
	}

	public static void main(String[] args) {
            
		parseCLIarguments(args);
		sim = new Simulation("The simulation manager");
		
		theMain = new SimulationMain();
		theMain.start();
	}
        
        private static boolean parseCLIarguments(String[] args)
        {
            //8000
            SIMULATION_LENGTH=Integer.parseInt(args[0]);
            //5
            INTER_ARRIVAL_TIME_MEAN=Double.parseDouble(args[1]);
            //10
            SERVICE_TIME_MEAN=Double.parseDouble(args[2]);
            //100
            MEMORY_INSTALLED=Integer.parseInt(args[3]);
            //100
            MAX_QUEUE_SIZE=Integer.parseInt(args[4]);
            //2
            NUMBER_OF_COMPUTERS=Integer.parseInt(args[5]);
            //1
            COMPUTER_SELECTION_STRATEGY=args[6];
            return true;
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
        
        public static int MAX_QUEUE_SIZE()
        {
            return MAX_QUEUE_SIZE;
        }

}
