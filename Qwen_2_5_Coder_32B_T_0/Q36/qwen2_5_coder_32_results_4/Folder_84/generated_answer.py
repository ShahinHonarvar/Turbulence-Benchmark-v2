def filter_chars(s):
    chars_to_remove = set(s[171:636]) & set((chr(i) for i in range(ord('d'), ord('s'))))
    return ''.join((c for c in s if c not in chars_to_remove))