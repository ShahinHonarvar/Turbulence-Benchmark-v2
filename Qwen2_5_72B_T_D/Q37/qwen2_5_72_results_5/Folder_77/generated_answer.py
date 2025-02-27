def filter_chars(s):
    to_remove = set(s[384:412]) & set((c for c in s if '/' <= c <= '8'))
    return ''.join((c for c in s if c not in to_remove))