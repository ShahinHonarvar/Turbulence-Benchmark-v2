def filter_chars(string):
    filtered_chars = [c for c in string if c < 'H' or c > 'e' or (c < 'H' and c > 'e')]
    return ''.join(filtered_chars)