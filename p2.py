from functions import *
from node import Node
import copy


# goal test is applied at node expansion
class IDS:

    def __init__(self, initial_state, initial_depth):
        self.initial_state = initial_state
        self.initial_depth = initial_depth  # initial depth of IDS
        self.count_generated_nodes = 0
        self.goal = None
        self.ids()

    def ids(self):
        while True:
            print(self.initial_depth)
            initial_node = self.restart()
            self.dls(self.initial_depth, initial_node)
            self.initial_depth += 1

    # TODO: how to handle failure?

    def dls(self, limit, node):
        if goal_test(node.state):
            self.goal = node
            success(self.goal, self.initial_state, 0, self.count_generated_nodes)
        if node.depth == limit:
            return
        state = copy.deepcopy(node.state)
        for i in state:
            if not i:
                continue
            index_i = state.index(i)
            card_number, lowest_card = find_lowest_card(i)
            for j in state:
                other_card_number = find_other_card_number(j)
                if card_number < other_card_number:
                    new_state = copy.deepcopy(state)
                    index_j = new_state.index(j)
                    new_state[index_j].append(lowest_card)
                    new_state[index_i].pop()
                    new_node_depth = node.depth + 1
                    new_node_move = "put card " + lowest_card + " from column " + str(index_i + 1) + " on column " + str(index_j + 1)
                    new_node = Node(new_state, node, new_node_move, new_node_depth)
                    self.count_generated_nodes += 1
                    self.dls(limit, new_node)

    def restart(self):
        self.count_generated_nodes = 0
        initial_node = Node(copy.deepcopy(self.initial_state), None, "", 0)
        return initial_node
