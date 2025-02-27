def filter_chars(s):
    filtered = [c for c in s if not (c > '9' and c < 'K')]
    return ''.join(filtered)