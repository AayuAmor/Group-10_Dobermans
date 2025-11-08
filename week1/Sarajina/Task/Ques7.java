import java.util.Scanner;

public class Ques7 {
    public static void main (String[]args){
        Scanner sc= new Scanner(System.in);
        int pin=1234;
        int tries=3;
        for (int i=1;i<=tries;i++){
            System.out.println("Enter the pin");
            int user=sc.nextInt();
            if (user==pin){
                System.out.println("Access Granted");
                break;
            }else{
                if (i<tries){
                    System.out.println("Incorrect pin,try again");
                }else{
                    System.out.println("Account locked");
                }
            }
            }
        }
    }

