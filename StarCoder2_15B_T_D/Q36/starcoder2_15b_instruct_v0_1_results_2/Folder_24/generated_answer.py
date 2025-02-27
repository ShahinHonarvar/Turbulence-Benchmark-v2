def filter_chars(s):
    filtered = [c for c in s if c <= 't' or c >= 'v']
    return ''.join(filtered)