from functions import *
from node import Node
import copy


class BFS:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.frontier = []
        self.explored = []
        self.goal = None
        self.program_loop(initial_state)

    def program_loop(self, initial_state):
        node = Node(copy.deepcopy(initial_state), None, "", 0)
        self.frontier.append(node)
        if goal_test(node.state):
            self.goal = node
        while not self.goal and self.frontier:
            self.expand()
        if self.goal:
            success(self.goal, self.initial_state, len(self.frontier), len(self.explored))
        else:
            fail()

    def expand(self):
        father = self.frontier.pop(0)
        self.explored.append(father)
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
                    if check_duplicate_state(new_state, self.frontier, self.explored):
                        # print("duplicate")
                        continue
                    new_node_depth = father.depth + 1
                    new_node_move = "put card " + lowest_card + " from column " + str(index_i + 1) + " on column " + str(index_j + 1)
                    new_node = Node(new_state, father, new_node_move, new_node_depth)
                    self.frontier.append(new_node)
                    if goal_test(new_node.state):
                        self.goal = new_node
                        return
