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