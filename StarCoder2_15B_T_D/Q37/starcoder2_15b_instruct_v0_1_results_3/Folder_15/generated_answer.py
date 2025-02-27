def filter_chars(s):
    return ''.join((c for c in s if c < '?' or c > 'f' or s.index(c) < 2 or (s.index(c) > 6)))