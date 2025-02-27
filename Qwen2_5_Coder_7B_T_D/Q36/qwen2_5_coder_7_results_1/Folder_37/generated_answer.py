def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if i not in range(44, 59) or not (c > '/' and c < '6')]
    return ''.join(filtered_chars)