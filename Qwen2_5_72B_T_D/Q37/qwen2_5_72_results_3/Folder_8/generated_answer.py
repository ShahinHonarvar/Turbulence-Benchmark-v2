def filter_chars(s):
    to_remove = set((c for c in s[41:87] if 'S' <= c <= 's'))
    return ''.join((c for c in s if c not in to_remove))