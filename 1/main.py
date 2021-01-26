from functions import get_input, get_initial_depth
from p1 import BFS
from p2 import IDS
from p3 import A_STAR


if __name__ == "__main__":

    initial_state, algorithm = get_input()

    if algorithm == 1:
        BFS(initial_state)
    elif algorithm == 2:
        IDS(initial_state, get_initial_depth())
    else:
        A_STAR(initial_state)