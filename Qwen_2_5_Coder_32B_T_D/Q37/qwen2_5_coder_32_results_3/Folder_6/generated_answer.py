def filter_chars(s):
    chars_to_remove = set(s[13:29]) & set((chr(x) for x in range(ord('c'), ord('n') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))