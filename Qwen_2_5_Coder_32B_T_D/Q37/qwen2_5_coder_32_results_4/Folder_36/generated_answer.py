def filter_chars(s):
    chars_to_remove = set(s[259:503]) & set((chr(i) for i in range(ord(','), ord('4'))))
    return ''.join((c for c in s if c not in chars_to_remove))