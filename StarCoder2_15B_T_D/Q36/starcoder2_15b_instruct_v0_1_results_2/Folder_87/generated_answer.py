def filter_chars(s):
    filtered = [c for c in s if not (c > '3' and c < 'D')]
    return ''.join(filtered)