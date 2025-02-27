def filter_chars(string):
    filtered_chars = [c for c in string if c < '?' or c > 'f' or string.index(c) < 2 or (string.index(c) > 6)]
    return ''.join(filtered_chars)