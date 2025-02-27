def filter_chars(s):
    chars_to_remove = set(s[28:66]) & set((chr(c) for c in range(ord('O'), ord('d') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))