// Source code is decompiled from a .class file using FernFlower decompiler (from Intellij IDEA).
import java.util.Scanner;

public class Ques_2 {
   public Ques_2() {
   }

   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      System.out.print("Enter a Number:");
      int var2 = var1.nextInt();

      for(int var3 = 1; var3 <= var2; ++var3) {
         if (var3 % 4 != 0) {
            System.out.println(var3);
         }
      }

      var1.close();
   }
}