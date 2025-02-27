def filter_chars(s):
    return ''.join((c for c in s if not (8 <= s.index(c) <= 9 and 'R' <= c <= 't')))