import java.util.Scanner;
public class student{
    public static void main(String args[]){
        double secondroot=0,firstroot=0;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the values of a"); 
        double a=sc.nextDouble();
        System.out.println("enter the values of b");
        double b=sc.nextDouble(); 
        System.out.println("enter the values of c");
        double c=sc.nextDouble();
        double det=(b*b)-(4*a*c);
        double sqrt =Math.sqrt(det);
        if(det>0){
            firstroot=(-b+sqrt)/(2*a);
            secondroot=(-b-sqrt)/(2*a);
            System.out.println("roots"+firstroot+"and"+secondroot);
        }
        else if(det==0){
            System.out.println("roots"+(-b+sqrt)/(2*a));
        }

        
        

    }

   
    
}