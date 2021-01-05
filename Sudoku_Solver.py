# This takes a Sudoku puzzle given as a nested list and returns the solved
# Sudoku puzzle using back tracing algorithm.

sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

sudoku_board2 = [
    [5, 1, 7, 6, 0, 0, 0, 3, 4],
    [2, 8, 9, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

hardest_sudoku = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def solve(sb):
    empty = empty_square(sb)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if valid(sb, i, (row, col)):
            sb[row][col] = i

            if solve(sb):
                return True

            sb[row][col] = 0

    return False


def valid(sb, num, pos):
    # check row
    for i in range(len(sb[0])):
        if sb[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(sb)):
        if sb[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sb[i][j] == num and (i, j) != pos:
                return False
    return True


def board_maker(sb):
    for i in range(len(sb)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(sb[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sb[i][j])
            else:
                print(str(sb[i][j]) + " ", end="")


def empty_square(sb):
    for i in range(len(sb)):
        for j in range(len(sb[0])):
            if sb[i][j] == 0:
                return i, j  # row, column
    return None


board_maker(hardest_sudoku)
solve(hardest_sudoku)
print("_______________________")
board_maker(hardest_sudoku)
