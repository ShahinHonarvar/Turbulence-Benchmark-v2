def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 299 or i >= 418 or (not (c > '9' and c < 'P'))))