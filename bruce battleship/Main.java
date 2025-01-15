
import java.util.Scanner;

public class Main {


    public static void main(String[] args) {

        /*
         * 
         * assign starting player
         * 
         * do board setup per player (set ships)
         *      verify placement
         * 
         * start the game
         *      pick current player
         *      take their shot
         *          verify shot
         *          check if hit
         *          update board
         *       swap players
         * 
         */

        int player = 1;

        Board p1_board = new Board();
        Board p2_board = new Board();

        boolean valid = false;
        Scanner scanner = new Scanner(System.in);
        while (!valid) {

            // x is an int
            // y is a char
            // this is how the actual battleship game board looks
            System.out.println("Enter position of ship: (x y)");
            String input = scanner.nextLine();
            

            System.out.println("Enter orientation of ship: (u, d, l, r)");
            String input2 = scanner.nextLine();

            // TODO just for testing!! place all ships!
            if (Ship.validate_input(input, input2)) {
                break;
            }

            System.out.println("ERROR: invalid input!");

            
            // TODO
            // Ship new_ship = new Ship();
        }

        System.out.println(p1_board.toString());



    }

}