def filter_chars(s):
    chars_to_remove = set(s[29:80]) & set((chr(i) for i in range(ord('K'), ord('z') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))