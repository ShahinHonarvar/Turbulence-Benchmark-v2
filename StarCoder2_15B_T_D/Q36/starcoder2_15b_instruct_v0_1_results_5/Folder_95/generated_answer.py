def filter_chars(s):
    remove_chars = set((chr(i) for i in range(ord('+') + 1, ord('w'))))
    return ''.join((c for c in s if c not in remove_chars or s.index(c) < 56 or s.index(c) >= 86))