def filter_chars(s):
    chars_to_remove = set(s[35:99]) & set((chr(x) for x in range(ord('A'), ord('b') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))