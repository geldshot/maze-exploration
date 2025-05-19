import random

from cell import Cell
from line import Line
from point import Point

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
        self._start = None
        self._stop = None

        self._cells = []

        self._create_cells()

    def get_cells(self):
        return self._cells
    
    def get_random_cell(self):
        col = random.randint(0,self.num_cols)
        row = random.randint(0,self.num_rows)
        return self._cells[row][col]
    
    def get_start(self):
        return self._start
    
    def get_stop(self):
        return self._stop

    def _create_cells(self):
        cells = []
        for row in range(self.num_rows):
            cells.append([])
            for col in range(self.num_cols):
                cells[row].append(Cell(col, row))
                if row > 0:
                    cells[row-1][col].down = cells[row][col]
                    cells[row][col].up = cells[row-1][col]
                if col > 0:
                    cells[row][col-1].right = cells[row][col]
                    cells[row][col].left = cells[row][col-1]
        self._cells = cells

    def reset(self):
        self._create_cells()

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
    
    def get_path_lines(self, cells=[]):
        lines = []
        c1 = cells[0]
        for i in range(len(cells)-1):
            c2 = cells[i+1]
            lines.append(self._line_adjusted(c1.col+.5, c1.row+.5, c2.col+.5, c2.row+.5))
        return lines
    
    def create_binary_maze(self):
        self._start = self._cells[0][0]
        self._stop = self._cells[-1][-1]
        to_visit = []
        for row in self._cells:
            to_visit.extend(row)
        
        for cell in to_visit:
            right = random.randint(0,1)==1
            if right and not cell.right is None:
                cell.connect(cell.right)
            if not right and not cell.down is None: 
                cell.connect(cell.down)

            if right and cell.right is None:
                cell.connect(cell.down) 
            if not right and cell.down is None:
                cell.connect(cell.right)

    def create_sidewinder_maze(self):
        self._start = self._cells[0][0]
        self._stop = self._cells[-1][-1]
        run = []
        for row in self._cells:
            
            for cell in row:
                right = random.randint(0,1)==1
                run.append(cell)
                if not right and not cell.down is None:
                    chosen = random.choice(run)
                    chosen.connect(chosen.down)
                    run.clear()
                elif not cell.right is None:
                    cell.connect(cell.right)
                else:
                    cell.connect(cell.down)
            run.clear()