# I need it later to count occurance of a string in the list
from collections import Counter

def count_words(first_file_name, second_file_name, text):
    with open(first_file_name, 'w') as first_file:
        for i in range(20):
            first_file.write('Be careful not to count a word and a non word character such as a comma as one word (e.g. “Hello, World!” should count 2 words total, one “Hello” and one “World”)\n')

    # Read through file and create a string from just one line, the file has 20 identical lines
    some_string = []
    row_count = 0
    with open(first_file_name) as first_file:
        for line in first_file:
            some_string = str(line.split(' '))
            row_count += 1

    # Transform the string into a clean list
    bad_strings = ',.""“”!()\\'
    some_string = ''.join(c for c in some_string if c not in bad_strings)
    some_string = some_string.split(' ')
    some_list = []
    for elem in some_string:
        some_list.append(elem[1:-1])

    for elem in some_list:
        if some_list.index(elem) == len(some_list) - 1:
            exchange = elem[:-2]
            some_list.remove(elem)
            some_list.append(exchange)

    # Count how many time a word is repeated per line and then per file (*20)
    times = Counter(some_list)
    some_dict = {}
    total_words = 0
    for elem in some_list:
        some_dict[elem] = times[elem] * row_count
        total_words += times[elem]

    #Printing the result
    with open(second_file_name, 'w') as second_file:
        second_file.write(f'\t\tThe total number of words is {total_words}')
        for val, key in enumerate(some_dict):
            second_file.write(f'{key} is repeated {val} times\n')

count_words('sample_text.txt', 'fisierul_final.txt','Be careful not to count a word and a non word character such as a comma as one word (e.g. “Hello, World!” should count 2 words total, one “Hello” and one “World”)\n')