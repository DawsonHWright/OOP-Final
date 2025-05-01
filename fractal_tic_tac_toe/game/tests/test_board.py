import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_empty_board_not_won(self):
        board = Board(isBig=False)
        self.assertEqual(board.isWon(), -1)

    def test_win_row(self):
        board = Board(isBig=False)
        for i in range(3):
            board._children[0][i].status = 1
        self.assertEqual(board.isWon(), 1)

    def test_win_col(self):
        board = Board(isBig=False)
        for i in range(3):
            board._children[i][1].status = 0
        self.assertEqual(board.isWon(), 0)

    def test_win_diag(self):
        board = Board(isBig=False)
        for i in range(3):
            board._children[i][i].status = 1
        self.assertEqual(board.isWon(), 1)

    def test_draw(self):
        board = Board(isBig=False)
        # Fill all cells with no winner
        fill = [[0, 1, 0], [1, 0, 1], [1, 0, 1]]
        for i in range(3):
            for j in range(3):
                board._children[i][j].status = fill[i][j]
        self.assertEqual(board.isWon(), 2)
