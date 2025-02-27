def filter_chars(s):
    chars_to_remove = set(s[373:902]) & set((chr(i) for i in range(ord('T'), ord('h') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))