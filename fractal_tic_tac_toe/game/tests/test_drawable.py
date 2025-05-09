import unittest
from unittest.mock import MagicMock
from drawable import Drawable


class TestDrawable(unittest.TestCase):
    def test_assertion_error(self):
        mock_surface = MagicMock()
        mock_surface.get_size.return_value = (600, 600)
        self.assertRaises(NotImplementedError, Drawable.draw,
                          self, mock_surface, margin=0.1)
