def filter_chars(string):
    valid_chars = [c for c in string if c <= '*' or c >= '7']
    return ''.join(valid_chars)