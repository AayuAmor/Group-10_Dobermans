//Write a Java program that prints the sum of even numbers and the product of odd numbers between 1 and 10 using a for loop and if condition.
public class Ques_5 {
    public static void main(String[] args) {
        int evenNum =0;
        int oddNum = 1;
        for(int i=1;i<10;i++){
            if (i%2==0){
                
                evenNum+=i;
                
            }
            else{
                oddNum*=i;
            }
        }
        System.out.println("EvenNum_sum= "+evenNum);
        System.out.println("OddNum_Product= "+oddNum);
    }
}