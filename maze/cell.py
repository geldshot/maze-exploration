from line import Line
from point import Point

# lets go for most likely to be rewritten class!
class Cell():
    def __init__(self, x, y, size, tags={}, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self._x = x
        self._y = y
        self._size = size
        self.tags = tags
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall

    def draw(self, canvas):
        if self.left_wall:
            canvas.create_line(self._x, self._y, self._x, self._y+self._size, fill="black", width=2)
        if self.right_wall:
            canvas.create_line(self._x+self._size, self._y, self._x+self._size, self._y+self._size, fill="black", width=2)
        if self.top_wall:
            canvas.create_line(self._x, self._y, self._x+self._size, self._y, fill="black", width=2)
        if self.bottom_wall:
            canvas.create_line(self._x, self._y+self._size, self._x+self._size, self._y+self._size, fill="black", width=2)

    def get_loc(self):
        return (self._x, self._y)

    def get_center(self):
        return (self._x + self._size/2, self._y + self._size/2)
    
    def get_render_lines(self):
        lines = []
        if self.left_wall:
            lines.append((
                Line(
                    Point(self._x, self._y),
                    Point(self._x, self._y+self._size)
                    ),
                    "black"))
        if self.right_wall:
            lines.append((
                Line(
                    Point(self._x + self._size, self._y),
                    Point(self._x+self._size, self._y+self._size)
                    ),
                    "black"))
        if self.top_wall:
            lines.append((
                Line(
                    Point(self._x, self._y),
                    Point(self._x+self._size, self._y)
                    ),
                    "black"))
        if self.bottom_wall:
            lines.append((
                Line(
                    Point(self._x, self._y+self._size),
                    Point(self._x+self._size, self._y+self._size)
                    ),
                    "black"))
        return lines

    def draw_move(self, canvas,  to_cell, undo=False):
        start = (self._x + self._size/2, self._y + self._size / 2)
        stop = to_cell.get_loc()
        fill_color="gray"
        if undo:
            fill_color = "red"
        canvas.create_line(start[0], start[1], stop[0], stop[1], fill=fill_color, width=2)
