def filter_chars(string):
    filtered_chars = [c for c in string if c < '*' or c > 'j']
    return ''.join(filtered_chars)