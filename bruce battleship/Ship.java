

public class Ship {

    int size;
    int x_pos;
    int y_pos;
    Direction dir;

    public enum Direction {
        UP,
        DOWN,
        LEFT,
        RIGHT
    }

    public Ship(int size, int x_pos, int y_pos, Direction dir) {
        this.size = size;
        this.x_pos = x_pos;
        this.y_pos = y_pos;
        this.dir = dir;
    }

    static public boolean validate_input(String coord_str, String dir_str) {

        // TODO!!!!! use direction and length to check if end of ship is out of bounds


        // first check x coord

        // "15 e"
        // ["15", "e"]

         
        String[] split_str = coord_str.split(" ");

        if (split_str.length != 2) {
            return false;
        }

        int first_val = Integer.valueOf(split_str[0]);
        char second_val = split_str[1].charAt(0);


        if (first_val < 0 || first_val > 10) {
            return false;
        }

        
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