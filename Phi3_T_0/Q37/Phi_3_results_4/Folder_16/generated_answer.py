def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (225 <= i <= 381 and 'D' <= c <= 'Y')))