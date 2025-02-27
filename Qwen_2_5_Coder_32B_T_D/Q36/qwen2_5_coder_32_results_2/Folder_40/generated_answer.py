def filter_chars(s):
    r = ''.join((c for i, c in enumerate(s) if not (1 < i < 7 and '-' < c < 'L')))
    return r