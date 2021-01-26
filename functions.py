from grid import Grid


def get_input():
    input_ = input("- ENTER m n : ")
    m = int(input_.split(" ")[0])
    n = int(input_.split(" ")[1])

    input_ = input("- ENTER colors: ")
    colors = []
    for color in input_.split(' '):
        colors.append(color)

    rows = []
    print("- ENTER rows:")
    for i in range(0, n):
        row = input()
        rows.append(row)

    return m, n, colors, rows


def create_grids(inpt, colors, n):
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


def find_color_neighbors(row):
    for grid in row:
        c = grid.column
        r = grid.row
        for j in row:
            cc = j.column
            rr = j.row
            if rr == r + 1 and cc == c or rr == r - 1 and cc == c or rr == r and cc == c + 1 or rr == r and cc == c - 1:
                grid.neighbors.append(j)


def find_neighbors_color(neighbors):
    colors = []
    for neighbor in neighbors:
        if neighbor.color is not None:
            colors.append(neighbor.color)
    return colors


def find_color_degree(row):
    for grid in row:
        degree = 0
        if grid.color_degree is not None:
            grid.color_degree = 0
            continue
        for i in grid.neighbors:
            if i.color is None:
                degree += 1
        grid.color_degree = degree


def find_number_degree(row):
    for grid in row:
        r = grid.row
        c = grid.column
        degree = 0
        if grid.number_degree is not None:
            grid.number_degree = 0
            continue
        for i in row:
            if (i.column == c and i.row != r or i.column != c and i.row == r) and i.number is None:
                degree += 1
        grid.number_degree = degree


def find_number_neighbors(row):
    for grid in row:
        r = grid.row
        c = grid.column
        for i in row:
            if i.column == c and i.row != r or i.column != c and i.row == r:
                grid.number_neighbors.append(i)


def assign_value_to_colors(colors):
    value = len(colors)
    dic = {}
    for color in colors:
        dic[color] = value
        value -= 1
    return value