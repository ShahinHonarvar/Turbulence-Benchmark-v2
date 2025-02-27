def filter_chars(string):
    filtered = [c for i, c in enumerate(string) if i < 42 or i >= 68 or (not 't' < c < 'x')]
    return ''.join(filtered)