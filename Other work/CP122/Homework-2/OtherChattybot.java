public class OtherChattybot {

    // ------------------------------------------------------------------------------------------------

    // simply say hello
    public static void sayHello() {
        System.out.println("Hello there. Nice to meet you.");

    }

    // ------------------------------------------------------------------------------------------------

    // say hello, with their first name and last name
    public static void sayHelloTo(String firstName, String lastName) {
        System.out.println("Hello " + firstName + " " + lastName + "!");
    }

    // ------------------------------------------------------------------------------------------------

    // tell a joke
    public static void tellAJoke(String topic) {
        switch (topic) {
            case "Colorado":
                System.out.println("Where do crayons go on vacation?");
                System.out.println("Color-ado!");
                break;
            case "Horse":
                System.out.println("What do you call a well-balanced horse?");
                System.out.println("Stable.");
                break;
            default:
                System.out.println("Unknown topic: " + topic);
        }
    }

    // ------------------------------------------------------------------------------------------------

    // tell a riddle
    public static void tellRiddle(String fact) {
        switch (fact) {
            case "Soap":
                System.out.println("What gets smaller every time it takes a bath?");
                System.out.println("Soap!");
                break;
            case "Snowflake":
                System.out.println("I'm not a blanket, yet I cover the ground; a crystal from heaven that doesn't make a sound. What am I?");
                System.out.println("Snowflake!");
                break;
            default:
                System.out.println("Unknown fact: " + fact);
        }
    }

    // ------------------------------------------------------------------------------------------------

    public static void main(String[] args) {

        sayHello();

        System.out.println();

        sayHelloTo("Aidan", "Prezzano");

        System.out.println();

        tellAJoke("Colorado");

        System.out.println();

        tellRiddle("Soap");

    }

    // ------------------------------------------------------------------------------------------------

}