def filter_chars(s):
    start, end = (35, 98)
    chars_to_remove = set([chr(i) for i in range(ord('A'), ord('b') + 1)])
    return ''.join([c for i, c in enumerate(s) if (i < start or i > end) or c not in chars_to_remove])