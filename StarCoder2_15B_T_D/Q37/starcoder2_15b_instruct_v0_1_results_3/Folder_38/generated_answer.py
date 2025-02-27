def filter_chars(s):
    return ''.join((c for c in s if c < 'a' or c > 'f' or s.index(c) < 24 or (s.index(c) > 79)))