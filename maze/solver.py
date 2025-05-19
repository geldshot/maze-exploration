
from cell import Cell

class Solver():
    def __init__(self):
        self._visited = []
        self._start = None
        self._end = None
        self._path = []

    def set_start(self, start):
        self._start = start

    def get_start(self):
        return self._start

    def set_end(self, end):
        self._end = end

    def get_end(self):
        return self._end

    def reset(self):
        self._visited = []
        self._path = []

    def get_visited(self):
        return self._visited.copy()
    
    def basic_solve(self):
        if self._start is None:
            raise Exception("No start for solver")

        if self._end is None:
            raise Exception("No end for solver")
        
        if not isinstance(self._start, Cell):
            raise TypeError("start is not an instance of a Cell")
        
        if not isinstance(self._end, Cell):
            raise TypeError("end is not an instance of a Cell")

        to_visit = [self._start]
        visited = []
        path = []
        end = self._end
        next = None
        while to_visit:
            next = to_visit.pop()
            visited.append(next)
            for link in next.links:
                if link is end:
                    visited.append(link)
                    path.append((next, link))
                    self._visited = visited
                    self._path = path
                    return path.copy()
                if not link in visited and not link in to_visit:
                    to_visit.append(link)
                    path.append((next, link))
        
        raise Exception("could not find path to end")
    
    def breadth_solve(self):
        if self._start is None:
            raise Exception("No start for solver")

        if self._end is None:
            raise Exception("No end for solver")
        
        if not isinstance(self._start, Cell):
            raise TypeError("start is not an instance of a Cell")
        
        if not isinstance(self._end, Cell):
            raise TypeError("end is not an instance of a Cell")

        to_visit = [self._start]
        visited = []
        path = []
        end = self._end
        next = None
        while to_visit:
            next = to_visit.pop(0)
            visited.append(next)
            for link in next.links:
                if link is end:
                    visited.append(link)
                    path.append((next, link))
                    self._visited = visited
                    self._path = path
                    return path.copy()
                if not link in visited and not link in to_visit:
                    to_visit.append(link)
                    path.append((next, link))
        
        raise Exception("could not find path to end")
    

