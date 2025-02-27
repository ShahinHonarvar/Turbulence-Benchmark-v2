def filter_chars(string):
    filtered_chars = [c for c in string if c < 'X' or c > 'p']
    return ''.join(filtered_chars)