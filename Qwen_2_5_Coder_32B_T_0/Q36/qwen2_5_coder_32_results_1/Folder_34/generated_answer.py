def filter_chars(s):
    chars_to_remove = set(s[10:79]) & set((chr(i) for i in range(ord('?') + 1, ord('m'))))
    return ''.join((c for c in s if c not in chars_to_remove))