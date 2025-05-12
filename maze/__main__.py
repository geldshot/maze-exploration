import sys
from window import Window
from line import Line
from point import Point
from cell import Cell

def main(*args, **kwargs):
    wind = Window(800, 600)

    lines = [
        Line(Point(0,0),Point(200,200)),
        Line(Point(200,0),Point(0,200))
    ]
    for line in lines:
        wind.draw_line(line)

    cells = [
        Cell(i*50+50, 300, 50) for i in range(10)
    ]

    render_lines = []
    for cell in cells:
        render_lines.extend(cell.get_render_lines())


    for line in render_lines:
        wind.draw_line(line[0], line[1])
    for cell in cells:
        wind.draw_cell(cell)

    path = [
        cells[0],
        cells[2],
        cells[5]
    ]

    path_lines = build_path(path)

    for line in path_lines:
        wind.draw_line(line)

    wind.wait_for_close()

def build_path(cells):
    if not cells:
        return
    path = []
    a1 = cells[0].get_center()

    for index in range(len(cells)-1):
        a2 = cells[index+1].get_center()
        path.append(Line(Point(a1[0],a1[1]),Point(a2[0], a2[1])))
        a1 = a2
    return path

if __name__ == "__main__":
    main(sys.argv)