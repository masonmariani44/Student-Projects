
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        /*
         * 
         * 
         * start the game
         * pick current player
         * take their shot
         * verify shot
         * check if hit
         * update board
         * swap players
         * 
         */

        int player = 1;

        Board p1_board = new Board();
        Board p2_board = new Board();

        boolean valid = false;
        Scanner scanner = new Scanner(System.in);

        int[] sizes = { 5, 4, 3, 3, 2 };

        for (int i = 1; i <= 2; i++) {

            for (int size : sizes) {

                System.out.println("current size: " + size);

                while (!valid) {

                    // x is an int
                    // y is a char
                    // this is how the actual battleship game board looks
                    System.out.println("Enter position of ship: (x y) (ex. 7 b)");
                    String input = scanner.nextLine();

                    System.out.println("Enter orientation of ship: (u, d, l, r)");
                    String input2 = scanner.nextLine();

                    // TODO just for testing!! place all ships!
                    // TODO i think this is wrong!!! or opposite double check!!!
                    valid = Ship.validate_input(input, input2);

                    if (!valid) {
                        System.out.println("ERROR: invalid input!");
                    }

                    Ship.Direction dir = Ship.Direction.UP;
                    if (input2.equals("u")) {
                        dir = Ship.Direction.UP;
                    }
                    if (input2.equals("d")) {
                        dir = Ship.Direction.DOWN;
                    }
                    if (input2.equals("l")) {
                        dir = Ship.Direction.LEFT;
                    }
                    if (input2.equals("r")) {
                        dir = Ship.Direction.RIGHT;
                    }

                    String[] coord_split = input.split(" ");
                    int x_pos = Integer.valueOf(coord_split[0]);
                    // NOTE: 'a' is ascii code 97. a should be row #1 so subtract 97 from our y pos
                    // character
                    int y_pos = (int) coord_split[1].charAt(0) - 97;

                    // DEBUG STUFF
                    System.out.println("size: " + size + " x_pos: " + x_pos + " y_pos: " + y_pos + " dir: " + dir);

                    Ship new_ship = new Ship(size, x_pos, y_pos, dir);

                    if (i == 1) {
                        valid = p1_board.AddShipToBoard(new_ship);
                    } else {
                        valid = p2_board.AddShipToBoard(new_ship);
                    }

                }
                valid = false;

                if (i == 1) {
                    System.out.println(p1_board.toString());
                }

                else {
                    System.out.println(p2_board.toString());
                }

            }
        }

        // AFTER BOARD POPULATION START GAMEPLAY HERE!!!!!!
        // TODO Change to while not_game_over
        Board cur_update_board = p2_board;
        while (true) {

            // Get input from user and take shot at that location
            String coords = input_board_pos();
            cur_update_board.validate_shot(coords);
            cur_update_board.take_shot(coords);

            if (player == 1) {
                player = 2;
                cur_update_board = p1_board;
            } else {
                player = 1;
                cur_update_board = p2_board;
            }
        }

    }

    private static String input_board_pos() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter position of ship: (x y)");
        String input = scanner.nextLine();
        scanner.close();
        return input;
    }

}