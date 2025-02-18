// convert a cartons volume to ounces by given inputs from user
import java.util.Scanner;

public class VolumeCarton {
    public static void main(String[] args) {

        // Get the user's length of carton
        Scanner length = new Scanner(System.in);
        System.out.print("What is the side length of the base of the carton in inches? ");
        double length_Carton = length.nextInt();

        // Get user's width of carton
        Scanner width = new Scanner(System.in);
        System.out.print("What is the width of the base of the carton in inches? ");
        double width_Carton = width.nextInt();

        // Get user's height of carton
        Scanner height = new Scanner(System.in);
        System.out.print("What is the height of the carton in inches? ");
        double height_Carton = height.nextInt();

        // calculate the volume of the milk carton in ounces,
        // then display it
        double volume = 0.55 * (length_Carton * width_Carton * height_Carton);
        System.out.println("The carton has a volume of " + String.format("%.2f", volume) + " ounces.");
        System.out.println("The volume of " + String.format("%.2f", volume) + " ounces.");

    }
}
