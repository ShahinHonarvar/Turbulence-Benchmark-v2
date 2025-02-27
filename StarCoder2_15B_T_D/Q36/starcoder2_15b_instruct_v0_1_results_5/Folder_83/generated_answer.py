def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if i < 72 or i >= 93 or (not ('<'.isascii() and c.isascii() and ('<' < c < 'J')))]
    return ''.join(filtered_chars)