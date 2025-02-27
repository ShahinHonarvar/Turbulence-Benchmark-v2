def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (i >= 21 and i <= 43) or (c < '+' or c > '8')))