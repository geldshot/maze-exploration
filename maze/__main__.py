import sys
from window import Window
from maze import Maze

def main(*args, **kwargs):
    wind = Window(800, 600)

    mz = Maze(10, 10, 20, 20, 25, 25)
    mz.create_binary_maze()

    lines = mz.get_render_lines()
    for line in lines:
        wind.draw_line(line, fill_color="black")
    wind.wait_for_close()


if __name__ == "__main__":
    main(sys.argv)