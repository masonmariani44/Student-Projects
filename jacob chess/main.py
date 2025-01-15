from Board import BoardClass


def validate_select(row, col, board, cur_player):

    # assert digit
    while row.isdigit() or col.isdigit() is False:
        print("Input must be digit")
        row, col = get_input()

    # assert bounds
    while row > 7 or row < 0 or col > 7 or col < 0:
        print("Input must be between 0 and 7")
        row, col = get_input()

    cur_piece = board.cur_board[row][col]

    while cur_piece[0] != cur_player:
        print("Input must be your piece")
        row, col = get_input()
        cur_piece = board.cur_board[row][col]

    
        


def get_input():
    selected_row = input("Select row: ")
    selected_col = input("Select col: ")
    return selected_row, selected_col


def main():

    board = BoardClass()

    cur_player = "w"


    while True:

        # TODO print current board

        selected_row_start, selected_col_start = get_input()
        validate_select(selected_row_start, selected_col_start, board, cur_player)

        selected_row_end, selected_col_end = get_input()
        validate_select(selected_row_end, selected_col_end, board, cur_player)


main()


"""

init the board
keep track of whos turn it is
have current player choose a piece
    attempt to move the piece
    validate the move (legal)
move piece, update board
check current game state
swap player
"""