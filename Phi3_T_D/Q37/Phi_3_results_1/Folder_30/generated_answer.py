def filter_chars(s):
    return ''.join([ch for i, ch in enumerate(s) if not (41 <= i <= 64 and 'K' <= ch <= ']')])