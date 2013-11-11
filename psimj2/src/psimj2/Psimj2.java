/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package psimj2;

import java.util.Random;
import psimjava.Erand;

public class Psimj2 
{
    public static void main(String[] args) 
    {
       Erand gen = new Erand(20);
       for(int i = 0; i < 5;i++)
       {
           double d = gen.fdraw();
           //System.out.println(d);
           System.out.println(randomString(-229985452) + " " + randomString(-147909649));
       }
    }
    public static String randomString(int i)
   {
       Random ran = new Random(i);
       StringBuilder sb = new StringBuilder();
       for (int n = 0; ; n++)
       {
           int k = ran.nextInt(27);
           if (k == 0)
           break;
           sb.append((char)('`' + k));
       }
       return sb.toString();
   }
}
