class BFS:

    def __init__(self, columns, k, m, n):
        self.columns = columns
        self.count_columns = k
        self.count_color = m
        self.count_cards = n
        self.goalFound = False
        self.frontier = []  # frontier list
        self.explored = []  # explored list
        print(columns)
        self.game_initial_state()  # running the game

    def game_initial_state(self):
        self.frontier.append(self.columns)
        if self.check_goal(self.columns):
            print("SUCCESS")
            return
        self.game_loop()

    def game_loop(self):
        while not self.goalFound and self.frontier:
            self.expand()

        print("FAIL!")
        return

    def check_goal(self, state):
        for i in state:
            numbers = []
            colors = []
            # there is no problem if a column is empty or it's success when all columns are empty
            if not i:
                continue
            for j in i:
                number = int(j[0:len(j) - 1])
                numbers.append(number)
                color = j[len(j) - 1:]
                colors.append(color)
            print(numbers)
            if numbers != sorted(numbers, reverse=True):
                return False
            if colors.count(colors[0]) != len(colors):
                return False
        self.goalFound = True
        return True

    def expand(self):
        state = self.frontier.pop(0)
        self.explored.append(state)
