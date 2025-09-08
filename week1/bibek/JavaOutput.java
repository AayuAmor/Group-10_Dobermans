/* 6. WAP that prints the following output:
A well-formed Java program has a main method with { and } braces.
A System.out.println statement has ( and ) and usually a String that starts and ends with a " character.
(But we type \" instead!)
What is the difference between
a ' and a "?  Or between a " and a \"?
One is what we see when we're typing our program. The other is what appears on the "console." */
public class JavaOutput {
    public static void main(String[] args) {
        System.out.println("A well-formed Java program has a main method with { and } braces.\n");

        System.out.println("A System.out.println statement has ( and ) and usually a String that starts and ends with a \" character.");
        System.out.println("(But we type \\\" instead!)\n");

        System.out.println("What is the difference between");
        System.out.println("a ' and a \"?  Or between a \" and a \\\"?\n");

        System.out.println("One is what we see when we're typing our program. The other is what appears on the \"console.\"");
    }
}