from word import Word
import re
import random


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
    words['#'] = Word('#', poet, 0)
    words['$'] = Word('$', poet, 0)

    for word in contents:
        if word in words.keys():
            words[word].count += 1
        else:
            words[word] = Word(word, poet, 1)

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


def calculate_backoff(word, previous, poet, h3, h2, h1, e):
    backoff = h1 * e
    if word in poet.words:
        backoff += h2 * poet.words[word].unigram
        if previous in poet.words[word].bigram:
            backoff += h3 * poet.words[word].bigram[previous]
    return backoff


def predict_poet(hemistich, h3, h2, h1, e, poet1, poet2, poet3):
    words = hemistich.split(' ')
    previous = '#'
    backoff = [1, 1, 1]
    words.pop(0)
    for word in words:
        backoff[0] *= calculate_backoff(word, previous, poet1, h3, h2, h1, e)
        backoff[1] *= calculate_backoff(word, previous, poet2, h3, h2, h1, e)
        backoff[2] *= calculate_backoff(word, previous, poet3, h3, h2, h1, e)
        previous = word

    poet = max(backoff)
    if poet == backoff[0]:
        return 1
    elif poet == backoff[1]:
        return 2
    else:
        return 3


def verify_test_set(h3, h2, h1, e, poet1, poet2, poet3, test_set_address):
    total_lines = 0
    correct_predictions = 0
    file = open(test_set_address)
    for line in file:
        total_lines += 1
        line = line.replace('\n', '')
        real_poet = int(line[0:1])
        hemistich = '# ' + line[2:] + ' $'
        predicted_poet = predict_poet(hemistich, h3, h2, h1, e, poet1, poet2, poet3)
        if predicted_poet == real_poet:
            correct_predictions += 1
    file.close()

    precision = str(100 * correct_predictions / total_lines) + ' %'
    print('precision : ', precision)