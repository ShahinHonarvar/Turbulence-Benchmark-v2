def filter_chars(s):
    return ''.join((ch for i, ch in enumerate(s) if not 52 <= i <= 81 or not 'A' <= ch <= 'U'))