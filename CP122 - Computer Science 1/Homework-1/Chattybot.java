import java.util.Scanner;

public class Chattybot{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println(SayHello());
        System.out.println();

        // Get user's first and last name and then call the Hello_First_Last function
        System.out.print("Enter your first name: ");
        String first_name = scan.nextLine();
        System.out.print("Enter your last name: ");
        String last_name = scan.nextLine();
        System.out.println(Hello_First_Last(first_name, last_name));

        // Ask user to choose a joke topic
        System.out.println("Would you like to hear a joke about food or skeletons?");
        System.out.println("Press 1 for food, 2 for skeletons");
        String choice = scan.nextLine();

        if(choice.equals("1")){
            System.out.print(tell_A_Joke("1"));
        }
        else if(choice.equals("2")){
            System.out.print(tell_A_Joke("2"));
        }
        else{
            System.out.print("I dont have a joke for that");
        }

        System.out.println();
        System.out.print("Would you like to hear a riddle? Press Y for yes and N for no: ");
        String riddle_choice = scan.nextLine();
        if(riddle_choice.equals("Y")){
            System.out.print(Tell_A_Riddle("hint_choice"));
            System.out.println();
            System.out.print("Would you like a hint? Press Y for yes and N for no: ");
            String hint_choice = scan.nextLine();
            if (hint_choice.equals("Y")){
                System.out.print();

            }
        }


    }

    public static String SayHello(){
        return "Hello there, nice to meet you!";
    }

    public static String Hello_First_Last(String first_name,String last_name){

        return "Hello "+ first_name+" "+last_name;
    }

    public static String tell_A_Joke(String topic) {
        if (topic.equals("1")) {
            return ("Why don’t eggs tell jokes? Because they might crack up!");
        }else  {
            return "Why don’t skeletons fight each other? Because they don’t have the guts!";
        }

    }

    public static String Tell_A_Riddle(String hint_choice){
        String riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?";
        //System.out.println(riddle);
        if(hint_choice.equals("Y")){
            return hint_choice;
        }
        return riddle;
    }
}