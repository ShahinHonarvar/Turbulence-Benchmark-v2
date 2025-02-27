def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 219 or i >= 403 or '*' <= c <= '7'))