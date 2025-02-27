def filter_chars(string):
    filtered_chars = [c for c in string if c <= 'B' or c >= 'v']
    return ''.join(filtered_chars)