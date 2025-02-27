def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (71 <= i <= 94 and 'K' <= c <= 'a')))