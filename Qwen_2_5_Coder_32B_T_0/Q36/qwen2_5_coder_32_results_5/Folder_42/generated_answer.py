def filter_chars(s):
    chars_to_remove = set(s[42:68]) & set((chr(i) for i in range(ord('u'), ord('x'))))
    return ''.join((c for c in s if c not in chars_to_remove))