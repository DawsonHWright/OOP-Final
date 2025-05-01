import pygame
from board import Board
from square import Square


class Fractal:
    def __init__(self, screen_size=600, margin=0.01):
        pygame.init()
        self.screen_size = screen_size
        self.margin = margin
        self.screen = pygame.display.set_mode((self.screen_size,
                                               self.screen_size))
        pygame.display.set_caption("Fractal Tic-Tac-Toe")

        self.main_board = Board(isBig=True)
        self.current_player = 0
        self.next_board = None
        self.main_winner = -1
        self.clock = pygame.time.Clock()

    def get_cell_from_pos(self, pos, board_rect):
        """Return (row, col) 3x3 grid for a given mouse position and rect."""
        x, y = pos
        rel_x = x - board_rect.left
        rel_y = y - board_rect.top
        cell_w = board_rect.width / 3
        cell_h = board_rect.height / 3
        col = int(rel_x // cell_w)
        row = int(rel_y // cell_h)
        if 0 <= row < 3 and 0 <= col < 3:
            return (row, col)
        return None

    def handle_mouse_click(self, pos):
        """Handle mouse click: checks big board, small board, places move."""
        clicked_big = self.get_cell_from_pos(pos, self.screen.get_rect())
        if not clicked_big:
            return

        big_row, big_col = clicked_big

        if self.next_board is not None\
           and (big_row, big_col) != self.next_board:
            return  # Not allowed to play here

        # Locate mini board
        working_rect = self.screen.get_rect().inflate(
            -2 * int(self.screen_size * self.margin),
            -2 * int(self.screen_size * self.margin)
        )
        margin_px = int(self.screen_size * self.margin)
        cell_w = (working_rect.width - 2 * margin_px) / 3
        cell_h = (working_rect.height - 2 * margin_px) / 3
        board_x = working_rect.left + big_col * (cell_w + margin_px)
        board_y = working_rect.top + big_row * (cell_h + margin_px)
        small_rect = pygame.Rect(board_x, board_y, cell_w, cell_h)

        clicked_small = self.get_cell_from_pos(pos, small_rect)
        if not clicked_small:
            return

        small_row, small_col = clicked_small

        self.make_move(big_row, big_col, small_row, small_col)

    def make_move(self, big_row, big_col, small_row, small_col):
        """Attempts to place a move on the board and update game state."""
        big_board = self.main_board._children[big_row][big_col]
        if isinstance(big_board, Board):
            small_square = big_board._children[small_row][small_col]
            if small_square.playHere(self.current_player):
                winner = big_board.isWon()
                if winner in [0, 1]:  # Only replace if one player won
                    self.main_board._children[big_row][big_col] = Square()
                    self.main_board._children[big_row][big_col].status = winner
                # If winner == 2 (draw), leave the mini-board visible & greyed

                self.main_winner = self.main_board.isWon()

                # Update next board constraint
                self.next_board = (small_row, small_col)
                if isinstance(self.main_board._children[small_row][small_col],
                              Square):
                    self.next_board = None  # Free choice
                elif hasattr(self.main_board._children[small_row][small_col],
                             'status'):
                    if self.main_board._children[small_row][small_col]\
                            .status == 2:
                        self.next_board = None  # Free choice if tied

                # Switch players
                self.current_player = 1 - self.current_player

    def draw(self):
        """Draws the full board."""
        self.screen.fill((0, 0, 0))
        self.main_board.draw(self.screen, self.margin, play_mode=0,
                             playable=self.next_board)
        pygame.display.flip()

    def loop(self):
        """Main game loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.main_winner == -1 and\
                   event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(pygame.mouse.get_pos())

            self.draw()
            self.clock.tick(60)

        pygame.quit()
