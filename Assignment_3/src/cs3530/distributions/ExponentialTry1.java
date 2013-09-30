package cs3530.distributions;

import psimjava.Erand;




public class ExponentialTry1 {

	public static void main(String[] args) {
		test1(5, 10, 2000000);

	}

	
	/**
	 * 	Generate numbers from an exponential random number generator and
	 * 	compare the observed histogram with the expected.
	 * 
	 * @param beta		The mean of the exponetial distibution
	 * @param numBoxes		The number of boxes in the histogram
	 * @param numSamples	The number of samples to generate
	 */
	public static void test1(double beta, int numBoxes, int numSamples) {
		// counters for the histogram
		int counters[] = new int[numBoxes];
		// Samples will be counted in intervals
		// numBoxes specifies the number of intervals to use
		double breaks[] = new double[numBoxes];
		for(int j = 1; j < numBoxes; j++) {
			// This uses the cumulative distribution function, in inverse form,
			//  to find where the even percentiles are.
			breaks[j-1] = -Math.log(1 - (double)j/numBoxes)*beta;
		}
		// This is not actually used, but reminds us that the last interval
		// in the histogram goes to infinity.
		breaks[numBoxes-1] = Double.MAX_VALUE;
		
		// create a generator
		Erand gen = new Erand(beta);
		// generate all the samples
		for(int i = 0; i < numSamples; i++ ) {
			// get one sample
			double x = gen.fdraw();
			// find the interval in which the sample falls
			int j = 0;
			while(x > breaks[j] && j < numBoxes-1) {
				j++;
			}
			// increment the counter
			counters[j]++;
		}
		// display the results
		System.out.printf(    "%8s     %10s\n", "count", "frequency");
		for(int i = 0; i < numBoxes; i++ ) {
			System.out.printf("%8d  %10.4f\n", counters[i], (double)counters[i]/numSamples);
		}
		// we could do a chi-square test on the results as a reasonable test of how well
		// the random number generator is working, but that will take us too far afield
		//
		// Simply observe the results.
		System.out.println("The count in each interval should be close to the expected count: " + numSamples/numBoxes);
		System.out.println("The frequency in each interval should be close to the expected frequency: "
				+ 1.0/numBoxes);
		
		// OK, here's the chi-square statistic itself, if you wish to look that up
		double x2 = 0;
		double expected = (double)numSamples/numBoxes;
		for(int j = 0; j < numBoxes; j++ ) {
			double diff = (expected - counters[j]);
			x2 += diff*diff/expected;
		}
		System.out.println("Chi-squared statistic is " + x2);
		System.out.println("The number of degrees of freedom is " + (numBoxes-1));
	}
}
