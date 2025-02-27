def filter_chars(string):
    filtered_chars = [c for c in string if c < 'H' or c > 'e' or string.index(c) < 38 or (string.index(c) > 69)]
    return ''.join(filtered_chars)