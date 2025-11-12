// Write a Java program using a for loop and if statement to print all numbers between 1 and 50 that are divisible by either 3 or 5, but not both.

public class Ques_1 {
    public static void main(String[] args) {
        for ( int i =1; i<=50; i++) {
            if ((i%3==0 && i%5==0)){
                continue;
            }
            else if(i%3==0 | i%5==0){
                System.out.println(i);
            }
            
            

        }
    
    }
}