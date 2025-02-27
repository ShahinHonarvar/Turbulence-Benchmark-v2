def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (19 <= i <= 22 and ']' <= c <= 't')))