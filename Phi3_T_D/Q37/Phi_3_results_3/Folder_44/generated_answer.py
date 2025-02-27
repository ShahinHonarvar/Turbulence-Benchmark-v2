def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (21 <= i <= 43 and '+' <= c <= '8')])