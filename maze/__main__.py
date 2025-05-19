import sys
from window import Window
from maze import Maze
from solver import Solver

def main(*args, **kwargs):
    wind = Window(800, 600)

    mz = Maze(10, 10, 30, 30, 15, 15)
    mz.create_sidewinder_maze()

    lines = mz.get_render_lines()
    for line in lines:
        wind.draw_line(line, fill_color="black")

    solver = Solver()
    solver.set_end(mz.get_stop())
    solver.set_start(mz.get_start())
    path = solver.breadth_solve()
    path_lines = mz.get_path_lines(path)

    for line in path_lines:
        wind.draw_line(line, fill_color="red")
    wind.wait_for_close()


if __name__ == "__main__":
    main(sys.argv)