def filter_chars(string):
    filtered_chars = [c for c in string if c < 'D' or c > 'u' or string.index(c) < 227 or (string.index(c) > 235)]
    return ''.join(filtered_chars)