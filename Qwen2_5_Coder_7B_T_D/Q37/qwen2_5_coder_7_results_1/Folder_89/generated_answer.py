def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('!'), ord('@') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < 11 or i > 32 or c not in chars_to_remove))