def filter_chars(input_string):
    if len(input_string) < 488 or len(input_string) > 992:
        raise ValueError('Input string must be at least 488 characters long and must not exceed 992 characters.')
    to_remove = set()
    for i in range(502, 946):
        char = input_string[i]
        if 'W' < char < 'y':
            to_remove.add(char)
    return ''.join((c for c in input_string if c not in to_remove))