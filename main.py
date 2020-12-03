from functions import get_input
from p1 import BFS
from p2 import IDS
import copy


if __name__ == "__main__":
    initial_state, k, m, n = get_input()

    # BFS(initial_state, k, m, n)
    IDS(initial_state, k, m, n)
    # A_STAR(initial_state, k, m, n)