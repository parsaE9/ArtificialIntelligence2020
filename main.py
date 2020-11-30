from functions import get_input
from p1 import BFS


if __name__ == "__main__":
    columns, k, m, n = get_input()

    BFS(columns, k, m, n)
    # DFS(columns, k, m, n)
    # A_STAR(columns, k, m, n)


