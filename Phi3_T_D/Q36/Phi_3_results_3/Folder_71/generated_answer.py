def filter_chars(s):
    filtered_chars = [c for idx, c in enumerate(s) if not 82 < idx < 89 and '*' < c < '[' and (c in s)]
    return ''.join(filtered_chars)