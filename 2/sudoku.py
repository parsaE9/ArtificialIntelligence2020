from node import Node
from grid import Grid
from functions import *
import copy


class Sudoku:

    def __init__(self, m, n, colors, rows):
        self.m = m
        self.n = n
        self.colors = colors
        self.colors_value = assign_value_to_colors(colors)
        self.grids = self.create_grids(rows, colors, n)
        self.father_node = None
        self.current_grid = None
        self.program_loop()

    def program_loop(self):
        self.adjust_possible_colors_and_numbers()
        self.father_node = Node(self.grids, None)
        while self.game_check():
            mrv_grid = self.MRV_check()
            self.current_grid = self.degree_check(mrv_grid)
            self.select_action_and_forward_check()

    def select_action_and_forward_check(self):
        action = self.current_grid.possible_moves.pop()
        self.father_node = Node(copy.deepcopy(self.grids), self.father_node)
        color = action[len(action) - 1]
        number = int(action[:len(action) - 1])
        self.current_grid.number = number
        self.current_grid.color = color
        self.current_grid.possible_moves = []
        self.current_grid.possible_colors = None
        self.current_grid.possible_numbers = None
        self.current_grid.color_value = self.colors_value[color]
        self.adjust_possible_colors_and_numbers()
        find_number_degree(self.grids)
        find_color_degree(self.grids)

    def adjust_possible_colors_and_numbers(self):
        for grid in self.grids:
            if grid.color is None:
                neighbor_colors = find_neighbors_color(grid.neighbors)
                grid.possible_colors = calculate_possible_values(grid.possible_colors, neighbor_colors)
                grid.color_value = 0
            else:
                grid.color_value = self.colors_value[grid.color]
            if grid.number is None:
                illegal_numbers = self.find_illegal_numbers(grid)
                grid.possible_numbers = calculate_possible_values(grid.possible_numbers, illegal_numbers)
            grid.adjust_possible_moves()

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

        # for grid in self.grids:
        #     number = grid.number
        #     neighbors_number = []
        #     for i in grid.number_neighbors:
        #         neighbors_number.append(i.number)
        #     if number in neighbors_number:
        #         return False

        for grid in self.grids:
            color_value = grid.color_value
            number = grid.number
            for neighbor in grid.neighbors:
                if number > neighbor.number and color_value <= neighbor.color_value:
                    return False
                if number < neighbor.number and color_value >= neighbor.color_value:
                    return False

        return True

    def create_grids(self, inpt, colors, n):
        row = []
        numbers = []
        for i in range(0, n):
            numbers.append(int(i) + 1)
        numbers.reverse()
        counter_row = 0
        for i in inpt:
            grid = i.split(' ')
            counter_column = 0
            for j in grid:
                possible_colors = []
                possible_numbers = []
                color_degree = 0
                number_degree = 0
                color = j[len(j) - 1]
                number = j[:len(j) - 1]
                if color == '#':
                    color = None
                    possible_colors = colors
                    color_degree = None
                if number == '*':
                    number = None
                    possible_numbers = numbers
                    number_degree = None
                row.append(Grid(color, number, counter_row, counter_column, possible_colors, possible_numbers,
                                color_degree, number_degree))
                counter_column += 1
            counter_row += 1
        find_color_neighbors(row)
        find_number_neighbors(row)
        find_color_degree(row)
        find_number_degree(row)
        return row

    def game_check(self):
        if self.goal_test():
            print_result('success', self.grids, self.n)
            quit()
        self.back_track_check()
        return True

    def back_track_check(self, recursive=False):
        flag = True
        for grid in self.grids:
            if len(grid.possible_moves) == 0 and (grid.number is None or grid.color is None):
                flag = False
                break
        if self.current_grid is not None and recursive is False:
            for grid in self.current_grid.neighbors:
                if grid.number is not None:
                    if self.current_grid.color_value > grid.color_value and self.current_grid.number < grid.number:
                        flag = False
                        break
                    if self.current_grid.color_value < grid.color_value and self.current_grid.number > grid.number:
                        flag = False
                        break
        if not flag and self.father_node.father is None:
            print_result('fail')
            quit()
        elif not flag:
            self.back_track()

    def back_track(self):
        self.grids = copy.deepcopy(self.father_node.state)
        self.father_node = self.father_node.father
        self.back_track_check(recursive=True)

    def MRV_check(self):
        grids = []
        minn = 9999999
        for grid in self.grids:
            if grid.number is not None and grid.color is not None:
                continue
            if len(grid.possible_moves) == minn:
                grids.append(grid)
            if len(grid.possible_moves) < minn:
                minn = len(grid.possible_moves)
                grids.clear()
                grids.append(grid)
        return grids

    def degree_check(self, grids):
        if len(grids) == 1:
            return grids[0]
        maxx = -1
        selected_grid = None
        for grid in grids:
            if grid.number_degree + grid.color_degree > maxx:
                maxx = grid.number_degree + grid.color_degree
                selected_grid = grid
        return selected_grid