def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (i >= 19 and i <= 90 and ('F' <= c <= 'h'))))