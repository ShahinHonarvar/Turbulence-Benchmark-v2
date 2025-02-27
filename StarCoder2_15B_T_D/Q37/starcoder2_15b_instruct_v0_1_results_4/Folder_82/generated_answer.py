def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if i < 12 or i > 25 or c < 'P' or (c > 'x')]
    return ''.join(filtered_chars)