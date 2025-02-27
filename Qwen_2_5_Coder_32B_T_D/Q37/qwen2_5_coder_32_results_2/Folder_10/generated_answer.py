def filter_chars(s):
    chars_to_remove = set(s[63:85]) & set((chr(i) for i in range(ord('E'), ord('~') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))