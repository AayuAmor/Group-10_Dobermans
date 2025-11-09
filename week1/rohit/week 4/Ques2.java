import java.util.Scanner;

public class Ques2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Number:");
        int num = sc.nextInt();

        for (int i =1; i<=num; i++){
            if (i%4==0){
                continue;
            }
            else{
                System.out.println(i);
            }
        }
        sc.close();
    }
}