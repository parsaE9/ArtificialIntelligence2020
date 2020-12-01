from functions import get_input
from p1 import BFS
from p2 import IDS
# from p2 import A_STAR


if __name__ == "__main__":
    columns, k, m, n = get_input()

    BFS(columns, k, m, n)
    # IDS(columns, k, m, n)
    # A_STAR(columns, k, m, n)

