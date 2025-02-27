def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if not 124 <= i <= 854 or not '9' <= c <= 's']
    return ''.join(filtered_chars)