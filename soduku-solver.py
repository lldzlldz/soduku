# for more info on recursive backtracking:
# https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf
from pkg.module import *

soduku_board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 1, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def main():
    solver(soduku_board)
    print_board(soduku_board)


def solver(soduku_board):
    # base case
    if slot_to_be_filled(soduku_board) == 1:
        return True
    # recursive case
    i, j = slot_to_be_filled(soduku_board)
    for k in range(1, 10):
        if condition(soduku_board, i, j, k):
            soduku_board[i][j] = k

            if solver(soduku_board):
                return True
            # makes the previously filled space unfilled again(with 0)
            soduku_board[i][j] = 0
    # starts the backtracking
    return False


if __name__ == "__main__":
    main()
