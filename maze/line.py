
class Line():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.start.x, self.start.y, self.stop.x, self.stop.y, fill=fill_color, width=2
        )


