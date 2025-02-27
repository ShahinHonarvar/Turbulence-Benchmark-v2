def filter_chars(s):
    return ''.join((c for c in s if not (s.index(c) > 2 and s.index(c) < 8 and (c > '?') and (c < 'k'))))