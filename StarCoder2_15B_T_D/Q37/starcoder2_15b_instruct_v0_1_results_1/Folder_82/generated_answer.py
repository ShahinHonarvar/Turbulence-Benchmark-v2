def filter_chars(s):
    filtered = [c for c in s if c < 'P' or c > 'x']
    return ''.join(filtered)