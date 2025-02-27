def filter_chars(s):
    return ''.join([c for c in s if c < ']' or c > 't' or s.index(c) < 19 or (s.index(c) > 22)])