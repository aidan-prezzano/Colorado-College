import java.util.Scanner;

public class OtherVolumeCarton {

    public static boolean TEST_MODE = true;
    public static int TEST_MODE_LENGTH = 2;
    public static int TEST_MODE_HEIGHT = 4;

    public static void main(String[] args) {

        // open the scanner, to get input from the user
        Scanner scan = new Scanner(System.in);

        // get the length of the milk carton
        System.out.print("What is the side length of the base of the carton in inches? ");
        int length = TEST_MODE ? TEST_MODE_LENGTH : scan.nextInt();

        // get the heighth of the milk carton
        System.out.print("What is the height of the carton in inches? ");
        int height = TEST_MODE ? TEST_MODE_HEIGHT : scan.nextInt();

        // close the scanner - no longer needed
        scan.close();

        // caluclate the volume of the milk carton in ounces,
        // then display it
        double volume = 0.55 * (length * length * height);
        System.out.println("The carton has a volume of " + String.format("%.2f", volume) + " ounces.");

    }

}