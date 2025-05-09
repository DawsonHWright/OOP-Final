import unittest
from unittest.mock import patch, MagicMock
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
        board._children[0][0].status = -1
        for i in range(3):
            board._children[i][2 - i].status = 1
        self.assertEqual(board.isWon(), 1)

    def test_tie(self):
        board = Board(isBig=False)
        # Fill all cells with no winner
        fill = [[0, 1, 0], [1, 0, 1], [1, 0, 1]]
        for i in range(3):
            for j in range(3):
                board._children[i][j].status = fill[i][j]
        self.assertEqual(board.isWon(), 2)

    @patch("board.draw.line")
    @patch("board.draw.rect")
    def test_board_draw(self, mock_rect, mock_line):
        board = Board(isBig=False)
        mock_surface = MagicMock()
        mock_surface.get_size.return_value = (600, 600)
        mock_rect_obj = MagicMock()
        mock_surface.get_rect.return_value = mock_rect_obj
        mock_rect_obj.inflate.return_value = mock_rect_obj
        mock_rect_obj.left = 0
        mock_rect_obj.top = 0
        mock_rect_obj.width = 600
        mock_rect_obj.height = 600
        mock_child_surface = MagicMock()
        mock_surface.subsurface.return_value = mock_child_surface
        mock_child_surface.get_size.return_value = (600, 600)

        board.draw(mock_surface, margin=0.01, play_mode=0)
        self.assertEqual(mock_surface.subsurface.call_count, 9)
        self.assertTrue(mock_line.called)
        board.status = 2
        board.draw(mock_surface, margin=0.01, play_mode=0, playable=(0, 0))
