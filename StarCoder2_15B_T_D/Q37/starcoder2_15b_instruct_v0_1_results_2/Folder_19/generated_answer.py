def filter_chars(s):
    filtered = [c for c in s if c < 'E' or c > 't' or s.index(c) < 35 or (s.index(c) > 89)]
    return ''.join(filtered)