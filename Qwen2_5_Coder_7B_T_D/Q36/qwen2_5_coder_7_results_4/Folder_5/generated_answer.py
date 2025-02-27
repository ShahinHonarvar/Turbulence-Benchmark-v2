def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (55 < i < 66 and 'f' < c < '|')]
    return ''.join(filtered_chars)