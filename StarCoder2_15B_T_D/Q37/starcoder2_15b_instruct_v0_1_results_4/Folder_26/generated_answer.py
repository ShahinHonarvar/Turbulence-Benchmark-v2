def filter_chars(s):
    filtered_chars = [c for c in s if c < 'i' or c > 'k']
    return ''.join(filtered_chars)