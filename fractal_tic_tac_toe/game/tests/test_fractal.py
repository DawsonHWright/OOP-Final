import unittest
from fractal import Fractal


class TestFractal(unittest.TestCase):
    def test_initial_state(self):
        game = Fractal()
        self.assertEqual(game.current_player, 0)
        self.assertEqual(game.main_winner, -1)
        self.assertIsNone(game.next_board)
