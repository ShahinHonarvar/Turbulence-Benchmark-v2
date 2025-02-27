def filter_chars(s):
    return ''.join((c for c in s if not (20 <= s.index(c) <= 62 and 'i' <= c <= 'k')))