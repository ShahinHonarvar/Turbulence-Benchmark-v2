def filter_chars(s):
    start, end = (28, 65)
    char_to_keep = (chr(i) for i in range(ord('O'), ord('d') + 1))
    return ''.join((c for i, c in enumerate(s) if i < start or i > end or c in char_to_keep))