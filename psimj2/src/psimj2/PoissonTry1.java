package psimj2;

import psimjava.Erand;

/**
 * We'll use an exponential distribution to generate arrival times.
 * Then we'll count the number of arrivals in intervals of time
 * and look at the mean.
 * 
 * @author Ben
 *
 */
public class PoissonTry1 {

	public static void main(String[] args) {
		test1(15, 10, 200000);

	}
	
	/**
	 * Generate arrival times and count how many fall in each
	 * interval of time.
	 * 
	 * @param perIntervalMean  Average number of events in an 'interval' of time
	 * @param interval 			Length of the time interval
	 * @param numSamples		Number of samples to generate.
	 */
	public static void test1(double perIntervalMean, double interval, int numSamples) {
		double samples[] = new double[numSamples];
		// generate samples
		// generator for interarrival times
		Erand gen = new Erand(interval/perIntervalMean);
		double time = gen.fdraw();
		for(int i = 0; i < numSamples; i++) {
			samples[i] = time;
			time += gen.fdraw();
		}

		// count samples in consecutive intervals
		// Interval i is from i*interval to (i+1)*interval
		// compute the interval containing the last sample
		int lastInterval = (int)(samples[samples.length-1]/interval);
		int firstInterval = 0;
		int numberOfIntervals = lastInterval - firstInterval + 1;
		double averageSamplesPerInterval = (double)numSamples/numberOfIntervals;
		System.out.println("Expected is: " + perIntervalMean);
		System.out.println("Observed is: " + averageSamplesPerInterval);
	}

}
