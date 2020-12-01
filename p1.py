from functions import *
import copy


class BFS:

    def __init__(self, columns, k, m, n):
        self.count_columns = k
        self.count_color = m
        self.count_cards = n
        self.goalFound = False
        self.frontier = []  # frontier list
        self.explored = []  # explored list
        print(columns)
        self.game_loop(columns)  # running the game

    def game_loop(self, initial_state):
        self.frontier.append(copy.deepcopy(initial_state))
        check_goal(initial_state)
        while not self.goalFound and self.frontier:
            self.expand()

        if self.goalFound:
            print("SUCCESS")
            print(self.frontier[len(self.frontier) - 1])
        else:
            print("FAIL!")
        return

    def expand(self):
        state = copy.deepcopy(self.frontier.pop(0))
        self.explored.append(copy.deepcopy(state))
        for i in state:
            # print("expand")
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
                    if self.explored.__contains__(new_state) or self.frontier.__contains__(new_state):
                        print("tekrari")
                        continue
                    self.frontier.append(copy.deepcopy(new_state))
                    if check_goal(new_state):
                        self.goalFound = True
                        return

