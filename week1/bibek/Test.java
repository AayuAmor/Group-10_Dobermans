/* public class Test {
    public static void main(String[] args) {
        long myLong = 1234567890L;
        double myDouble = myLong; 
        System.out.println("Long value: " + myLong);
        System.out.println("Converted to double: " + myDouble);

        double anotherDouble = 098765.4321;
        long newLong = (long) anotherDouble; 
        System.out.println("Double value: " + anotherDouble);
        System.out.println("Converted to long: " + newLong);
    }
}
 */

 public class Test {
    public static void main(String[] args) {
        int a = 6;
        int b = 7;
        System.out.println(++a);
        System.out.println(a++);
        System.out.println(a++ + ++b);
        System.out.println(a);
    }
}