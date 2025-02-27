def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (12 <= i <= 88 and ' &' <= c <= 'v')))