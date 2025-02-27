def filter_chars(s):
    if len(s) <= 79:
        return s
    chars_to_remove = set(s[10:79]) & set((chr(x) for x in range(ord('?') + 1, ord('m'))))
    return ''.join((c for c in s if c not in chars_to_remove))