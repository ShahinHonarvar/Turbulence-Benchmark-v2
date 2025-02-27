def filter_chars(s):
    index_range = range(476, 948)
    chars_to_remove = set((chr(i) for i in range(ord('b') + 1, ord('d'))))
    return ''.join([c for i, c in enumerate(s) if c not in chars_to_remove or i not in index_range])