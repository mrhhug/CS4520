package computerarrayStrategy3;

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
		while(SimulationMain.isSimulationRunning()) {
			if(batchQueue.empty()) {
				deactivate(this);
			} else {
				Job jb = (Job)batchQueue.out();
				if(jb.getMemoryNeeded() > installedMemory) {
					// terminate the job, it won't fit in memory
					jb.terminate();
				} else {
					reactivate(jb);
					delay(jb.getServiceTime());
					reactivate(jb);
				}
			}
		}
		terminate();
	}
	
	
	
	/**
	 * Attempt to submit the job 'jb' into the batch queue.
	 * If the queue is full, return false.
	 * Otherwise, insert the job and return true.
	 * 
	 * If the computer is idle, reactivate the computer process
	 * after inserting the job into the queue.
	 * 
	 * @return  Return true if the job was submitted successfully.
	 */
	public boolean submit(Job jb) {
		if(batchQueue.full()) {
			return false;
		} else {
			batchQueue.into(jb);
			if(this.idle()) {
				reactivate(this);
			}
			return true;
		}
	}
	
	
	public int getQueueSize() {
		return batchQueue.length();
	}
}
