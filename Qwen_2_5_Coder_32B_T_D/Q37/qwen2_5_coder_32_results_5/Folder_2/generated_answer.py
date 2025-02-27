def filter_chars(s):
    if len(s) < 985:
        return s
    chars_to_remove = set(s[477:985]) & set((chr(i) for i in range(ord(','), ord('V') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))