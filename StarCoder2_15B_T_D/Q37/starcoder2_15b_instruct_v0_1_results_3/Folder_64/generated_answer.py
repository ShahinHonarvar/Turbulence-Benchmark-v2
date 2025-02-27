def filter_chars(s):
    filtered = [c for i, c in enumerate(s) if i < 1 or i > 7 or (not 'L' <= c <= 'a')]
    return ''.join(filtered)