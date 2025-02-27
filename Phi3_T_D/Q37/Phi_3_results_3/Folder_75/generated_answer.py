def filter_chars(s):
    return ''.join((ch for i, ch in enumerate(s) if not 34 <= i <= 67 or not 'W' <= ch <= 'x'))