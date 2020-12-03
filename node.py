class Node:

    def __init__(self, state, father, move, depth):
        self.state = state
        self.father = father
        self.move = move
        self.depth = depth