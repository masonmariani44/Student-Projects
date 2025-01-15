public class Cell {

    public enum Status {
        EMPTY,
        EMPTY_MISS,
        UNHIT,
        HIT
    }

    Status status;

    public Cell(Status cur_status) {
        this.status = cur_status;
    }

}