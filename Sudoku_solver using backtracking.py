def is_valid(board, r, c, ch):
    for i in range(9):
        if board[i][c] == ch or board[r][i] == ch or \
           board[3*(r//3)+i//3][3*(c//3)+i%3] == ch:
            return False
    return True

def solve_sudoku(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for ch in "123456789":
                    if is_valid(board, r, c, ch):
                        board[r][c] = ch
                        if solve_sudoku(board):
                            return True
                        board[r][c] = "."
                return False
    return True

# Test board (incomplete Sudoku)
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)
for row in board:
    print(" ".join(row))
