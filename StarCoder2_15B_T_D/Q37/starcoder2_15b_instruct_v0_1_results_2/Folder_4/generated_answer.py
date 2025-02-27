def filter_chars(string):
    filtered = [c for c in string if c < 'S' or c > '{' or string.index(c) < 19 or (string.index(c) > 33)]
    return ''.join(filtered)