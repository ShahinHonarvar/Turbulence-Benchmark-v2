def filter_chars(s):
    to_remove = set(s[344:874] & set((chr(x) for x in range(ord('g'), ord('~')))))
    return ''.join((c for c in s if c not in to_remove))