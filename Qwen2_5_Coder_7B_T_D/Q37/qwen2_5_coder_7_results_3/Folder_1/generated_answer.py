def filter_chars(s):
    return ''.join((c for c in s if not (41 <= s.index(c) <= 79 and 'f' <= c <= '|')))