public class Ques5 {
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
