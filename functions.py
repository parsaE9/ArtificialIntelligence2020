def get_input():
    input_ = input("enter k m n : ")
    k = int(input_.split(" ")[0])
    m = int(input_.split(" ")[1])
    n = int(input_.split(" ")[2])

    arr = []

    for i in range(0, k):
        input_ = input("column {}: ".format(i + 1))
        arr.append(input_)

    # creating 2d array
    columns = []

    for i in range(len(arr)):
        col = []
        split_arr = arr[i].split(" ")
        for j in range(len(split_arr)):
            if split_arr[j] != '':
                col.append(split_arr[j])
        columns.append(col)

    return columns, k, m, n


def check_goal(state):
    for i in state:
        numbers = []
        colors = []
        # there is no problem if a column is empty or it's success when all columns are empty
        if not i:
            continue
        for j in i:
            number = int(j[0:len(j) - 1])
            numbers.append(number)
            color = j[len(j) - 1:]
            colors.append(color)
        # print(numbers)
        if numbers != sorted(numbers, reverse=True):
            return False
        if colors.count(colors[0]) != len(colors):
            return False
    return True


def find_lowest_card(column):
    lowest_card = column[len(column) - 1]
    card_number = int(lowest_card[:len(lowest_card) - 1])
    return card_number, lowest_card


def find_other_card_number(column):
    if not column:
        other_card_number = 99999
    else:
        other_lowest_card = column[len(column) - 1]
        other_card_number = int(other_lowest_card[:len(other_lowest_card) - 1])
    return other_card_number

