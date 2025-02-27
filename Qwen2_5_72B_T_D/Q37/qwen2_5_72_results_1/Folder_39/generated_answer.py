def filter_chars(input_string):
    to_remove = set()
    for i in range(52, 82):
        if 'A' <= input_string[i] <= 'U':
            to_remove.add(input_string[i])
    result = ''.join((c for c in input_string if c not in to_remove))
    return result