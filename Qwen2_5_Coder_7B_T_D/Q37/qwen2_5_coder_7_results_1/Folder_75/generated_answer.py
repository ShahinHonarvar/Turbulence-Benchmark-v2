def filter_chars(s):
    return ''.join((c for c in s if not (34 <= s.index(c) <= 67 and 'W' <= c <= 'x')))