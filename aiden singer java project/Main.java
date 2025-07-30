import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner my_scanner = new Scanner(System.in);

        System.out.println("Enter your name:");
        String name = my_scanner.nextLine();
        System.out.println("Your name is: " + name);

        my_scanner.close();
    }

}