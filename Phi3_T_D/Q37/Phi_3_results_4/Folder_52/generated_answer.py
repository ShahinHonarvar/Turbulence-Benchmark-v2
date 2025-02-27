def filter_chars(input_string):
    return ''.join([char for char in input_string if not (54 <= input_string.index(char) <= 83 and 'j' <= char <= 'v')])