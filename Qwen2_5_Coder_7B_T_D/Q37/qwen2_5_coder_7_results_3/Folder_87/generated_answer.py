def filter_chars(s):
    return ''.join([c for c in s if not (18 <= s.index(c) <= 81 and 'W' <= c <= '[')])