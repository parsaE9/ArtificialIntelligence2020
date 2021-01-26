from functions import *
from sudoku import Sudoku

if __name__ == "__main__":

    m, n, colors, rows = get_input()
    Sudoku(m, n, colors, rows)