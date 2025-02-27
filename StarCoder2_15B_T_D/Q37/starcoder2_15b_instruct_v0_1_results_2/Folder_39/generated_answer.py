def filter_chars(string):
    allowed_chars = set((chr(c) for c in range(ord('A'), ord('U') + 1)))
    return ''.join((c for c in string if c not in allowed_chars or string.index(c) < 52 or string.index(c) > 81))