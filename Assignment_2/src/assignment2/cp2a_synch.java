package assignment2;

/**
 * Assignment 2 for Setzer 3530fa13
 * @author Michael Hug hmichae4@students.kennesaw.edu
 */
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.atomic.AtomicLong; //import for AtomicLong

public class cp2a_synch 
{
    private static BlockingQueue<Long> dropoff = new ArrayBlockingQueue<>(1);
    private static long start = 1;
    private static long end = 9999999; //large enough to toss error on my machine
    private static AtomicLong total = new AtomicLong(0); //changed to AtomicLong
    
    public static void main(String[] args) throws InterruptedException
    {
        Runnable prodR = new cp2a_synch.ProducerRunnable();
        Runnable consR = new cp2a_synch.ConsumerRunnable();
        Thread prodThr = new Thread(prodR);
        Thread consThr0 = new Thread(consR);
        Thread consThr1 = new Thread(consR);
        prodThr.start();
        consThr0.start();
        consThr1.start(); //start second consumer thread
        prodThr.join();
        consThr0.join();
        consThr1.join(); //wait for second consuer thread
        long expectedTotal = end*(end-1)/2 - start*(start-1)/2;
        System.out.println("Expected total: " + expectedTotal);
        System.out.println("Actual total:   " + total);
    }
    private static class ConsumerRunnable implements Runnable
    {
        @Override
        public void run()
        {
            long subtotal = 0;
            try
            {
                long x = dropoff.take();
                while(x >= 0)
                {
                    total.addAndGet(x); //add to total
                    subtotal += x;
                    x = dropoff.take();
                }
                System.out.println("Subtotal is " + subtotal);
            }
            catch(InterruptedException ie) 
            {
                    // not much to do
                System.out.println("Something wicked happened from consumer");
                System.exit(1);
            }
        }
    }    
    private static class ProducerRunnable implements Runnable 
    {

        @Override
        public void run()
        {
            try
            {
                for(long i = start; i < end; i++ )
                {
                    dropoff.put(i);
                }
                dropoff.put(-1L);
                dropoff.put(-1L); //added dropoff for second consumer
            }
            catch(InterruptedException ie)
            {
                    // not much to do here
                System.out.println("Something wicked happened from producer");
                System.exit(2);
            }
        }
    }
}
