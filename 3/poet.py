from functions import *


class Poet:
    def __init__(self, train_set, poet, h3, h2, h1, e):
        self.poet = poet
        self.words = create_dictionary(train_set, poet)
        self.backoff = calculate_backoff(self.words, h3, h2, h1, e)
        print(len(self.words))
        for word in self.words:
            a = self.words[word]