def filter_chars(s):
    return ''.join((c for c in s if not (15 <= s.index(c) <= 55 and 'W' <= c <= '{')))