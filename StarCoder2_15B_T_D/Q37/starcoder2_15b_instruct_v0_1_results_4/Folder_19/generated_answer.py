def filter_chars(s):
    valid_chars = [ch for i, ch in enumerate(s) if 35 <= i <= 89 and 'E' <= ch <= 't']
    return ''.join(valid_chars)