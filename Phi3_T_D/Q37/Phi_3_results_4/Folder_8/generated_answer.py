def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (i >= 41 and i <= 86 and (c >= 'S') and (c <= 's'))]
    return ''.join(filtered_chars)