// import java.util.Scanner;

// public class CW{
//     public static void main(String[] args) {
//         Scanner sc= new Scanner(System.in);
//         int number = 12345;
//         int num;
//         while(true){
//             System.out.print("Enter a number : ");
//             num = sc.nextInt();
//             if (number == num){
//                 System.out.println("You entered : "+num);
//                 break;
//             };
        
        
//         }
//         sc.close();
//     }
// }


//Write the multiplication table of 2 and skip 6 in the table of 2 using continue
public class CW{
    public static void main(String[]args){
        for (int i=1; i<=10; i++){
            if (2*i==6) {
                continue;

            }else{
                System.out.println("2x"+i+"="+2*i);
            }
        }

    }
}
