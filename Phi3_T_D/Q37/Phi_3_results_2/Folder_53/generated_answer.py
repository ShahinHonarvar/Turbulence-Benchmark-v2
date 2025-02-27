def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if i < 83 or i > 99 or (not '*' <= c <= 'j')]
    return ''.join(filtered_chars)