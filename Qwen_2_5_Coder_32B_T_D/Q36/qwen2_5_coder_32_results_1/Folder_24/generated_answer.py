def filter_chars(s):
    chars_to_remove = set(s[10:15]) & set((chr(i) for i in range(ord('u'), ord('t'), -1)))
    return ''.join((c for c in s if c not in chars_to_remove))