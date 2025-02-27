def filter_chars(s):
    filtered = [c for c in s if c <= ',' or c >= 'c']
    return ''.join(filtered)