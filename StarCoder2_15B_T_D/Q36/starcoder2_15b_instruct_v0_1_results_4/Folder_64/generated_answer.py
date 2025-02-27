def filter_chars(text):
    return ''.join((c for i, c in enumerate(text) if not (1 < i < 7 and '4' < c < '^')))