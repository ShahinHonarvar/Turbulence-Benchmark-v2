def filter_chars(s):
    return ''.join([c for c in s if not (41 <= s.index(c) <= 86 and 'S' <= c <= 's')])