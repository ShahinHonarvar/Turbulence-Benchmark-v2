def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if i < 58 or i >= 81 or c <= '5' or (c >= '>')]
    return ''.join(filtered_chars)