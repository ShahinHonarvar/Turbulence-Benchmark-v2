def filter_chars(s):
    target_range = set((chr(i) for i in range(ord('8'), ord('e') + 1)))
    return ''.join((c for i, c in enumerate(s) if not (i < 75 or i > 99 or c in target_range)))