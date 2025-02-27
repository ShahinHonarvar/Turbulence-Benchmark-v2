def filter_chars(s):
    chars_to_remove = set(s[26:65]) & set((c for c in range(ord('V'), ord('p'))))
    return ''.join((c for c in s if c not in chars_to_remove))