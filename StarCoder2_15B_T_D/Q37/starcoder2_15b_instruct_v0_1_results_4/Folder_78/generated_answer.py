def filter_chars(string):
    return ''.join([c for c in string if (string.index(c) < 75 or string.index(c) > 99) or (c < '8' or c > 'e')])