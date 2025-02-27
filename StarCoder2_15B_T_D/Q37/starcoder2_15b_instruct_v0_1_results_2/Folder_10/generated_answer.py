def filter_chars(s):
    filtered_chars = [c for c in s if c < 'E' or c > '~' or s.index(c) < 63 or (s.index(c) > 84)]
    return ''.join(filtered_chars)