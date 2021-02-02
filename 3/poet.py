from functions import *


class Poet:
    def __init__(self, train_set, poet):
        self.poet = poet
        self.words = create_dictionary(train_set, poet)