public class Main {
    public static void main(String[] args) {
        Old_Calcultor oldCalculator = new Old_Calcultor();

        System.out.println(oldCalculator.sub(3,6));
        System.out.println(oldCalculator.mul(3,6));
        System.out.println(oldCalculator.sub(4,5));
        System.out.println(oldCalculator.sub(5,4));
        System.out.println(oldCalculator.sub(33,11));

        Calculator calculator = new Calculator();
        System.out.println(calculator.sum(5,4));
        System.out.println(calculator.sum(5, 5));
        calculator.print();

    }
}
