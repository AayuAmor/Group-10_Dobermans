public class Teacher {
    int age;
    String name;

    void display() {
        String name = "Ram";
        System.out.println("Name: " + name +age);
    }

    public static void main(String[] args) {
        Teacher teacher = new Teacher();
        teacher.display();
        teacher.age = 55;
    }
    
}
