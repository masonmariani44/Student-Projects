

public class Ship {

    int size;
    int[][] coords;
    Direction dir;

    public enum Direction {
        UP,
        DOWN,
        LEFT,
        RIGHT
    }

    public Ship(int size, int[][] coords, Direction dir) {
        this.size = size;
        this.coords = coords;
        this.dir = dir;
    }

    static public boolean validate_input(String coord_str, String dir_str) {

        /*
         * FOR NEXT TIME!!!
         * Convert out of string (ie make sure input was valid)
         * 
         */


        // first check x coord

        // "15 e"
        // ["15", "e"]

         
        String[] split_str = coord_str.split(" ");

        if (split_str.length != 2) {
            return false;
        }

        int first_val = Integer.valueOf(split_str[0]);
        if (first_val < 1 || first_val > 10) {
            return false;
        }

        char second_val = split_str[1].charAt(0);
        if (second_val < 'a' || second_val > 'j') {
            return false;
        }

        char dir_char = dir_str.charAt(0);
        if (dir_char != 'u' && dir_char != 'd' && dir_char != 'l' && dir_char != 'r') {
            return false;
        }



        return true;

    }

}