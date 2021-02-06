import numpy
import sys


def shuffle_word(word):
    # check if word contains > 3 characters
    if sum([1 if c.isalpha() else 0 for c in word]) <= 3:
        return word
    # split word into 3 parts
    begin = ''
    end = ''
    while not word[len(word) - 1].isalpha():
        end = word[len(word) - 1] + end
        word = word[:len(word) - 1]
    while not word[0].isalpha():
        begin = begin + word[0]
        word = word[1:]

    end = word[len(word) - 1] + end
    word = word[:len(word) - 1]

    begin = begin + word[0]
    word = word[1:]
    var = list(word)
    if len(var) > 2:
        numpy.random.shuffle(var)
    return ''.join(list(begin) + var + list(end))


def shuffle_string(string):
    new_words = []
    for word in string.split():
        new_words.append(shuffle_word(word))
    return ' '.join(new_words)


print(shuffle_string(sys.argv[1]))