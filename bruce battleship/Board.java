public class Board {

    public Cell[][] board = new Cell[10][10];

    public Board() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                this.board[i][j] = new Cell(Cell.Status.EMPTY);
            }
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