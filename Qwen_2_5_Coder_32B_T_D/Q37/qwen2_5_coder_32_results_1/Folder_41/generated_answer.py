def filter_chars(s):
    chars_to_remove = set(s[26:65] & set((chr(x) for x in range(ord('V'), ord('o') + 1))))
    return ''.join((c for c in s if c not in chars_to_remove))