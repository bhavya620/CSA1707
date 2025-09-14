# Simple Tic Tac Toe Game in Python (Player vs Player)

board = [" " for _ in range(9)]  # 3x3 board (flattened)

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(player):
    # Winning combinations (rows, cols, diagonals)
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

def play_game():
    current_player = "X"
    while True:
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full():
            print_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
