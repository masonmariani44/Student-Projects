#include <"stdlib.h">
#include <"stdio.h">
#include <"time.h">

int size_x = 10;
int size_y = 10;

int bomb_count = 5;

int board[10][10];

// TODO x and y might be reversed
void print_board() {
    for (int x = 0; x < size_x; x++) {
        for (int y = 0; y < size_y; y++) {
            printf(" %d ", board[x][y]);
        }
        printf("\n");
    }
}


void init_board() {
    for (int x = 0; x < size_x; x++) {
        for (int y = 0; y < size_y; y++) {
            board[x][y] = 0;
        }
    }
}

void set_mines() {

    for (int i = 0; i < bomb_count; i++) {
        int x = rand() % (size_x - 0 + 1) + 0;
        int y = rand() % (size_y - 0 + 1) + 0;
        bomb_count[x][y] = -1;
    }

}

void set_numbers() {

    for (int x = 0; x < size_x; x++) {
        for (int y = 0; y < size_y; y++) {
            if (board[x][y] == -1) {

                // TODO check for out of bounds
                board[x-1][y+1]++;
                board[x][y+1]++;
                board[x+1][y+1]++;
                board[x-1][y]++;
                board[x+1][y]++;
                board[x-1][y-1]++;
                board[x][y-1]++;
                board[x+1][y-1]++;

            }
        }
    }

}



int main() {
    srand(time(NULL));

    init_board();
    set_mines();
    set_numbers();

    return 0;
}