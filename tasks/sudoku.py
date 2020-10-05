class Cell:
    def __init__(self):
        self.val = None


class Boxes:
    def __init__(self, cells):
        self._cells = cells

    def __getitem__(self, item):
        if isinstance(item, int):
            return [[Cell() for x in range(order*order)] for y in range(order*order)]
        x, y = item
        return self._cells[x][y]


class SudokuBoard:
    def __init__(self, order):
        self.order = order
        self.row = None
        self.cols = None
        self._cells = [[Cell() for x in range(order*order)] for y in range(order*order)]
        self.boxes = Boxes(self._cells)

    def __getitem__(self, item):
        x, y = item
        return self._cells[x][y]

    def __iter__(self):
        for row in self._cells:
            for col in row:
                yield col


if __name__ == "__main__":
    board = SudokuBoard(order=3)
    print(board[3, 5].val)
    board[3, 5].val = 1
    print(board[3, 5].val)
    print(board.boxes[3])