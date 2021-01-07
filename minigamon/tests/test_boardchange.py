from unittest import TestCase
from minigamon.boardchange import boardchange

class BoardchangeTest(TestCase):
    def test_boardchange(self):
        self.assertEqual(boardchange([0, 2, 2, 2, 2, -2, -2, -2, -2, 0], 1, 3, 1), [0, 2, 2, 1, 3, -2, -2, -2, -2, 0])
        self.assertEqual(boardchange([0, -8, 0, 0, 3, 2, 1, 0], 1, 4, 4), [0, -8, 0, 0, 2, 2, 2, 0])
