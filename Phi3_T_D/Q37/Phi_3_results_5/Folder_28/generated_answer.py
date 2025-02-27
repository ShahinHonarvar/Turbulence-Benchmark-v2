def filter_chars(s):
    filtered = [c for i, c in enumerate(s) if i < 20 or i > 79 or (not '!' <= c <= 'T')]
    return ''.join(filtered)