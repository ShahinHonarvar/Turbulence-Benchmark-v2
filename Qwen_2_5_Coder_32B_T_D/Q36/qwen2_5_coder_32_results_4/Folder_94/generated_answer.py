def filter_chars(s):
    chars_to_remove = set(s[15:85]) & set((chr(x) for x in range(ord('J'), ord('M'))))
    return ''.join((c for c in s if c not in chars_to_remove))