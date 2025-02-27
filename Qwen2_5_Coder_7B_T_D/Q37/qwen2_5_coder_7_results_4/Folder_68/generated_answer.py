def filter_chars(s):
    return ''.join([c for c in s if not (7 <= s.index(c) <= 9 and '6' <= c <= 'w')])