def filter_chars(s):
    return ''.join([c for c in s if not (5 <= s.index(c) <= 6 and 'G' <= c <= 'p')])