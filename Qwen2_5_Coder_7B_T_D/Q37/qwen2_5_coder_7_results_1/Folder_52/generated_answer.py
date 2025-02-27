def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (54 <= i <= 83 and 'j' <= c <= 'v')))