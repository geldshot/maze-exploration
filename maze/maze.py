from .cell import Cell
from .line import Line
from .point import Point

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        self._cells = []

        self._create_cells()

    def get_cells(self):
        return self._cells

    def _create_cells(self):
        cells = []
        for row in range(self.num_rows):
            cells.append([])
            for col in range(self.num_cols):
                cells[row].append(Cell(col, row))
                if row > 0:
                    cells[row-1][col].right = cells[row][col]
                    cells[row][col].left = cells[row-1][col]
                if col > 0:
                    cells[row][col-1].down = cells[row][col]
                    cells[row][col].up = cells[row][col-1]
        self._cells = cells

    def get_render_lines(self):
        r_lines = []

        for row in range(len(self._cells)):
            for col in range(len(self._cells[row])):
                
                if row == 0:
                    r_lines.append(self._line_adjusted(col, row, col+1, row))
                if col == 0:
                    r_lines.append(self._line_adjusted(col, row, col, row+1))

                cell = self._cells[row][col]
                right = cell.right
                down = cell.down

                if not cell.is_connected(right):
                    r_lines.append(self._line_adjusted(col+1, row, col+1,row+1))
                if not cell.is_connected(down):
                    r_lines.append(self._line_adjusted(col, row+1, col+1, row+1))
        return r_lines
    
    def _line(self, x1, y1, x2, y2):
        return Line(Point(x1,y1),Point(x2,y2))
    
    def _line_adjusted(self, x1, y1, x2, y2):
        x = self.x1
        y = self.y1
        h = self.cell_size_y
        w = self.cell_size_x
        return Line(Point(x+(x1*w), y+(y1*h)), Point(x+(x2*w), y+(y2*h)))