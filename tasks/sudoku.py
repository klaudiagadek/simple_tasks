class Cell:
    def __init__(self):
        self.fixed = False
        self._val = None

    def fix(self):
        self.fixed = True

    def __bool__(self):
        return self.fixed

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        if self.fixed:
            raise SudokuBoard.FixedError
        self._val = value

    def __repr__(self):
        return str(self._val)


class BoardSlice:
    def __init__(self, table, order, xb, yb):
        self.order = order
        self._cells = table
        self.x_box = xb
        self.y_box = yb

    def __getitem__(self, item):
        x, y = item
        return self._cells[self.order*(self.y_box+1)-1 - y][x+self.x_box*self.order]

    def __iter__(self):
        for i in range(3):
            for j in range(3):
                yield self._cells[self.order*(self.y_box+1)-1 - i][j+self.x_box*self.order]


class Box:
    def __init__(self, table, order):
        self.order = order
        self._cells = table

    def __getitem__(self, item):
        if isinstance(item, int):
            x = item % 3
            y = 2 - int(item/3)
        else:
            x, y = item
        return BoardSlice(self._cells, self.order, x, y)


class SudokuBoard:
    class FixedError(Exception):
        """Modifying cell which is fixed"""

    def __init__(self, order):
        self.order = order
        self.size = order**2
        self._cells = [[Cell() for _ in range(self.size)] for y in range(self.size)]

    def __getitem__(self, item):
        x, y = item
        return self._cells[self.size-y-1][x]

    def __iter__(self):
        for row in self._cells:
            for col in row:
                yield col

    def __repr__(self):
        return "\n".join([str(x) for x in self._cells])

    @property
    def boxes(self):
        return Box(self._cells, self.order)


if __name__ == "__main__":
    board = SudokuBoard(order=3)
    print(board)
    board[3, 5].val = 1
    board[3, 5].fix()
    print(board.boxes[4][0, 2])
    for x in board.boxes[4]:
        print(x)
    print(board)
    # print(board[3, 5])
    # print(board[3, 5].val)
    # print(board.boxes[3])
