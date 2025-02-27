def filter_chars(s):
    chars_to_remove = set(s[502:946]) & set((chr(i) for i in range(ord('X'), ord('y'))))
    return ''.join((c for c in s if c not in chars_to_remove))