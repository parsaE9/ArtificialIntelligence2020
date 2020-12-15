class Node:

    def __init__(self, state, father, move, depth, heuristic=0):
        self.state = state
        self.father = father
        self.move = move
        self.depth = depth
        self.heuristic = heuristic
        self.cost = depth + heuristic