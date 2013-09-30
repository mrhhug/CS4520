package cs3530.batch1;

import psimjava.Process;

public class Job extends Process {

	private Computer comp;
	private double serviceTime;
	private double memoryNeeded;
	
	protected Job(String processName, Computer comp,
			double serviceTime, double memoryNeeded) {
		super(processName);
		this.comp = comp;
		this.memoryNeeded = memoryNeeded;
		this.serviceTime = serviceTime;
	}

	@Override
	protected void Main_body() {
		
	}

	public double getMemoryNeeded() {
		return memoryNeeded;
	}

	public double getServiceTime() {
		return serviceTime;
	}
	
	

}
