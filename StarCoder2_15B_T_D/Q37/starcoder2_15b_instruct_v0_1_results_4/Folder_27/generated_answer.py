def filter_chars(string):
    filtered_chars = [c for c in string if c < '=' or c > 'E' or (c < '43' or c > '80')]
    return ''.join(filtered_chars)