def filter_chars(string):
    return ''.join((c for c in string if c < 'L' or c > 'a' or string.index(c) < 1 or (string.index(c) > 7)))