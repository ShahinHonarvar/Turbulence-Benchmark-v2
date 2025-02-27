def filter_chars(s):
    chars_to_remove = set(s[41:56]) & set((chr(i) for i in range(ord('a'), ord('c'))))
    return ''.join((c for c in s if c not in chars_to_remove))