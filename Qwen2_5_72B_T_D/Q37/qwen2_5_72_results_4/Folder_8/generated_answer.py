def filter_chars(input_string):
    to_remove = set()
    for i in range(41, 87):
        if 'S' <= input_string[i] <= 's':
            to_remove.add(input_string[i])
    result = ''.join([char for char in input_string if char not in to_remove])
    return result