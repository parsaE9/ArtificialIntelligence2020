from functions import *
from node import Node
import copy


# goal test is applied at node expansion
class IDS:

    frontier = []
    explored = []
    goal = None

    def __init__(self, initial_state, k, m, n):
        self.initial_state = initial_state
        self.count_columns = k
        self.count_color = m
        self.count_cards = n
        self.game_loop(initial_state)  # running the game

    def game_loop(self, initial_state):
        node = Node(copy.deepcopy(initial_state), None, "", 0)
        self.frontier.append(node)
        while not self.goal and self.frontier:
            # print("running")
            self.expand()

        if self.goal:
            success(self.goal, self.initial_state, len(self.frontier), len(self.explored))
        else:
            fail()
        return

    def expand(self):
        father = self.frontier.pop(0)
        self.explored.append(father)
        if goal_test(father.state):
            self.goal = father
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
                    if check_duplicate_state(new_state, self.frontier, self.explored):
                        # print("duplicate")
                        continue
                    new_node_depth = father.depth + 1
                    new_node_move = "put card " + lowest_card + " from column " + str(index_i + 1) + " on column " + str(index_j + 1)
                    new_node = Node(new_state, father, new_node_move, new_node_depth)
                    self.frontier.append(new_node)

