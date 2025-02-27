def filter_chars(s):
    s = ''.join((c for i, c in enumerate(s) if i < 21 or i > 43 or '+' <= c <= '8'))
    return s