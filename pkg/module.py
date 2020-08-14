def print_board(soduku_board):
    """
    Prints out a nicer looking soduku board
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(soduku_board[i][j]))
            else:
                print(str(soduku_board[i][j]) + " ", end="")


def condition(soduku_board, i, j, k):
    """
    Checks if the rules of the game have been broken
    Returns:
        True/False
    """

    def row():
        for a in range(9):
            if soduku_board[i][a] == k:  # and j != a
                return False
        return True

    def columns():
        for a in range(9):
            if soduku_board[a][j] == k:  # and i != a
                return False
        return True

    # ii/jj is for the mini 3*3 square that the function has to go through
    def box():
        ii = i // 3
        jj = j // 3

        for a in range(ii * 3, ii * 3 + 3):
            for b in range(jj * 3, jj * 3 + 3):
                if soduku_board[a][b] == k:  # and (a, b) != (i, j)
                    return False
        return True

    if row() and columns() and box():
        return True


def slot_to_be_filled(soduku_board):
    """
    Returns:
        The coordinates of the next 0 in the board
        1 if there are no more 0s left
    """
    for i in range(9):
        for j in range(9):
            if soduku_board[i][j] == 0:
                return i, j
    return 1
