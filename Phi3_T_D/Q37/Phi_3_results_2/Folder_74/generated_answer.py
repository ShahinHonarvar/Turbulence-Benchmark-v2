def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 19 <= i <= 32 or not 'f' <= c <= 'o'))