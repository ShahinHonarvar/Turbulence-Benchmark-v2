def filter_chars(s):
    return ''.join((c for c in s if c < 'i' or c > 'k' or s.index(c) < 20 or (s.index(c) > 62)))