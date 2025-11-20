package Aayush.First;

import Aayush.First.GetterSetter;

public class Main {

    public static void main(String[] args) {
        GetterSetter getterSetter = new GetterSetter();

        getterSetter.setName("Aayush");
        System.out.println(getterSetter.getName());
        getterSetter.setAge(22);
        System.out.println(getterSetter.getAge());

    }
}
