def filter_chars(string):
    filtered = [c for c in string if c < 'E' or c > 't' or c not in string[35:90]]
    return ''.join(filtered)