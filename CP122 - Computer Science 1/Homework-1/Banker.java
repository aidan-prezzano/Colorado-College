import java.math.BigDecimal;
import java.util.Scanner;

public class Banker {

    // ------------------------------------------------------------------------------------------------

    public static boolean TEST_MODE = false;
    public static String TEST_MODE_INITIAL_BALANCE = "$1000.0";
    public static String TEST_MODE_ANNUAL_INTEREST = "6.0%";

    // ------------------------------------------------------------------------------------------------

    // calculate the new balance
    public static BigDecimal firstQuarterEarnings(BigDecimal initialBalance, BigDecimal annualInterest) {
        BigDecimal monthlyInterest = annualInterest.divide(new BigDecimal("12"));
        BigDecimal interest = initialBalance.multiply(monthlyInterest);
        return initialBalance.add(interest);
    }

    // ------------------------------------------------------------------------------------------------

    public static void main(String[] args) {

        // open the scanner, to get input from the user
        Scanner scan = new Scanner(System.in);

        // get the initial balance
        System.out.print("Initial balance: ");
        String initialBalanceStr = TEST_MODE ? TEST_MODE_INITIAL_BALANCE : scan.nextLine();
        initialBalanceStr = initialBalanceStr.replace("$", "");
        BigDecimal initialBalance = new BigDecimal(initialBalanceStr);

        // get the annual interest rate - divide this by 100, to get the true rate
        System.out.print("Annual interest: ");
        String annualInterestStr = TEST_MODE ? TEST_MODE_ANNUAL_INTEREST : scan.nextLine();
        annualInterestStr = annualInterestStr.replace("%", "");
        BigDecimal annualInterest = new BigDecimal(annualInterestStr).divide(new BigDecimal("100"));

        // close the scanner - no longer needed
        scan.close();

        // to start, set the balance to the initial balance
        BigDecimal balance = initialBalance;

        // balance after first month
        balance = firstQuarterEarnings(balance, annualInterest);
        System.out.println("Balance after first month: $" + String.format("%.2f", balance));

        // balance after second month
        balance = firstQuarterEarnings(balance, annualInterest);
        System.out.println("Balance after second month: $" + String.format("%.2f", balance));

        // balance after third month
        balance = firstQuarterEarnings(balance, annualInterest);
        System.out.println("Balance after third month: $" + String.format("%.2f", balance));

    }

    // ------------------------------------------------------------------------------------------------

}