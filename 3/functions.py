from word import Word
import re


def create_dictionary(address, poet):
    f = open(address)
    contents = ('# ' + re.sub('\n', ' $ # ', f.read()) + ' $').split(' ')
    f.close()
    # ff = open('test.txt', 'w')
    # for i in contents:
    #     ff.write(i + ' ')
    # ff.close()
    # print(contents)
    # print(len(contents))

    words = {}
    previous_word = '$'
    words['#'] = Word('#', poet, 0, False)
    words['$'] = Word('$', poet, 0, False)

    for word in contents:
        if word in words.keys():
            words[word].count += 1
        else:
            words[word] = Word(word, poet, 1, True)

        if previous_word in words[word].bigram.keys():
            words[word].bigram[previous_word] += 1
        else:
            words[word].bigram[previous_word] = 1
        previous_word = word

    delete = [word for word in words if words[word].count < 3]
    for key in delete:
        del words[key]
    for word in words:
        for key in delete:
            if key in words[word].bigram.keys():
                del words[word].bigram[key]

    unigram(words)
    bigram(words)
    return words


def unigram(words):
    words_count = 0
    for word in words:
        words_count += words[word].count
    words_count -= words['$'].count
    words_count -= words['#'].count
    for word in words:
        words[word].unigram = words[word].count / words_count


def bigram(words):
    for word in words:
        for i in words[word].bigram:
            words[word].bigram[i] /= words[word].count


def calculate_backoff(words, h3, h2, h1, e):
    backoff = {}
    for word in words:
        value = h2 * words[word].unigram + h1 * e
        for condition in words[word].bigram:
            backoff[word + '|' + condition] = value + h3 * words[word].bigram[condition]
    return backoff