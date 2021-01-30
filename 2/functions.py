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
        if grid.color is not None:
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
        if grid.number is not None:
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
    return dic


def possible_actions(number, numbers, color, colors):
    if number is None and color is None:
        return calculate_possible_actions(numbers, colors)
    elif number is None and color is not None:
        return calculate_possible_actions(numbers, [color])
    elif number is not None and color is None:
        return calculate_possible_actions([number], colors)
    else:
        return []


def calculate_possible_actions(numbers, colors):
    actions = []
    for i in numbers:
        for j in colors:
            actions.append(str(i) + j)
    return actions


def calculate_possible_values(arr1, arr2):
    arr = []
    for i in arr1:
        if i not in arr2:
            arr.append(i)
    return arr


def print_result(result, grids=None, n=0):
    if result == 'fail':
        print("\n\nfail!")
        quit()
    print('\n\nsuccess\n\n')
    i = 1
    for grid in grids:
        print(str(grid.number) + grid.color, end="")
        if i % n:
            print(" | ", end="")
        else:
            print()
        i += 1