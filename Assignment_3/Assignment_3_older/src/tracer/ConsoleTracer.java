package cs3530.tracer;

public class ConsoleTracer extends Tracer {

	
	private ConsoleTracer() {}
	
	private static ConsoleTracer theTracer;
	
	public static  ConsoleTracer get() {
		if(theTracer == null) 
			theTracer = new ConsoleTracer();
		return theTracer;
	}
	
	
	@Override
	public void write(Object... parameters) {
		for(Object x : parameters) {
			if(x instanceof String) {
				String s = (String) x;
				if(s.charAt(s.length()-1) == '-')
					System.out.print(s.substring(0,s.length()-1));
				else 
					System.out.print(x + " ");
			} else {
				System.out.print(x + " ");
			}
		}
		System.out.println();
	}

}
