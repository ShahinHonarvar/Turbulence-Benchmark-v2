def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (25 <= i <= 97 and 'm' <= c <= 'w')))