

class Line():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start.x, self.start.y, self.stop.x, self.stop.y, fill=fill_color, width=2
        )

    def __eq__(self, other):
        return self.start == other.start and self.stop == self.stop
    
    def __add__(self, other):
        if isinstance(Line):
            return Line(self.start+other.start, self.stop+other.stop)
        else:
            return Line(self.start+other, self.stop+other)
    
    def __mul__(self, other):
        if isinstance(Line):
            return Line(self.start*other.start, self.stop*other.stop)
        else:
            return Line(self.start*other, self.stop*other)
    
    def __sub__(self, other):
        if isinstance(Line):
            return Line(self.start-other.start, self.stop-other.stop)
        else:
            return Line(self.start-other, self.stop-other)
        
    def __truediv__(self, other):
        if isinstance(Line):
            return Line(self.start/other.start, self.stop/other.stop)
        else:
            return Line(self.start/other, self.stop/other)

    def __str__(self):
        return f'start: {self.start}, stop: {self.stop}'
