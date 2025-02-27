def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 33 or i >= 36 or (not (c > '>' and c < 'A'))])