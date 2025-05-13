import unittest

from maze.maze import Maze
from maze.line import Line
from maze.point import Point
from maze.cell import Cell

class TestMaze(unittest.TestCase):
    def test_simple_setup(self):
        mz = Maze(0, 0, 2, 2, 1, 1)

        expected = [[
            Cell(0,0),
            Cell(1,0)
        ],[
            Cell(0,1),
            Cell(1,1)
        ]]

        self.assertEqual(expected, mz.get_cells())

    def test_render_lines(self):
        mz = Maze(0, 0, 1, 1, 1, 1)

        expected = [
            Line(Point(0,0),Point(1,0)),
            Line(Point(0,0),Point(0,1)),
            Line(Point(1,0),Point(1,1)),
            Line(Point(0,1),Point(1,1))
        ]
        lines = mz.get_render_lines()

        self.assertEqual(expected, lines)