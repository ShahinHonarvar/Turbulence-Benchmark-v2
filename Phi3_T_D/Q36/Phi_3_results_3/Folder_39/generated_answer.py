def filter_chars(s):
    chars_to_remove = set((chr(x) for x in range(ord('5') + 1, ord('C'))))
    return ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or not 43 < i < 59))