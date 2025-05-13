import unittest

from maze.cell import Cell

class TestCell(unittest.TestCase):
    def test_eq(self):
        c1 = Cell(1, 2)
        c2 = Cell(1, 2)
        c3 = Cell(2, 2)

        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)

    def test_is_connected_true(self):
        c1 = Cell(1, 1)
        c2 = Cell(1, 2)
        c1.right = c2
        c2.left = c1

        c1.connect(c2)

        self.assertTrue(c1.is_connected(c2))

    def test_is_connected_false(self):
        c1 = Cell(1, 1)
        c2 = Cell(1, 2)
        c1.right = c2
        c2.left = c1

        self.assertFalse(c1.is_connected(c2))