def filter_chars(s):
    return ''.join((c for c in s if not (379 <= s.index(c) <= 898 and 'M' <= c <= 'v')))