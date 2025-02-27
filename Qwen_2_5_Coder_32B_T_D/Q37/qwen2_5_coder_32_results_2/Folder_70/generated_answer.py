def filter_chars(s):
    if len(s) < 539:
        return s
    to_remove = set(s[515:539]) & set((c for c in range(ord('+'), ord('}') + 1)))
    return ''.join((c for c in s if c not in to_remove))