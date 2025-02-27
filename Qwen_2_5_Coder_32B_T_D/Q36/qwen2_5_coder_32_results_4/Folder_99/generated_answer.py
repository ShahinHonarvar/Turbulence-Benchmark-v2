def filter_chars(s):
    if len(s) <= 948:
        return s
    to_remove = set(s[476:948]) & set((c for c in range(ord('c'), ord('d'))))
    return ''.join((c for c in s if c not in to_remove))