def filter_chars(s):
    to_remove = set(s[46:91]) & set((c for c in range(ord('E'), ord('H'))))
    return ''.join((c for c in s if c not in to_remove))