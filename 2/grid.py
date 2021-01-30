from functions import *


class Grid:
    def __init__(self, color, number, row, column, possible_colors, possible_numbers, color_degree, number_degree):
        self.color = color
        self.number = number
        self.row = row
        self.column = column
        self.color_value = None
        self.possible_colors = possible_colors
        self.possible_numbers = possible_numbers
        self.possible_moves = []
        self.neighbors = []
        self.number_neighbors = []
        self.color_degree = color_degree
        self.number_degree = number_degree

        if self.number is not None:
            self.number = int(self.number)

    def adjust_possible_moves(self):
        self.possible_moves = possible_actions(self.number, self.possible_numbers, self.color, self.possible_colors)