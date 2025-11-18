public class Ques6 {
    public static void main (String[]args){
        for (int i=0; i<=30;i++){
            if (i==15){
                System.out.println("Skip");
            }else if (i%4==0){
                System.out.println(i*2);
            }else{
                System.out.println(i);
            }
        }
        System.out.println("done");
    }
}
