def filter_chars(string):
    filtered = [c for c in string if c < 'O' or c > 'd' or string.index(c) < 28 or (string.index(c) > 65)]
    return ''.join(filtered)