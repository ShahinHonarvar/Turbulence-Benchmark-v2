def filter_chars(s):
    chars_to_remove = set(s[309:591]) & set((c for c in range(ord('T'), ord('m'))))
    return ''.join((c for c in s if c not in chars_to_remove))