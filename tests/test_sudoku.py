import pytest
from tasks.sudoku import SudokuBoard


def test_sudoku_board():
    board = SudokuBoard(order=3)
    assert all(not cell for cell in board)
    board[3, 5].val = 1
    board.boxes[4][0, 2].fix()
    assert board.rows[3].cols[5].val == 1
    assert any(cell.fixed for cell in board.boxes[1, 1])
    with pytest.raises(board.FixedError):
        (board.cols[5] & board.rows[3]).val = 2
