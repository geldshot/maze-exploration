import sys
from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main(*args, **kwargs):
    wind = Window(800, 600)

    mz = Maze(10, 10, 5, 5, 50, 50, wind)
    lines = mz.get_render_lines()
    for line in lines:
        wind.draw_line(line, fill_color="black")
    wind.wait_for_close()


if __name__ == "__main__":
    main(sys.argv)