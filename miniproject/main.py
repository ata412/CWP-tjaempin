"""Entry point for the Rush00 checkmate project."""

import sys

from checkmate import checkmate


DEFAULT_BOARD = """\
R...
.K..
..P.
...."""


def main():
    """Check the demo board, or every board file passed on the command line."""
    if len(sys.argv) == 1:
        checkmate(DEFAULT_BOARD)
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, "r", encoding="utf-8") as board_file:
                checkmate(board_file.read())
        except (OSError, UnicodeError):
            print("Error")


if __name__ == "__main__":
    main()
