import string

filename = 'meiguice.txt'

with open(filename) as file:
    punctuation = string.punctuation

    words_list = file.read().lower()

    table = words_list.maketrans('', '', punctuation)
    words_list = words_list.translate(table).split()

    print(words_list)

