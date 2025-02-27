def filter_chars(s):
    return ''.join([c for c in s if not (37 <= s.index(c) <= 56 and '6' <= c <= '_')])