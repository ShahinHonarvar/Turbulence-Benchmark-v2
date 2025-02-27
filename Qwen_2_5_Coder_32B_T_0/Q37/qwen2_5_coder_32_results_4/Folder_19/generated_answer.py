def filter_chars(s):
    chars_to_remove = set(s[35:90]) & set((chr(i) for i in range(ord('E'), ord('t') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))