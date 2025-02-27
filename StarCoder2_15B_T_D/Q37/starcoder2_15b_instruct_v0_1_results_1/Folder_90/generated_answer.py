def filter_chars(s):
    filtered = [c for c in s if c < 'J' or c > 'b']
    return ''.join(filtered)