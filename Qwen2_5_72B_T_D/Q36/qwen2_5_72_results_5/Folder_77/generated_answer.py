def filter_chars(s):
    to_remove = set((c for c in s[221:419] if '-' < c < 'v'))
    return ''.join((c for c in s if c not in to_remove))