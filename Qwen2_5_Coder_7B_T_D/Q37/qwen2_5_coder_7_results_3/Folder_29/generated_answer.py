def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('&'), ord('v') + 1)))
    return ''.join((c for c in s if s.index(c) < 12 or s.index(c) > 88 or c not in to_remove))