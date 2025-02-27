def filter_chars(string):
    filtered_chars = [c for c in string if c <= 'Y' or c >= 's']
    return ''.join(filtered_chars)