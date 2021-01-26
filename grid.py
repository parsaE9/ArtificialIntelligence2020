class Grid:
    def __init__(self, color, number, row, column, possible_colors, possible_numbers, color_degree, number_degree):
        self.color = color
        self.number = number
        self.row = row
        self.column = column
        self.possible_colors = possible_colors
        self.possible_numbers = possible_numbers
        self.neighbors = []
        self.number_neighbors = []
        self.color_degree = color_degree
        self.number_degree = number_degree
        self.color_value = None

        if self.number is not None:
            self.number = int(self.number)