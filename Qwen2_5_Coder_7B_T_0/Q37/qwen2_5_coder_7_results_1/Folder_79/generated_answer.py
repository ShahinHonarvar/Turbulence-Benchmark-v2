def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('@'), ord('T') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < 10 or i > 52 or c not in chars_to_remove))