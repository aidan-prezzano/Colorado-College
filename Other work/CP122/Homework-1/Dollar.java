import java.math.BigDecimal;
import java.util.Scanner;

public class Dollar {

    public static boolean TEST_MODE = true;
    public static String TEST_DOLLAR = "32.99";

    // define currency amounts
    public static BigDecimal ONE_DOLLAR = new BigDecimal("1.00");
    public static BigDecimal ONE_QUARTER = new BigDecimal("0.25");
    public static BigDecimal ONE_DIME = new BigDecimal("0.10");
    public static BigDecimal ONE_NICKEL = new BigDecimal("0.05");
    public static BigDecimal ONE_CENT = new BigDecimal("0.01");

    public static void main(String[] args) {

        // open the scanner, to get input from the user
        Scanner scan = new Scanner(System.in);

        // get the number of dollars
        // take in a String, then set it into a BigDecimal, to avoid floating point issues
        System.out.print("Enter the number of dollars: ");
        String dollar = TEST_MODE ? TEST_DOLLAR : scan.nextLine();
        BigDecimal dollar_amount = new BigDecimal(dollar);

        // close the scanner - no longer needed
        scan.close();

        // caluclate the number of dollars, quarters, dimes, nickels, and cents
        // use a while loop ... with if else-if statements
        // while the dollar amount has 1+ dollars ... increment nbrDollars, and subtract 1.00 from the dollar amount
        // while the dollar amount has 1+ quarters ... increment nbrQuarters, and subtract 0.25 from the dollar amount
        // while the dollar amount has 1+ dimes ... increment nbrDimes, and subtract 0.10 from the dollar amount
        // while the dollar amount has 1+ nickels ... increment nbrNickels, and subtract 0.05 from the dollar amount
        // while the dollar amount has 1+ cents ... increment nbrCents, and subtract 0.01 from the dollar amount
        int nbrDollars = 0;
        int nbrQuarters = 0;
        int nbrDimes = 0;
        int nbrNickels = 0;
        int nbrCents = 0;
        while (dollar_amount.compareTo(BigDecimal.ZERO) > 0) {
            if (dollar_amount.compareTo(ONE_DOLLAR) >= 0) {
                nbrDollars = nbrDollars + 1;
                dollar_amount = dollar_amount.subtract(ONE_DOLLAR);
            } else if (dollar_amount.compareTo(ONE_QUARTER) >= 0) {
                nbrQuarters = nbrQuarters + 1;
                dollar_amount = dollar_amount.subtract(ONE_QUARTER);
            } else if (dollar_amount.compareTo(ONE_DIME) >= 0) {
                nbrDimes = nbrDimes + 1;
                dollar_amount = dollar_amount.subtract(ONE_DIME);
            } else if (dollar_amount.compareTo(ONE_NICKEL) >= 0) {
                nbrNickels = nbrNickels + 1;
                dollar_amount = dollar_amount.subtract(ONE_NICKEL);
            } else {
                nbrCents = nbrCents + 1;
                dollar_amount = dollar_amount.subtract(ONE_CENT);
            }
        }

        // display the currency amounts
        System.out.print(nbrDollars + " dollars " + nbrQuarters + " quarter " + nbrDimes + " dimes " + nbrNickels + " nickel " + nbrCents + " cents");

    }

}