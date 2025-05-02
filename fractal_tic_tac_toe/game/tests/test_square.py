import unittest
from unittest.mock import patch, MagicMock
from square import Square


class TestSquare(unittest.TestCase):
    def test_play_valid(self):
        sq = Square()
        self.assertTrue(sq.playHere(0))
        self.assertEqual(sq.status, 0)

    def test_play_invalid(self):
        sq = Square()
        sq.playHere(1)
        self.assertFalse(sq.playHere(0))
        self.assertEqual(sq.status, 1)

    def test_is_owned(self):
        sq = Square()
        self.assertFalse(sq.isOwned())
        sq.playHere(1)
        self.assertTrue(sq.isOwned())

    @patch("square.draw.line")
    @patch("square.draw.circle")
    @patch("square.draw.rect")
    def test_square_draw(self, mock_rect, mock_circle, mock_line):
        mock_surface = MagicMock()
        mock_surface.get_size.return_value = (100, 100)
        mock_rect_obj = MagicMock()
        mock_rect_obj.inflate.return_value = mock_rect_obj
        mock_rect_obj.width = 100
        mock_rect_obj.height = 100
        mock_rect_obj.center = (50, 50)
        mock_rect_obj.topleft = (0, 0)
        mock_rect_obj.topright = (100, 0)
        mock_rect_obj.bottomleft = (0, 100)
        mock_rect_obj.bottomright = (100, 100)
        mock_surface.get_rect.return_value = mock_rect_obj

        s1 = Square()
        s1.draw(mock_surface, margin=0.01, play_mode=0)
        self.assertFalse(mock_circle.called)
        self.assertFalse(mock_line.called)
        mock_circle.reset_mock()
        s2 = Square()
        s2.status = 0
        s2.draw(mock_surface, margin=0.01, play_mode=0)
        self.assertTrue(mock_circle.called)
        mock_line.reset_mock()
        s3 = Square()
        s3.status = 1
        s3.draw(mock_surface, margin=0.01, play_mode=0)
        self.assertTrue(mock_line.called)
        mock_rect.reset_mock()
        s4 = Square()
        s4.draw(mock_surface, margin=0.01, play_mode=-1)
