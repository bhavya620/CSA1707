# Tic Tac Toe with Minimax Algorithm (Player vs Computer)

import math

board = [" " for _ in range(9)]  # 3x3 board

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in win_combos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_full():
    return " " not in board

# Minimax function
def minimax(is_maximizing):
    if check_winner("O"):  # Computer wins
        return 1
    if check_winner("X"):  # Human wins
        return -1
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# Best move for computer
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
def play_game():
    print("Tic Tac Toe - You are X, Computer is O")
    while True:
        print_board()
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("🎉 You win!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break

        # Computer's turn
        comp_move = best_move()
        board[comp_move] = "O"

        if check_winner("O"):
            print_board()
            print("💻 Computer wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break

# Run the game
play_game()
