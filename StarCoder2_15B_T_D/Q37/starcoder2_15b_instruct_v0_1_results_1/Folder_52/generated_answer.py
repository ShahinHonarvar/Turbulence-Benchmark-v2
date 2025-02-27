def filter_chars(string):
    filtered = [c for c in string if c < 'j' or c > 'v' or string.index(c) < 54 or (string.index(c) > 83)]
    return ''.join(filtered)