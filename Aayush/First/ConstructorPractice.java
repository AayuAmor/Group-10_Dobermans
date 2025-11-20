package Aayush.First;

public class ConstructorPractice {
    String name;
    int age;
    public ConstructorPractice(){
        System.out.println("Hello");
    }
    public ConstructorPractice(String name, int age){
        this.name = name;
        this.age = age;
    }
    public ConstructorPractice(ConstructorPractice s1){
        this.name = s1.name;
        this.age = s1.age;
    }
    public void display(){
        System.out.println(name + age);
    }


}

class TestConstructor{
    public static void main(String[] args) {
        ConstructorPractice cp = new ConstructorPractice(
            "new",9
        );
        cp.display();
        ConstructorPractice cp1 = new ConstructorPractice(cp);
        cp1.display();
    }
}
