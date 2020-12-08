from functions import *
from node import Node
import copy


# goal test is applied at node expansion
class IDS:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.initial_depth = 0  # initial depth of IDS
        self.explored = []
        self.goal = None
        self.parent_states = 0
        self.ids()

    def ids(self):
        while True:
            initial_node = self.restart()
            self.dls(self.initial_depth, initial_node)
            self.initial_depth += 1

    # TODO: how to handle failure?
    def restart(self):
        self.explored.clear()
        initial_node = Node(copy.deepcopy(self.initial_state), None, "", 0)
        return initial_node

    def dls(self, limit, father):
        self.explored.append(father)
        if goal_test(father.state):
            self.goal = father
            # TODO: duplicate parent states count
            success(self.goal, self.initial_state, 0, len(self.explored))
        if father.depth == limit:
            return

        state = copy.deepcopy(father.state)
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
                    if new_state == father.state:
                        self.parent_states += 1
                        # print("duplicate")
                        continue
                    new_node_depth = father.depth + 1
                    new_node_move = "put card " + lowest_card + " from column " + str(index_i + 1) + " on column " + str(index_j + 1)
                    new_node = Node(new_state, father, new_node_move, new_node_depth)
                    self.dls(limit, new_node)
