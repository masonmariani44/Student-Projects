public class Board {

    public Cell[][] board = new Cell[10][10];

    public Board() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                this.board[i][j] = new Cell(Cell.Status.EMPTY);
            }
        }
    }

    public boolean AddShipToBoard(Ship add_ship) {

        int cell_num = 1;
        int x = add_ship.x_pos;
        int y = add_ship.y_pos;
        while (cell_num <= add_ship.size) {
            if (x < 0)
                return false;
            if (y < 0)
                return false;
            if (x > 9)
                return false;
            if (y > 9)
                return false;

            if (this.board[y][x].status == Cell.Status.UNHIT) {
                return false;
            }

            if (add_ship.dir == Ship.Direction.UP) {
                y -= 1;
            }
            if (add_ship.dir == Ship.Direction.DOWN) {
                y += 1;
            }
            if (add_ship.dir == Ship.Direction.LEFT) {
                x -= 1;
            }
            if (add_ship.dir == Ship.Direction.RIGHT) {
                x += 1;
            }

            cell_num += 1;
        }

        cell_num = 1;
        x = add_ship.x_pos;
        y = add_ship.y_pos;
        while (cell_num <= add_ship.size) {
            this.board[y][x].status = Cell.Status.UNHIT;

            if (add_ship.dir == Ship.Direction.UP) {
                y -= 1;
            }
            if (add_ship.dir == Ship.Direction.DOWN) {
                y += 1;
            }
            if (add_ship.dir == Ship.Direction.LEFT) {
                x -= 1;
            }
            if (add_ship.dir == Ship.Direction.RIGHT) {
                x += 1;
            }

            cell_num += 1;
        }
        return true;
    }

    public boolean validate_shot(String coords) {
        String[] split_str = coords.split(" ");

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

        Cell.Status shot_status = this.board[(int) second_val - 97][first_val - 1].status;
        if (shot_status != Cell.Status.EMPTY && shot_status != Cell.Status.UNHIT) {
            return false;
        }

        return true;

    }

    /*
     * 
     * TODO PLEASEEEE FIX NOOOWWW!!!!1
     * 
     * we used to access the board via board[x][y]
     * instead, we need to do board[y][x]
     * 
     * also change 60/61 to be 97 instead, which is what the ascii code for a is
     */
    public void take_shot(String coords) {
        String[] split_str = coords.split(" ");
        int first_val = Integer.valueOf(split_str[0]);
        char second_val = split_str[1].charAt(0);

        Cell.Status shot_status = this.board[(int) second_val - 97][first_val - 1].status;

        if (shot_status == Cell.Status.EMPTY) {
            this.board[first_val - 1][(int) second_val - 61].status = Cell.Status.EMPTY_MISS;
        }
        if (shot_status == Cell.Status.UNHIT) {
            this.board[first_val - 1][(int) second_val - 61].status = Cell.Status.HIT;
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {

                if (this.board[i][j].status == Cell.Status.EMPTY) {
                    sb.append('O');
                }
                if (this.board[i][j].status == Cell.Status.EMPTY_MISS) {
                    sb.append('/');
                }
                if (this.board[i][j].status == Cell.Status.UNHIT) {
                    sb.append('=');
                }
                if (this.board[i][j].status == Cell.Status.HIT) {
                    sb.append('X');
                }

            }
            sb.append('\n');
        }
        return sb.toString();
    }

}