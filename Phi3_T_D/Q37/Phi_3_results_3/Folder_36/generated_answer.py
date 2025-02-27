def filter_chars(s):
    special_chars = set((chr(i) for i in range(ord(','), ord('3') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < 259 or (i > 502 or c not in special_chars)))