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
        self.game_initial_state(columns)  # running the game

    def game_initial_state(self, state):
        self.frontier.append(copy.deepcopy(state))
        if check_goal(state):
            print("SUCCESS")
            return
        self.game_loop()

    def game_loop(self):
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
                    if self.explored.__contains__(new_state):
                        continue
                    self.frontier.append(new_state)
                    if check_goal(new_state):
                        self.goalFound = True
                        return
