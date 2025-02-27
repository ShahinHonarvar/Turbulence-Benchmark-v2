def filter_chars(s):
    to_remove = set(s[10:15]) & set((chr(c) for c in range(ord('u'), ord('t'), -1)))
    return ''.join((c for c in s if c not in to_remove))