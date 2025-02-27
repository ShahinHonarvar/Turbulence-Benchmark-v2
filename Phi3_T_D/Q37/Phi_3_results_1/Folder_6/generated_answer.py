def filter_chars(s):
    filtered_string = ''.join((char for index, char in enumerate(s) if index < 13 or index > 28 or (not 'c' <= char <= 'n')))
    return filtered_string