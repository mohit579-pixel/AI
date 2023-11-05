def is_safe(board, row, col):
    # Check the vertical up direction
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False

    # Check the diagonal left direction
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the diagonal right direction
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def queens(board, row):
    global count
    if row == len(board):
        count += 1
        print_queens(board)
        return

    for j in range(len(board)):
        if is_safe(board, row, j):
            board[row][j] = 'Q'
            queens(board, row + 1)
            board[row][j] = 'X'  # Backtracking

def print_queens(board):
    print("-------Chess board--------")
    for row in board:
        print(' '.join(row))
    print()

if __name__ == "__main__":
    n = int(input(" Please Enter The Chess Board Size "))
    
    board = [['X' for _ in range(n)] for _ in range(n)]
    count = 0
    queens(board, 0)
    print(f"Total No. of Ways: {count}")
