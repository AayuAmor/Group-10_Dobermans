//7. Write a Java program that simulates an ATM PIN verification system.The program should have a correct PIN stored (for example, 1234) and allow the user up to three attempts to enter the correct PIN.If the user enters the correct PIN, print "Access Granted" and stop the program.If the user enters the wrong PIN, print "Incorrect PIN, try again".After three incorrect attempts, print "Account locked".
import java.util.*;
public class Ques_7 {
    

    public static void main(String[] args) {
        int correctPIN = 1234;
        int attempts = 3;
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < attempts; i++) {
            System.out.print("Enter your PIN: ");
            int enteredPIN = sc.nextInt();

            if (enteredPIN == correctPIN) {
                System.out.println("Access Granted");
                sc.close();
                return;
            } else {
                System.out.println("Incorrect PIN, try again");
            }
        }

        System.out.println("Account locked");
        sc.close();
    }
}

