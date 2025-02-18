import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {


        System.out.println(displacement(3, 4, 5));


    }


    public static double displacement(double velocity, double a, double t) {
        double displacement = velocity * t + 0.5 * a * Math.pow(t, 2);
        return displacement;

    }
}