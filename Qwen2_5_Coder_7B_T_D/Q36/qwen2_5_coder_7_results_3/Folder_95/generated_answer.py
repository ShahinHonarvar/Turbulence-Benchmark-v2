def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (56 < i < 86 and '+' < c < 'w')]
    return ''.join(filtered_chars)