def filter_chars(s):
    chars_to_remove = set(s[42:67]) & set((chr(i) for i in range(ord('7'), ord('g'))))
    return ''.join((c for c in s if c not in chars_to_remove))