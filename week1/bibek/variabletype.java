public class variabletype {
    int age;
    String name;
    static int num1 =98;


    void display() {
        System.out.println("Name: " + name+ "age" +age +"num"+num1);
    }
    public static void main(String[] args) {
        variabletype VariableType = new variabletype();
        VariableType.display();
        VariableType.age = 67;
        variabletype.num1 = 2;
        
        VariableType.display();
        variabletype VariableType2 = new variabletype();
        VariableType2.display();
        VariableType2.age = 7;
        variabletype.num1 = 8;
        VariableType2.display();

        System.out.println(variabletype.num1);
       
    }
}