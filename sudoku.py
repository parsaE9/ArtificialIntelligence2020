from node import Node
from functions import *
import copy


class Sudoku:

    def __init__(self, m, n, colors, rows):
        self.m = m
        self.n = n
        self.colors = colors
        self.colors_value = assign_value_to_colors(colors)
        self.grids = create_grids(rows, colors, n)
        self.adjust_possible_colors_and_numbers()
        self.node = Node(copy.deepcopy(self.grids), None)

        for i in self.grids:
            print(i)

    def adjust_possible_colors_and_numbers(self):
        for grid in self.grids:
            if grid.color is None:
                neighbor_colors = find_neighbors_color(grid.neighbors)
                grid.possible_colors = list(set(grid.possible_colors) ^ set(neighbor_colors))
                grid.color_value = 0
            else:
                grid.color_value = self.colors_value[grid.color]

            if grid.number is None:
                illegal_numbers = self.find_illegal_numbers(grid)
                grid.possible_numbers = list(set(grid.possible_numbers) ^ set(illegal_numbers))


    def find_illegal_numbers(self, grid):
        r = grid.row
        c = grid.column
        illegal_numbers = []
        for i in self.grids:
            if (i.column == c and i.row != r or i.column != c and i.row == r) and i.number is not None:
                illegal_numbers.append(i.number)
        return illegal_numbers

    def goal_test(self):
        for grid in self.grids:
            if grid.number is None or grid.color is None:
                return False

        for grid in self.grids:
            number = grid.number
            neighbors_number = []
            for i in grid.number_neighbors:
                neighbors_number.append(i.number)
            if number in neighbors_number:
                return False

