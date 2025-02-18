import java.util.Scanner;

public class Dollar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("How much money would you like to deposit? ");
        double amount = sc.nextDouble();

        amount = amount * 100;

        double ONE_DOLLAR = 100;
        double QUARTER = 25;
        double DIME = 10;
        double NICKEL = 5;
        double PENNY = 1;

        if (amount > ONE_DOLLAR) {
            ;
        }



    }
}
