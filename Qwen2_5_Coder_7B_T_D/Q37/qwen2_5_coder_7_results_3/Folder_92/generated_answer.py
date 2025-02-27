def filter_chars(s):
    return ''.join([c for c in s if not (4 <= s.index(c) <= 4 and '7' <= c <= 'o')])