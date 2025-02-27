def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (i == 4 and '7' <= c <= 'o')))