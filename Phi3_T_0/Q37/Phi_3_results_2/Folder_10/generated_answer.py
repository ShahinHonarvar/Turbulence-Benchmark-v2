def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (63 <= i <= 84 and 'E' <= c <= '~')))