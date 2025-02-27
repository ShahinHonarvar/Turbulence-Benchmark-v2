def filter_chars(s):
    return ''.join([c for c in s if not (33 <= s.index(c) <= 70 and '7' <= c <= 'k')])