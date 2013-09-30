package cs3530.batch1;

import psimjava.Process;
import psimjava.Squeue;

public class Computer extends Process {

	private Squeue batchQueue;
	private int installedMemory;
	
	
	protected Computer(String processName, int maxQueueSize,
			int installedMemory ) {
		super(processName);
		batchQueue = new Squeue(processName + "-BatchQueue", 
				maxQueueSize);
		this.installedMemory = installedMemory;
	}

	@Override
	protected void Main_body() {
		
	}

	public int getInstalledMemory() {
		return installedMemory;
	}
	
	
	
	
}
