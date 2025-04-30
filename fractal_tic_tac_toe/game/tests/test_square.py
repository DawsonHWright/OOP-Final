import unittest
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
