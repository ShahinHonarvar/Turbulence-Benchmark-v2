def filter_chars(s):
    target_chars = set(s[34:68]) & set((chr(i) for i in range(ord('W'), ord('x') + 1)))
    return ''.join((c for c in s if c not in target_chars))