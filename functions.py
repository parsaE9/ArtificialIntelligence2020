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
            color = j[len(j) - 1]
            number = j[:len(j) - 1]
            if color == '#':
                color = None
                possible_colors = colors
            if number == '*':
                number = None
                possible_numbers = numbers
            row.append(Grid(color, number, counter_row, counter_column, possible_colors, possible_numbers))
            counter_column += 1
        counter_row += 1

    find_neighbors(row)
    return row


def find_neighbors(row):
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