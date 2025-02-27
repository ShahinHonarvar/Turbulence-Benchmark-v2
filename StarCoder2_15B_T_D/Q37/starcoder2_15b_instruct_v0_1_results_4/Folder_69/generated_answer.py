def filter_chars(string):
    filtered = [c for i, c in enumerate(string) if i < 114 or i > 639 or c < '!' or (c > 'x')]
    return ''.join(filtered)