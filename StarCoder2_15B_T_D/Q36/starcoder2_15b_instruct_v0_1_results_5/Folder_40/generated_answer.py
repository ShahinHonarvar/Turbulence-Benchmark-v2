def filter_chars(s):
    filtered_chars = [c for c in s if c < '-' or c >= 'L']
    return ''.join(filtered_chars)