from board_original import FractalTicTacToe


def play_game():
    game = FractalTicTacToe()  # This line creates the game instance
    print("Welcome to Fractal Tic-Tac-Toe!")
    print("Player X and Player O will take turns.")
    print("To make a move, enter the large board row and column (0-2) and then the small board row and column (0-2).")

    while True:
        print(game.display())
        print(f"Player {game.current_player}'s turn.")

        if game.next_board is not None:
            print(f"You must play in board {game.next_board}.")

        try:
            board_row = int(input("Enter large board row (0-2): "))
            board_col = int(input("Enter large board column (0-2): "))
            cell_row = int(input("Enter small board row (0-2): "))
            cell_col = int(input("Enter small board column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if not (0 <= board_row < 3 and 0 <= board_col < 3 and 0 <= cell_row < 3 and 0 <= cell_col < 3):
            print("Invalid move. Please choose numbers between 0 and 2.")
            continue

        if game.play_turn(board_row, board_col, cell_row, cell_col):
            if game.main_board.winner:
                print(game.display())
                print(f"Player {game.main_board.winner} wins the game!")
                break
