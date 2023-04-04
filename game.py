import numpy as np

# initialize the board
board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

# function to print the board
def print_board():
    print(board[0])
    print(board[1])
    print(board[2])

# function to check if a player has won
def check_win(player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

# function to check if the game is a tie
def check_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

# game loop
while True:
    # player 1's turn
    print("Player 1's turn (X)")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if board[row][col] == '-':
        board[row][col] = 'X'
    else:
        print("Invalid move. Try again.")
        continue
    print_board()
    if check_win('X'):
        print("Player 1 wins!")
        break
    if check_tie():
        print("It's a tie!")
        break

    # player 2's turn
    print("Player 2's turn (O)")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if board[row][col] == '-':
        board[row][col] = 'O'
    else:
        print("Invalid move. Try again.")
        continue
    print_board()
    if check_win('O'):
        print("Player 2 wins!")
        break
    if check_tie():
        print("It's a tie!")
        break



