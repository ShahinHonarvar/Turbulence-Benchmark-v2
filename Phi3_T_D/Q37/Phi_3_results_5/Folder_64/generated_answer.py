def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not (1 <= i <= 7 and 'L' <= c <= 'a')]
    return ''.join(filtered_chars)