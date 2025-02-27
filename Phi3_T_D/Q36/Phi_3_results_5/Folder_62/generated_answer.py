def filter_chars(s):
    subset_chars_range = set((chr(i) for i in range(ord('*') + 1, ord('w'))))
    return ''.join([ch for i, ch in enumerate(s) if i < 63 or i >= 89 or ch not in subset_chars_range])