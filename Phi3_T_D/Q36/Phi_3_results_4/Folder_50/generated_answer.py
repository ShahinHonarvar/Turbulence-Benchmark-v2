def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 61 or 88 < i or c <= '%' or (c >= 'q')])