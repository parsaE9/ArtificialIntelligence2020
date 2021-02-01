class Word:
    def __init__(self, name, poet, count, real):
        self.name = name
        self.poet = poet
        self.count = count
        self.is_real = real
        self.unigram = None
        self.bigram = {}