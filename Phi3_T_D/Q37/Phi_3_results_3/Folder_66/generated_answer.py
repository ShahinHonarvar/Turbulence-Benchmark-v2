def filter_chars(s):
    result = ''.join((c for i, c in enumerate(s) if not (27 <= i <= 85 and 'c' <= c <= 'i')))
    return result