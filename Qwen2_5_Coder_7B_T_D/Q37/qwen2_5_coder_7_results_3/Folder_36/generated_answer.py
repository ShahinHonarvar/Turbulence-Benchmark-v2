def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if (i < 259 or i > 502) or not ',' <= c <= '3'])