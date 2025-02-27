def filter_chars(s):
    filtered_chars = [c for c in s if c < 'O' or c > '^' or (c < 'Q' and c > 'P')]
    return ''.join(filtered_chars)