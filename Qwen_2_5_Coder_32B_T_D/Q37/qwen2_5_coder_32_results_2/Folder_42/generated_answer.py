def filter_chars(s):
    if len(s) < 75:
        return s
    to_remove = set(s[73:75]) & set((chr(i) for i in range(ord('U'), ord('l') + 1)))
    return ''.join((c for c in s if c not in to_remove))