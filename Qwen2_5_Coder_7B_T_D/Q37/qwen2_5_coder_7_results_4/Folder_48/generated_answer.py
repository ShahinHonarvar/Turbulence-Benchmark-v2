def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('?'), ord('n') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < 513 or i > 877 or c not in to_remove))