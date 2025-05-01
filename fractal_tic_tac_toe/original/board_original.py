import numpy as np

class SmallBoard:
    def __init__(self):
        self.board = np.full((3, 3), ' ')
        self.winner = None

    def display(self):
        return "\n".join([" | ".join(self.board[i]) for i in range(3)])

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i, :] == self.board[i, 0]) and self.board[i, 0] != ' ':
                self.winner = self.board[i, 0]
                return self.winner
            if all(self.board[:, i] == self.board[0, i]) and self.board[0, i] != ' ':
                self.winner = self.board[0, i]
                return self.winner
        if all(self.board.diagonal() == self.board[0, 0]) and self.board[0, 0] != ' ':
            self.winner = self.board[0, 0]
            return self.winner
        if all(np.fliplr(self.board).diagonal() == self.board[0, 2]) and self.board[0, 2] != ' ':
            self.winner = self.board[0, 2]
            return self.winner
        if not np.any(self.board == ' '):
            self.winner = 'Draw'
            return 'Draw'
        return None

    def make_move(self, row, col, player):
        if self.board[row, col] == ' ' and not self.winner:
            self.board[row, col] = player
            return True
        return False

class FractalTicTacToe:
    def __init__(self):
        self.boards = [[SmallBoard() for _ in range(3)] for _ in range(3)]
        self.main_board = SmallBoard()
        self.current_player = 'X'
        self.next_board = None

    def display(self):
        result = ""
        for i in range(3):
            for row in range(3):
                result += " || ".join([" | ".join(self.boards[i][j].board[row]) for j in range(3)]) + "\n"
            result += "-" * 33 + "\n"
        return result

    def check_main_board_winner(self):
        for i in range(3):
            # Check row
            if all(self.boards[i][j].winner == self.current_player for j in range(3)):
                return self.current_player
            # Check column
            if all(self.boards[j][i].winner == self.current_player for j in range(3)):
                return self.current_player
        # Check diagonals
        if all(self.boards[i][i].winner == self.current_player for i in range(3)):
            return self.current_player
        if all(self.boards[i][2-i].winner == self.current_player for i in range(3)):
            return self.current_player
        return None

    def play_turn(self, board_row, board_col, cell_row, cell_col):
        if self.next_board is not None and (board_row, board_col) != self.next_board:
            print("You must play in the designated board:", self.next_board)
            return False

        if self.boards[board_row][board_col].make_move(cell_row, cell_col, self.current_player):
            self.boards[board_row][board_col].check_winner()
            
            # Check if the main game has a winner
            if self.boards[board_row][board_col].winner == self.current_player:
                self.main_board.board[board_row, board_col] = self.current_player
                self.main_board.check_winner()
                if self.main_board.winner:
                    print("Player", self.current_player, "wins the game!")
                    return True

            # Determine next board
            if self.boards[cell_row][cell_col].winner is None:
                self.next_board = (cell_row, cell_col)
            else:
                self.next_board = None  # Free choice if board is won or drawn

            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            print("Invalid move, try again.")
            return False

# Start the game
game = FractalTicTacToe()
game.display()