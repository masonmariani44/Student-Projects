class MinesweeperBoard:

    def __init__(self, height, width, bomb_count):

        # create empty board
        # set all bombs
        # update board values for bombs

        # might cause crash, allocate space for new empty lists!!!
        self.board = []
        for i in range(0, height):
            for j in range(0, width):
                self.board[i].append(0)
        
        

        