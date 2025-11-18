
public class Ques5 {
    public static void main (String[]args){
        int Evensum=0;
        int Oddsum=1;
       for (int i=0; i<=10; i++){
            if (i %2==0){
                Evensum +=i;
            }else{
                Oddsum*=i;
            }
        }
        System.out.println("sum of even numbers"+Evensum); 
        System.out.println("sum of odd numbers"+Oddsum);
    }
}

