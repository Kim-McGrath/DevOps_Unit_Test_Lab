def sudoku_solver(board):

    # validate the input board
    if not is_valid_board(board):
        return None

    # Make a copy of the board to avoid modifying the input
    board_copy = [row[:] for row in board]

    if solve(board_copy):
        return board_copy
    else:
        return None


def solve(board):
    # Recursive backtracking
    try:
        row, col = next(empty_cell(board))
    except StopIteration:
        return True  # No empty cells left, puzzle solved

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack

    return False


def empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                yield row, col


def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row, box_col = row // 3 * 3, col // 3 * 3
    if num in [
        board[box_row + i][box_col + j]
        for i in range(3)
        for j in range(3)
    ]:
        return False

    return True


def is_valid_board(board):
    # Check board dimensions
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False

    # Check values are between 0-9
    for row in board:
        for num in row:
            if not isinstance(num, int) or num < 0 or num > 9:
                return False

    # Check initial numbers don't violate Sudoku rules
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                # Temporarily set to 0 to check validity
                board[row][col] = 0
                if not is_valid(board, row, col, num):
                    board[row][col] = num
                    return False
                board[row][col] = num

    return True

