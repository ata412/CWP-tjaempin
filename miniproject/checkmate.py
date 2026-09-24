"""Utilities for checking whether a king is attacked on a chessboard."""


PIECES = {"K", "P", "B", "R", "Q"}


def _parse_board(board):
    """Return a square board as a list of rows, or None if it is invalid."""
    if not isinstance(board, str):
        return None

    rows = board.splitlines()
    if not rows or not rows[0]:
        return None

    size = len(rows)
    if any(len(row) != size for row in rows):
        return None

    if sum(row.count("K") for row in rows) != 1:
        return None

    return rows


def _first_piece(rows, row, column, row_step, column_step):
    """Find the first chess piece in a direction from a square."""
    size = len(rows)
    row += row_step
    column += column_step

    while 0 <= row < size and 0 <= column < size:
        piece = rows[row][column]
        if piece in PIECES:
            return piece
        row += row_step
        column += column_step

    return None


def _is_attacked_by_pawn(rows, king_row, king_column):
    """Pawns attack diagonally upward, as shown in the subject diagram."""
    pawn_row = king_row + 1
    for pawn_column in (king_column - 1, king_column + 1):
        if 0 <= pawn_row < len(rows) and 0 <= pawn_column < len(rows):
            if rows[pawn_row][pawn_column] == "P":
                return True
    return False


def is_in_check(board):
    """Return True when the board is valid and its king is under attack."""
    rows = _parse_board(board)
    if rows is None:
        return None

    king_row = next(row_index for row_index, row in enumerate(rows) if "K" in row)
    king_column = rows[king_row].index("K")

    if _is_attacked_by_pawn(rows, king_row, king_column):
        return True

    diagonal_directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    for row_step, column_step in diagonal_directions:
        if _first_piece(rows, king_row, king_column, row_step, column_step) in {"B", "Q"}:
            return True

    straight_directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for row_step, column_step in straight_directions:
        if _first_piece(rows, king_row, king_column, row_step, column_step) in {"R", "Q"}:
            return True

    return False


def checkmate(board):
    """Print the result required by Rush00 and return it as a boolean.

    Invalid boards print ``Error`` and return None.
    """
    result = is_in_check(board)
    if result is None:
        print("Error")
        return None

    print("Success" if result else "Fail")
    return result
