def filter_chars(input_string):
    to_remove = set()
    for i in range(55, 66):
        if 'f' < input_string[i] < '|':
            to_remove.add(input_string[i])
    result = ''.join([char for char in input_string if char not in to_remove])
    return result