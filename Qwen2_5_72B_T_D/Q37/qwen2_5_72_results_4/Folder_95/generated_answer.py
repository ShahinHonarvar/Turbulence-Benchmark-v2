def filter_chars(s):
    to_remove = set((c for c in s[35:41] if ')' <= c <= 'l'))
    return ''.join((c for c in s if c not in to_remove))