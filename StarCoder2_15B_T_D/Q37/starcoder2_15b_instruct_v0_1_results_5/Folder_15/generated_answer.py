def filter_chars(s):
    chars_to_remove = set((chr(c) for c in range(ord('?'), ord('f') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 2 or s.index(c) > 6))