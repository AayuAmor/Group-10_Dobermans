import java.util.Scanner;

public class Ques7 {
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
