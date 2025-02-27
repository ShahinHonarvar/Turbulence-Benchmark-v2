def filter_chars(input_string):
    to_remove = set()
    for i in range(124, 855):
        if '9' <= input_string[i] <= 's':
            to_remove.add(input_string[i])
    result = ''.join((c for c in input_string if c not in to_remove))
    return result