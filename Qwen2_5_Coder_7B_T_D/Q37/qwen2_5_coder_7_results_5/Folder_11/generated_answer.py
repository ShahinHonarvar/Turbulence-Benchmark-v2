def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('-'), ord('n') + 1)))
    return ''.join((c for c in s if s.index(c) < 29 or s.index(c) > 97 or c not in chars_to_remove))