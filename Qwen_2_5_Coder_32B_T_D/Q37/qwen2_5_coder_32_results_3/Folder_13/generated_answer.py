def filter_chars(s):
    if len(s) < 855:
        return s
    chars_to_remove = set(s[124:855]) & set((chr(c) for c in range(ord('9'), ord('s') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))