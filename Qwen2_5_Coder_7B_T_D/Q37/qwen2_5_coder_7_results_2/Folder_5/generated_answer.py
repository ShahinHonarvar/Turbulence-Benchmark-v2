def filter_chars(s):
    return ''.join([c for c in s if not (24 <= s.index(c) <= 82 and '5' <= c <= '<')])