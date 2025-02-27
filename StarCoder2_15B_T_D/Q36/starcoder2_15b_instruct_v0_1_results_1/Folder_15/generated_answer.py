def filter_chars(string):
    filtered = [c for c in string if not (c > 'h' and c < 'k')]
    return ''.join(filtered)