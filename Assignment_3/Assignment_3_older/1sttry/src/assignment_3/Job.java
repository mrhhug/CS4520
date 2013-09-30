/*
 * @author: Michael Hug hmichae4@students.kennesaw.edu
 * Created for Dr Setzer's Fall 2013 4520 Distributed Systems Development
 * Assignment 3
 * 14 September 2013
 */

package assignment_3;

import psimjava.Process;
import static cs3530.batch4A.SimulationMain.tracer;

public class Job extends Process {

	private Computer comp;
	private double serviceTime;
	private double memoryNeeded;
	private int jobNumber;
	
	protected Job(int jobNumber,  Computer comp,
			double serviceTime, double memoryNeeded) {
		super("Job" + jobNumber);
		this.comp = comp;
		this.memoryNeeded = memoryNeeded;
		this.serviceTime = serviceTime;
		this.jobNumber = jobNumber;
	}

	private static double totalWaitTime;
	private static double totalExecuteTime;
	private static int numberFinished;
	
	@Override
	protected void Main_body() {
		double submitTime;
		double startTime;
		double finishTime;
		if(comp.submit(this)) {
			// successfully submitted, must wait until executed
			submitTime = get_clock();
			tracer.write("Job submitted", "Job--", jobNumber, submitTime);
			deactivate(this);
			// starting execution
			startTime = get_clock(); 
			tracer.write("Job starts executing", "Job--", jobNumber, startTime);
			deactivate(this);
			// finished execution
			finishTime = get_clock();
			tracer.write("Job finishes executing", "Job--", jobNumber, finishTime);
			
			if(SimulationMain.getDataCollectionStartTime() <= startTime
					&& finishTime <= SimulationMain.getDataCollectionEndTime()) {
				double waitTime = startTime - submitTime;
				double executeTime = finishTime - startTime;
				totalWaitTime += waitTime;
				totalExecuteTime += executeTime;
				numberFinished ++;
			}
		} else {
			// nothing to do
		}
		terminate();
	}

	public double getMemoryNeeded() {
		return memoryNeeded;
	}
	
	public double getServiceTime() {
		return serviceTime;
	}

	public static double getTotalWaitTime() {
		return totalWaitTime;
	}

	public static double getTotalExecuteTime() {
		return totalExecuteTime;
	}

	public static int getNumberFinished() {
		return numberFinished;
	}
	
}
