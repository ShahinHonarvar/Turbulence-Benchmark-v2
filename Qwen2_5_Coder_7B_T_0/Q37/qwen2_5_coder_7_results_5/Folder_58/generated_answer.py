def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (503 <= i <= 753 and '9' <= c <= 'w')))