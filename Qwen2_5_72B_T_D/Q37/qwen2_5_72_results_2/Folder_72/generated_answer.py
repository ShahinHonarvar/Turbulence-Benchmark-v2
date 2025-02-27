def filter_chars(input_string):
    to_remove = set()
    for i in range(35, 52):
        if 'H' <= input_string[i] <= 's':
            to_remove.add(input_string[i])
    result = ''.join((ch for ch in input_string if ch not in to_remove))
    return result