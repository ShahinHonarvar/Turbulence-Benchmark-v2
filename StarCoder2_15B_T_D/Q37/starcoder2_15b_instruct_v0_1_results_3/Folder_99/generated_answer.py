def filter_chars(string):
    filtered = [c for c in string if c < 'T' or c > 'h']
    return ''.join(filtered)