import java.util.Scanner;

public class Main {

   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       int length = scanner.nextInt();
       int count=0;
       int[] array =  new int[length];
       for (int i = 0; i < length; i++) {
           array[i] = scanner.nextInt();
           if(array[i]%4==0){
               count=count+array[i];
           }
       }
System.out.println(count);
       //your code goes here
       
   }
}