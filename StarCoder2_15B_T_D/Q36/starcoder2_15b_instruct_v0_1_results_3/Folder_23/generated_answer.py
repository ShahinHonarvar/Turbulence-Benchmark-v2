def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if i < 21 or i >= 25 or (not (c > '5' and c < '}'))]
    return ''.join(filtered_chars)