def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (373 <= i <= 901 and 'T' <= c <= 'h')))