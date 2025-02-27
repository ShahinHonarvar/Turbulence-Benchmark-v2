def filter_chars(s):
    char_set = set((chr(i) for i in range(ord('!'), ord('s') + 1)))
    return ''.join((c for c in s if c not in char_set or s.index(c) < 86 or s.index(c) > 92))