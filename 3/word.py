class Word:
    def __init__(self, name, poet, count):
        self.name = name
        self.poet = poet
        self.count = count
        self.unigram = None
        self.bigram = {}