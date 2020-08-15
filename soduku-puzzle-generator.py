import copy
import itertools
import random

import soduku_solver
from pkg.module import *

d = {"counter": 0, "unique_counter": 0}

# makes a complete solution before randomly removing the numbers in cell
# not doing the method of putting numbers randomly according to the rules of the game as
# doing so might make the problem unsolvable
# to change the difficulty, change the paremeter of the remove_cell function in main()
def main():
    while True:
        soduku_board = create_board()
        fill_board(soduku_board)
        soduku_board = remove_cell(soduku_board, 40)
        d["unique_counter"] += 1
        if unique(soduku_board):
            break
    print_board(soduku_board)
    print(soduku_board)
    print("backtracking counter =", d["counter"])
    print("unique counter =", d["unique_counter"])
    print()


def unique(soduku_board):
    """Checks if there is only 1 solution for the soduku board."""
    a = copy.deepcopy(soduku_board)
    b = copy.deepcopy(soduku_board)
    soduku_solver.solver(a)
    soduku_solver.solver(b, 1)
    if a == b:
        return True
    return False


def create_board():
    """Creates a blank soduku board"""
    return [[0] * 9 for i in range(9)]


def rand(generated_numbers):
    """Returns a random number generated such that it does not have a duplicate
    in the same row
    """
    if not generated_numbers:
        generated_numbers = list(range(1, 10))
    k = random.choice(generated_numbers)
    generated_numbers.remove(k)
    return k, generated_numbers


def fill_board(soduku_board, generated_numbers=list(range(1, 10))):
    """Makes a completed, solved soduku board."""
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


def remove_cell(soduku_board, number=30):
    """Randomly changes some cells to become unsolved(0)

    number(1-81) refers to the number of solved cells
    """
    if number not in range(1, 82):
        print(
            "The number paremeter for the remove cell function is out of range"
        )
    combinations = list(itertools.product(range(0, 9), range(0, 9)))
    while len(combinations) > number:
        k = random.choice(combinations)
        combinations.remove(k)
        i, j = k
        soduku_board[i][j] = 0
    return soduku_board


if __name__ == "__main__":
    main()
