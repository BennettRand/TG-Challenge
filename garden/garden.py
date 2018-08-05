import logging

logger = logging.getLogger(__name__)


class Garden(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = []

        for _ in range(self.h):
            self.cells.append([None] * w)

    @classmethod
    def from_matrix(cls, matrix):
        """
        Initializes the Garden from the NxM matrix.
        assumes the matrix is not empty and every row is the same length.
        """
        h = len(matrix)
        w = len(matrix[0])

        garden = cls(w, h)

        logger.debug(garden.cells)

        for y, row in enumerate(matrix):
            for x, carrots in enumerate(row):
                logger.debug('%s carrots in %s, %s', carrots, x, y)
                garden.cells[y][x] = Cell(carrots, garden, (x, y))

        return garden

    @property
    def center(self):
        cyl = (len(self.cells) - 1) / 2
        cxl = (len(self.cells[0]) - 1) / 2
        cyu = len(self.cells) / 2 + 1
        cxu = len(self.cells[0]) / 2 + 1

        candidates = []

        for r in self.cells[cyl:cyu]:
            candidates += r[cxl:cxu]

        center = max(candidates, key=lambda c: c.carrots)

        return center


class Cell(object):
    def __init__(self, carrots, garden, loc):
        self.carrots = carrots  # number of carrots
        self.garden = garden  # reference to parent garden obj
        self.loc = loc  # (x, y) tuple of position in garden

    @property
    def left(self):
        x, y = (self.loc[0] - 1, self.loc[1])

        if x < 0:
            return None

        return self.garden.cells[y][x]

    @property
    def right(self):
        x, y = (self.loc[0] + 1, self.loc[1])

        if x >= self.garden.w:
            return None

        return self.garden.cells[y][x]

    @property
    def up(self):
        x, y = (self.loc[0], self.loc[1] - 1)

        if y < 0:
            return None

        return self.garden.cells[y][x]

    @property
    def down(self):
        x, y = (self.loc[0], self.loc[1] + 1)

        if y >= self.garden.h:
            return None

        return self.garden.cells[y][x]
