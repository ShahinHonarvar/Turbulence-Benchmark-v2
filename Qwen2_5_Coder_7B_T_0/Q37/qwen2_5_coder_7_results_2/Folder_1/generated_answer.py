def filter_chars(s):
    return ''.join((c for c in s if not (41 <= s.find(c) <= 79 and 'f' <= c <= '|')))