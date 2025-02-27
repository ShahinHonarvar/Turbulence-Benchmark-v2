def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not 23 <= i <= 89 or not 'w' <= c <= '{'])