def get_input():
    algorithm = input("press 1 for BFS or 2 for IDS or 3 for A_STAR: ")
    input_ = input("- ENTER k m n : ")
    k = int(input_.split(" ")[0])
    m = int(input_.split(" ")[1])
    n = int(input_.split(" ")[2])

    arr = []

    for i in range(0, k):
        input_ = input("- COLUMN {}: ".format(i + 1))
        if input_.__contains__('#'):
            input_ = ''
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

    return columns, int(algorithm)


def get_initial_depth():
    depth = input('- enter initial depth or press enter to skip and default depth is 0: ')
    if depth != '':
        return int(depth)
    return 0


def goal_test(state):
    for i in state:
        numbers = []
        colors = []
        # there is no problem if a column is empty. it's success when all columns are empty
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


def check_duplicate_state(new_state, frontier, explored):
    for node in frontier:
        if new_state == node.state:
            return True
    for node in explored:
        if new_state == node.state:
            return True
    return False


def success(goal, initial_state, count_frontier, count_explored):
    moves = [goal.move]
    previous_node = goal.father
    if previous_node:
        while previous_node.move:
            moves.append(previous_node.move)
            previous_node = previous_node.father
    moves.reverse()
    print("#############################################################")
    print("#############################################################")
    print("- SUCCESS!")
    print("- initial state : {}".format(initial_state))
    print("- Goal state : {}".format(goal.state))
    print("- Goal depth : {}".format(goal.depth))
    print("- number of expanded nodes : {}".format(count_explored))
    print("- number of generated nodes (expanded + generated) : {}".format(count_frontier + count_explored))
    print("- number of generated nodes (not yet expanded) : {}".format(count_frontier))
    print("- actions in each step:")
    step = 1
    for move in moves:
        print("\t- step {} : {}".format(step, move))
        step += 1
    exit()


def fail():
    print("#############################################################")
    print("#############################################################")
    print("- FAIL!")
    exit()
