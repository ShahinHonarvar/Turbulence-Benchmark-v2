def filter_chars(s):
    start, end = (18, 31)
    char_set = set([chr(i) for i in range(ord('H') + 1, ord('|'))])
    return ''.join([c for i, c in enumerate(s) if not start <= i < end or c not in char_set])