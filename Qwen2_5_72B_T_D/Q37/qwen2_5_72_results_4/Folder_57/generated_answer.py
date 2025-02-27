def filter_chars(s):
    to_remove = set(s[27:86]) & set((chr(i) for i in range(ord('!'), ord('B') + 1)))
    return ''.join((c for c in s if c not in to_remove))