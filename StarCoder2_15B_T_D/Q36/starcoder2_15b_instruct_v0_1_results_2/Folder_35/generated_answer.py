def filter_chars(s):
    filtered = [c for c in s if not (c > '(' and c < ')')]
    return ''.join(filtered)