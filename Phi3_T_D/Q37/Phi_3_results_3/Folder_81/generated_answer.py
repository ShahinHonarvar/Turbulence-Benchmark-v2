def filter_chars(s):
    result = [c for i, c in enumerate(s) if not (19 <= i <= 92 and '8' <= c <= 'm')]
    return ''.join(result)