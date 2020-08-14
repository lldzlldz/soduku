import random

from pkg.module import *

d = {"counter": 0}

# makes a complete solution before randomly removing the number in the cells
# not doing the method of putting numbers randomly according to the rules of the game as
# doing so might make the problem unsolvable


def main():
    soduku_board = create_board()
    fill_board(soduku_board)
    remove_cell(soduku_board)
    print_board(soduku_board)
    print(d["counter"])
    print()


def create_board():
    """Creates a blank soduku board"""
    return [[0] * 9 for i in range(9)]


def rand(generated_numbers):
    """
    Returns a random number generated such that it does not have a duplicate
    in the same row
    """
    if not generated_numbers:
        generated_numbers = list(range(1, 10))
    k = random.choice(generated_numbers)
    generated_numbers.remove(k)
    return k, generated_numbers


def fill_board(soduku_board, generated_numbers=list(range(1, 10))):
    """
    Makes a completed, sovled soduku board
    """
    d["counter"] += 1
    # base case
    if slot_to_be_filled(soduku_board) == 1:
        return True
        # recursive case
    i, j = slot_to_be_filled(soduku_board)
    # a is in range(9) so that it can try out all the different combinations in a cell from 1-9
    # if range is too small, then all the combinations cannot be tried out
    # if range is too big, then there will be some repeated backtracking, possibly increasing the number of recursions needed
    for a in range(9):
        k, generated_numbers = rand(generated_numbers)
        if condition(soduku_board, i, j, k):
            generated_numbers.append(k)
            soduku_board[i][j] = k

            if fill_board(soduku_board, generated_numbers):
                return True
            # makes the previously filled space unfilled again(with 0)
            # need to put this statement into a loop or there will be no backtracking
            soduku_board[i][j] = 0
    # starts the backtracking
    return False


def remove_cell(soduku_board, t=[]):
    """
    Randomly changes some cells to become unsolved(0)
    """
    while len(t) < 65:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        tt = [i, j]
        t.append(tt)
    for i, j in t:
        soduku_board[i][j] = 0
    return soduku_board


if __name__ == "__main__":
    main()

