def filter_chars(s):
    return ''.join([c for c in s if c < 'D' or c > 'u' or s.index(c) < 227 or (s.index(c) > 235)])