def filter_chars(input_string):
    to_remove = set((char for char in input_string[46:91] if 'D' < char < 'H'))
    return ''.join((char for char in input_string if char not in to_remove))