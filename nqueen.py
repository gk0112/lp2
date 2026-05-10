n = 4

board = [["." for _ in range(n)] for _ in range(n)]

def print_board():
    print("\n".join([" ".join(row) for row in board]))
    print("-" * 10)

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(row):
    if row == n:
        print("Solution Found:\n")
        print_board()
        return True

    for col in range(n):
        print(f"Trying Row {row}, Col {col}")

        if is_safe(row, col):
            board[row][col] = "Q"

            print(f"Placed Q at ({row},{col})")
            print_board()

            if solve(row + 1):
                return True

            board[row][col] = "."

            print(f"Backtracking from ({row},{col})")
            print_board()

    return False

solve(0)
