def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('A'), ord('U') + 1)))
    return ''.join((c for c in s if s.index(c) < 52 or s.index(c) > 81 or c not in to_remove))