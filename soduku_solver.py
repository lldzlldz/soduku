# for more info on recursive backtracking:
# https://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf
from pkg.module import *

soduku_board = [
    [5, 2, 0, 0, 9, 6, 0, 0, 8],
    [0, 3, 0, 0, 5, 1, 0, 6, 9],
    [4, 0, 0, 0, 0, 8, 5, 3, 1],
    [1, 7, 0, 2, 6, 9, 0, 5, 0],
    [6, 5, 0, 0, 8, 0, 3, 0, 7],
    [0, 4, 2, 0, 0, 0, 0, 1, 6],
    [0, 1, 0, 0, 0, 0, 0, 9, 3],
    [3, 6, 0, 0, 0, 0, 7, 0, 0],
    [0, 8, 0, 6, 0, 0, 0, 4, 5],
]


def main():
    solver(soduku_board)
    print_board(soduku_board)


def solver(soduku_board, way=0):
    """Solves a partially filled/empty soduku board.
    
    If way = 1 --> solves in the opposite way.
    """
    # base case
    if slot_to_be_filled(soduku_board) == 1:
        return True
    # recursive case
    i, j = slot_to_be_filled(soduku_board)

    a, b, c = 1, 10, 1
    if way == 1:
        a, b, c = 9, 0, -1
    for k in range(a, b, c):
        if condition(soduku_board, i, j, k):
            soduku_board[i][j] = k

            if solver(soduku_board, way):
                return True
            # makes the previously filled cell unfilled again(with 0)
            soduku_board[i][j] = 0
    # starts the backtracking
    return False


if __name__ == "__main__":
    main()
