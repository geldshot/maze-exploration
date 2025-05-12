import sys
from window import Window
from line import Line
from point import Point

def main(*args, **kwargs):
    wind = Window(800, 600)

    lines = [
        Line(Point(0,0),Point(200,200)),
        Line(Point(200,0),Point(0,200))
    ]
    for line in lines:
        wind.draw_line(line)
    wind.wait_for_close()

if __name__ == "__main__":
    main(sys.argv)