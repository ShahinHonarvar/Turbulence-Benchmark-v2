def filter_chars(s):
    chars_to_remove = set(s[40:63]) & set((chr(c) for c in range(ord('8'), ord('H'))))
    return ''.join((c for c in s if c not in chars_to_remove))