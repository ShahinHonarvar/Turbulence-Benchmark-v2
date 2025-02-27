def filter_chars(s):
    chars_to_remove = set(s[19:33]) & set((chr(i) for i in range(ord('f'), ord('o') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))