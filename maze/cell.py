

# lets go for most likely to be rewritten class!
class Cell():
    def __init__(self, row, col, tags={}):
        self.row = row
        self.col = col
        self.tags = tags
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.links = []

    def connect(self, cell):
        if not isinstance(cell, Cell):
            return
        if not cell in self.links and not cell is None:
            self.links.append(cell)
        if not self in cell.links and not cell is None:
            cell.links.append(self)

    def get_tags(self):
        return self.tags
    
    def is_connected(self, other):
        return not other is None and other in self.links
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def __str__(self):
        return f'({self.row}, {self.col})'
