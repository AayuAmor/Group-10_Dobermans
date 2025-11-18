//Write a Java program that asks for 10 integers and prints only those that are even and greater than 20 using if and for loops.
import java.util.*;
public class Ques_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 1; i<=10;i++){
            System.out.print("Enter an Interger:");
            int num = sc.nextInt();
            if (num%2==0 & num>20){
                System.out.println(num);
            }
        }
        sc.close();
    }
}
