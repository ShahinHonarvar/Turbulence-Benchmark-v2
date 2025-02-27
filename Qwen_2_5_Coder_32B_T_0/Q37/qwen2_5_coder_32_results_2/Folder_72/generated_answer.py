def filter_chars(s):
    chars_to_remove = set(s[35:52]) & set((chr(i) for i in range(ord('H'), ord('s') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))