# Check whether queen can be placed safely
def isSafe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Solve N-Queens using backtracking
def solveNQueens(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if isSafe(board, row, col, n):

            board[row][col] = 1

            if solveNQueens(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main program
n = int(input("Enter value of N: "))

if n <= 0:
    print("N must be positive.")

else:
    board = [[0 for j in range(n)] for i in range(n)]

    # Place first queen
    board[0][1] = 1

    if solveNQueens(board, 0, n):

        print("\nSolution (Q = Queen, . = Empty):")

        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

    else:
        print("No solution exists with the first queen in that column.")